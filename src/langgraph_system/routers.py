from typing import Literal
from langchain_core.messages import AIMessage

# Monitor agent router
def monitor_router(state) -> Literal["call_tool", "proceed_to_profile"]:
    messages = state["messages"]
    last_message = messages[-1]
    if "proceed_to_profile" in last_message.content:
        return "proceed_to_profile"
    return "call_tool"

# Profile agent router
def profile_router(state) -> Literal["call_tool", "proceed_to_decision"]:
    messages = state["messages"]
    last_message = messages[-1]
    if "proceed_to_decision" in last_message.content:
        return "proceed_to_decision"
    return "call_tool"

# Decision agent router
def decision_router(state) -> Literal["call_tool", "end"]:
    messages = state["messages"]
    last_message = messages[-1]
    if "end" in last_message.content:
        return "end"
    return "call_tool"
