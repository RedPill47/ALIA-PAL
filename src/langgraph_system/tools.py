# tools.py

from langchain_core.tools import tool
import json

# Define tools that will be used in the workflow

import json
import os

# Define the path to the JSON database file
DATABASE_FILE = 'tutor_ai_crew/src/langgraph_system/student_data.json'

# Function to read data from the JSON database
def read_student_data(student_id):
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r') as f:
            data = json.load(f)
        return data.get(student_id)
    return None

# Function to write data to the JSON database
def write_student_data(student_id, progress_data, quiz_result):
    data = {}
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'r') as f:
            data = json.load(f)
    data[student_id] = {"progress_data": progress_data, "quiz_result": quiz_result}
    with open(DATABASE_FILE, 'w') as f:
        json.dump(data, f, indent=4)


@tool
def analyze_progress(student_id):
    """
    Analyze the student's progress and return feedback.
    """
    student_data = read_student_data(student_id)
    if not student_data or 'progress_data' not in student_data:
        raise ValueError(f"No progress data found for student {student_id}")
    progress_data = student_data['progress_data']
    # Now use progress_data to perform the analysis
    return {"analysis": f"Progress analysis for student {student_id} completed."}

@tool
def trigger_crewai() -> str:
    """
    Trigger the CrewAI to generate new learning material for the student.
    """
    return "CrewAI has been triggered to generate new learning materials."

@tool
def generate_quiz(student_profile: dict) -> str:
    """
    Generate a quiz based on the student's profile and progress.
    """
    if not student_profile:
        return "No student profile provided."
    
    # Generate a quiz based on the profile details
    return f"Quiz generated for student {student_profile.get('student_id', 'unknown')} based on current progress."

@tool
def update_profile(student_profile: dict) -> str:
    """
    Update the student's profile with new progress or feedback.
    """
    if not student_profile:
        return "No student profile provided."
    
    # Update logic for student profile
    student_id = student_profile.get("student_id", "unknown")
    return f"Profile for student {student_id} has been updated with new data."

@tool
def get_learning_materials(student_profile: dict) -> str:
    """
    Retrieve appropriate learning materials for the student.
    """
    if not student_profile:
        return "No student profile provided."
    
    # Example logic to fetch materials
    return f"Learning materials retrieved for student {student_profile.get('student_id', 'unknown')}."

@tool
def record_feedback(feedback: str) -> str:
    """
    Record feedback from the student interaction and store it in the system.
    """
    if not feedback:
        return "No feedback provided."
    
    # Logic to store feedback
    return f"Feedback recorded: {feedback}"


@tool
def send_quiz_results(student_id):
    """
    Send the quiz result to the student's profile or to the system for analysis.
    """
    student_data = read_student_data(student_id)
    if not student_data or 'quiz_result' not in student_data:
        raise ValueError(f"No quiz result found for student {student_id}")
    quiz_result = student_data['quiz_result']
    # Now use quiz_result to send the results
    return {"result": f"Quiz results for student {student_id} sent."}
