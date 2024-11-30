# my_agent/utils/state.py

from typing import TypedDict, Annotated, Sequence
from langchain.schema import BaseMessage
from langgraph.graph import add_messages

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    report: str
    processed_report: str
    decision: str
    crew_response: str
    # Fields for crew outputs
    lesson_content: str
    quiz_content: str
    teaching_prompts_content: str
    # Fields for student info
    pdf: str
    query: str
    student_name: str
    student_level: str
    learning_preferences: str
    feedback: str
    crew_result: dict