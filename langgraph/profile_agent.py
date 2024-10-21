from langgraph.agent import Agent

class ProfileAgent(Agent):
    def __init__(self):
        super().__init__()
        self.profile_data = {}

    def save_student_profile(self, student_profile):
        """Store the student's profile in memory (or database)."""
        self.profile_data = student_profile

    def get_student_profile(self):
        """Retrieve the stored student profile."""
        return self.profile_data
