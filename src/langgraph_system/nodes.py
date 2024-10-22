# src/langgraph_system/nodes.py

from langgraph import Node
from database.database import Database

class StudentProfileNode(Node):
    def __init__(self, config):
        super().__init__(config)
        self.database = Database()

    def process(self, data):
        student_id = data.get('student_id')
        if data.get('action') == 'fetch':
            profile = self.database.fetch_student_profile(student_id)
            return {'student_profile': profile}
        elif data.get('action') == 'update':
            updated_profile = data.get('updated_profile')
            self.database.update_student_profile(student_id, updated_profile)
            return {'status': 'profile_updated'}

class MonitorNode(Node):
    def __init__(self, config):
        super().__init__(config)

    def process(self, data):
        # Simulate interaction with student
        student_activity = self.collect_student_activity()
        return {'student_activity': student_activity}

    def collect_student_activity(self):
        # Placeholder for actual student activity collection
        return {'quiz_scores': [80, 90], 'time_spent': 120}

class DecisionEngineNode(Node):
    def __init__(self, config):
        super().__init__(config)

    def process(self, data):
        student_profile = data.get('student_profile')
        student_activity = data.get('student_activity')
        decision = self.make_decision(student_profile, student_activity)
        return {'adjustment_needed': decision}

    def make_decision(self, profile, activity):
        # Placeholder logic for decision-making
        if activity['quiz_scores'][-1] < 70:
            return True
        else:
            return False

class TeacherProfileNode(Node):
    def __init__(self, config):
        super().__init__(config)

    def process(self, data):
        # Provide teaching prompts based on content
        teaching_prompts = self.generate_teaching_prompts(data)
        return {'teaching_prompts': teaching_prompts}

    def generate_teaching_prompts(self, data):
        # Placeholder for generating teaching prompts
        return "Teaching prompts based on the new content."

class EducationalCrewAINode(Node):
    def __init__(self, config, crew_ai):
        super().__init__(config)
        self.crew_ai = crew_ai

    def process(self, data):
        student_profile = data.get('student_profile')
        # Assuming student_profile contains necessary fields
        self.crew_ai.run(
            pdf='C:/Users/hedit/Personal projects/crewai_test/tutor_ai_crew/input/lesson-3.pdf',
            student_name=student_profile.get('name'),
            student_level=student_profile.get('level'),
            learning_preferences=student_profile.get('preferences'),
            feedback=student_profile.get('feedback', '')
        )
        return {'status': 'crew_ai_completed'}
