from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END
from my_agent.utils.nodes import (
    monitor_agent_node,
    collect_student_info,      # Added import
    student_profile_agent_node,
    decision_engine_node,
    crew_ai_node,
    monitor_agent_decision,    # Added import
    decision_logic,
)
from my_agent.utils.state import AgentState

# Define the config
class GraphConfig(TypedDict):
    model_name: Literal["openai"]

# Define a new graph
workflow = StateGraph(AgentState, config_schema=GraphConfig)

# Add nodes
workflow.add_node("monitor_agent", monitor_agent_node)
workflow.add_node("collect_student_info", collect_student_info)  # Added node
workflow.add_node("student_profile_agent", student_profile_agent_node)
workflow.add_node("decision_engine", decision_engine_node)
workflow.add_node("crew_ai", crew_ai_node)

# Set the entry point as `monitor_agent`
workflow.set_entry_point("monitor_agent")

# Modify conditional edge from `monitor_agent`
workflow.add_conditional_edges(
    "monitor_agent",
    monitor_agent_decision,  # Function to decide whether to continue or proceed
    {
        "continue": "monitor_agent",
        "proceed": "collect_student_info",  # Proceed to collect student info
    },
)

# Add edge from `collect_student_info` to `student_profile_agent`
workflow.add_edge("collect_student_info", "student_profile_agent")

# Edge from `student_profile_agent` to `decision_engine`
workflow.add_edge("student_profile_agent", "decision_engine")

# Add conditional edges from `decision_engine`
workflow.add_conditional_edges(
    "decision_engine",
    decision_logic,
    {
        "request_adjustments": "crew_ai",
        "initialize_recommendations": "crew_ai",
        "continue": "monitor_agent",
    },
)

# From `crew_ai`, loop back to `monitor_agent`
workflow.add_edge("crew_ai", "monitor_agent")

# Compile the graph
graph = workflow.compile()
