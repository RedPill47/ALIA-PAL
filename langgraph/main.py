from decision_engine import DecisionEngineAgent
from monitor_agent import MonitorAgent
from profile_agent import ProfileAgent

def main():
    # Initialize the agents
    decision_engine = DecisionEngineAgent()
    monitor_agent = MonitorAgent()
    profile_agent = ProfileAgent()

    # Example student profile
    student_profile = {
        'name': 'John Doe',
        'learning_preferences': 'prefers detailed explanation and examples',
        'level': 'Beginner',
        'feedback': 'Struggles with quizzes',
    }

    # Save student profile
    profile_agent.save_student_profile(student_profile)

    # Simulate student progress (quiz score from Monitor Agent)
    quiz_score = monitor_agent.track_progress(45)  # Simulating a low score

    # Decision Engine analyzes performance and decides what to do next
    task_to_modify = decision_engine.analyze_performance(quiz_score)

    # Notify CrewAI to replay or adjust the task
    decision_engine.notify_crewai(task_to_modify, student_profile)

if __name__ == "__main__":
    main()
