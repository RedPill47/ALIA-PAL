import os
import functools
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
from dotenv import load_dotenv

from langgraph_system.agents import *  # Import agent creation functions from agents.py
from langgraph_system.tools import *   # Import tool functions from tools.py
from langgraph_system.routers import *  # Import router functions from routers.py

# Load environment variables from .env
load_dotenv()

# Initialize the LLM
GPT_MODEL = "gpt-4o"
llm = ChatOpenAI(model=GPT_MODEL)

# Memory setup using synchronous saver
memory = AsyncSqliteSaver.from_conn_string(":memory:")

# Agents creation
monitor_agent = create_agent(
    agentName='monitor', 
    llm=llm, 
    tools=[analyze_progress, send_quiz_results], 
    system_message="You are the monitor agent responsible for tracking student quiz behavior."
)
monitor_node = functools.partial(agent_node, agent=monitor_agent, name='monitor')

profile_agent = create_agent(
    agentName='profile', 
    llm=llm, 
    tools=[update_profile], 
    system_message="You are the profile agent responsible for updating student profiles based on their quiz results."
)
profile_node = functools.partial(agent_node, agent=profile_agent, name='profile')

decision_agent = create_agent(
    agentName='decision', 
    llm=llm, 
    tools=[trigger_crewai], 
    system_message="You are the decision agent, responsible for deciding if the student should proceed, retry, or start CrewAI."
)
decision_node = functools.partial(agent_node, agent=decision_agent, name='decision')

# Tool nodes
monitor_tools = [analyze_progress, send_quiz_results]
profile_tools = [update_profile]
decision_tools = [trigger_crewai]

monitor_tool_node = ToolNode(monitor_tools)
profile_tool_node = ToolNode(profile_tools)
decision_tool_node = ToolNode(decision_tools)

# Define the workflow
workflow = StateGraph(AgentState)
workflow.add_node("monitor", monitor_node)
workflow.add_node("profile", profile_node)
workflow.add_node("decision", decision_node)

workflow.add_node("monitor_call_tool", monitor_tool_node)
workflow.add_node("profile_call_tool", profile_tool_node)
workflow.add_node("decision_call_tool", decision_tool_node)

# Add conditional edges to guide the flow
workflow.add_conditional_edges(
    "monitor",
    monitor_router,
    {"call_tool": "monitor_call_tool", "proceed_to_profile": "profile"}
)

workflow.add_conditional_edges(
    "profile",
    profile_router,
    {"call_tool": "profile_call_tool", "proceed_to_decision": "decision"}
)

workflow.add_conditional_edges(
    "decision",
    decision_router,
    {"call_tool": "decision_call_tool", "end": END}
)

# Add edges to transition back from tool nodes
workflow.add_edge("monitor_call_tool", "monitor")
workflow.add_edge("profile_call_tool", "profile")
workflow.add_edge("decision_call_tool", "decision")

# Start the graph
workflow.add_edge(START, "monitor")

# Compile the graph with synchronous memory
graph = workflow.compile(checkpointer=memory)
