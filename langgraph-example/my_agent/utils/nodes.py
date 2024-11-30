from functools import lru_cache
from langchain.chat_models import ChatOpenAI
from my_agent.utils.tools import tools

@lru_cache(maxsize=4)
def _get_model(model_name: str):
    if model_name == "openai":
        model = ChatOpenAI(temperature=0, model_name="gpt-4")
    else:
        raise ValueError(f"Unsupported model type: {model_name}")
    return model

# Monitor Agent Node
system_prompt_monitor = """You are a helpful educational assistant. You interact with the student, answer their questions, teach them, evaluate their progress, and generate a report about their learning style and progress.

When interacting with the student, please follow this format:
1. Provide an informative response to the student's message.
2. At the end of your response, include a section titled '[Report]:' where you evaluate the student's progress and learning style. This report should be brief and focused.

Example:
[Assistant's reply to student]

[Report]:
- Student shows good understanding of the material.
- Learning style: visual learner.
"""

def monitor_agent_node(state, config):
    messages = state.get("messages", [])
    model_name = config.get('configurable', {}).get("model_name", "openai")
    model = _get_model(model_name)

    # Include any updates from `crew_ai_node`
    crew_response = state.get("crew_response", "")
    if crew_response:
        messages.append({"role": "system", "content": f"Update from crew: {crew_response}"})
        # Clear the crew response after using it
        state["crew_response"] = ""

    # Prepare messages
    full_messages = [{"role": "system", "content": system_prompt_monitor}] + messages

    response = model.invoke(full_messages)
    assistant_reply = response.content

    # Parse assistant reply and report
    if "\n\n[Report]:" in assistant_reply:
        reply_content, report_section = assistant_reply.split("\n\n[Report]:", 1)
        report = report_section.strip()
    else:
        reply_content = assistant_reply
        report = ""

    # Update state
    state["messages"].append({"role": "assistant", "content": reply_content})
    state["report"] = report

    return state

# Student Profile Agent Node
def student_profile_agent_node(state, config):
    report = state.get("report", "")
    if not report:
        # No report to process
        return state

    prompt = f"""You are an assistant that processes student reports for storage in a database.
Rewrite the following report in a structured JSON format suitable for storing in a database:

Report:
{report}

The JSON should have the following fields:
- 'progress': description of the student's progress
- 'learning_style': description of the student's learning style
"""
    model_name = config.get('configurable', {}).get("model_name", "openai")
    model = _get_model(model_name)
    response = model.invoke([{"role": "user", "content": prompt}])
    processed_report = response.content
    state["processed_report"] = processed_report
    return state

# Decision Engine Node
def decision_engine_node(state, config):
    processed_report = state.get("processed_report", "")
    if not processed_report:
        state["decision"] = "continue"
        return state

    prompt = f"""You are a decision engine that decides whether to trigger adjustments or recommendations based on the student's progress.
Analyze the following processed report and decide whether to:

- Output 'request_adjustments' if the student needs adjustments to their course (e.g., make it harder, easier, or change something).
- Output 'initialize_recommendations' if the student needs new recommendations.
- Output 'continue' if no action is needed.

Only output one of the above options.

Processed Report:
{processed_report}
"""

    model_name = config.get('configurable', {}).get("model_name", "openai")
    model = _get_model(model_name)
    response = model.invoke([{"role": "user", "content": prompt}])
    decision = response.content.strip().lower()

    if "request_adjustments" in decision:
        state["decision"] = "request_adjustments"
    elif "initialize_recommendations" in decision:
        state["decision"] = "initialize_recommendations"
    else:
        state["decision"] = "continue"

    return state

# Decision Logic for Conditional Edge
def decision_logic(state):
    decision = state.get("decision", "continue")
    if decision == "request_adjustments":
        return "request_adjustments"
    elif decision == "initialize_recommendations":
        return "initialize_recommendations"
    else:
        return "continue"

# CrewAI Node
def crew_ai_node(state, config):
    # Determine the action based on the decision
    decision = state.get("decision", "")
    if decision == "request_adjustments":
        action = "adjusted the course based on your progress."
    elif decision == "initialize_recommendations":
        action = "provided new recommendations for your learning path."
    else:
        action = "processed your request."

    state["crew_response"] = f"The crew has {action}"
    return state
