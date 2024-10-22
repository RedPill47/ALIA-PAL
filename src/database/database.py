# src/database/database.py

class Database:
    def __init__(self):
        # Simulate a database with a dictionary
        self.students = {
            'student_123': {
                'name': 'John Doe',
                'level': 'Intermediate',
                'preferences': 'Visual learning',
                'feedback': ''
            }
        }

    def fetch_student_profile(self, student_id):
        return self.students.get(student_id)

    def update_student_profile(self, student_id, profile_data):
        self.students[student_id].update(profile_data)
        return True
