from typing import TypedDict, Annotated, Sequence
from langchain.schema import BaseMessage
from langgraph.graph import add_messages

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    report: str
    processed_report: str
    decision: str
    crew_response: str
