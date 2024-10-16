from langgraph.agent import Agent
from tutor_ai_crew.src.tutor_ai_crew.main import run

class DecisionEngineAgent(Agent):
    def __init__(self):
        # Initialize the Decision Engine Agent
        super().__init__()
        self.student_profile = {}

    def collect_student_data(self, student_data):
        """
        Collect initial student data and store it in the agent's memory.
        """
        self.student_profile = student_data

    def analyze_performance(self, quiz_score):
        """
        Analyze the student's performance and make decisions about next steps.
        """
        # Example decision-making based on quiz score
        if quiz_score < 50:
            # If the quiz score is low, replay the quiz task with easier questions
            return "create_quiz"
        elif quiz_score >= 50 and quiz_score < 80:
            # If the quiz score is moderate, replay the course task with simplified content
            return "adapt_learning_path"
        else:
            # If the student performs well, proceed to the next section
            return "proceed"

    def notify_crewai(self, task_id, student_profile):
        """
        Notify CrewAI to replay a specific task or proceed.
        """
        print(f"Notifying CrewAI to modify task {task_id} based on student progress.")
        # Here you would call CrewAI's replay function or kickoff depending on the task_id
        run(student_profile, task_to_modify=task_id)









####################


"""

# Example of running the Decision Engine
if __name__ == "__main__":
    decision_engine = DecisionEngineAgent()

    # Example student data
    student_profile = {
        'name': 'John Doe',
        'learning_preferences': 'prefers detailed explanation and examples',
        'level': 'Beginner',
        'feedback': 'Struggles with quizzes',
    }

    # Collect student data
    decision_engine.collect_student_data(student_profile)

    # Example quiz score from monitoring
    quiz_score = 45  # Assume the student scored 45 out of 100

    # Decision-making based on the quiz score
    task_id = decision_engine.analyze_performance(quiz_score)

    # Notify CrewAI to replay or modify tasks
    decision_engine.notify_crewai(task_id, student_profile)

"""