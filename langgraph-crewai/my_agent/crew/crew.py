# my_agent/crew/crew.py

from crewai import Crew, Process
from .agents import TutorAgents
from .tasks import TutorTasks

class TutorCrew:
    def __init__(self):
        agents = TutorAgents()
        self.file_manager = agents.file_manager()
        self.tutor = agents.tutor()
        self.practical = agents.practical()
        self.teacher_persona = agents.teacher_persona()

        self.agents = [
            self.file_manager,
            self.tutor,
            self.practical,
            self.teacher_persona
        ]

    def kickoff(self, state):
        # Retrieve parameters from state
        pdf = state.get('pdf')
        query = state.get('query', 'course material')
        student_name = state.get('student_name')
        student_level = state.get('student_level')
        learning_preferences = state.get('learning_preferences')
        feedback = state.get('feedback')

        # Initialize tasks
        tasks = TutorTasks()
        task_list = [
            tasks.process_file(self.file_manager, pdf, query),
            tasks.adapt_learning_path(self.tutor, student_name, student_level, learning_preferences, feedback),
            tasks.create_quiz(self.practical, student_level, learning_preferences, feedback),
            tasks.create_teaching_prompts(self.teacher_persona, student_name, feedback),
        ]

        crew = Crew(
            agents=self.agents,
            tasks=task_list,
            process=Process.sequential,
            memory=True,
            verbose=True,
        )

        # Run the crew
        result = crew.kickoff()

        # Store outputs in the output directory
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        # Assuming each task writes its output to a file specified in `output_file`

        # Read the outputs to pass to the monitor_agent_node
        lesson_path = os.path.join(output_dir, 'lesson.md')
        quiz_path = os.path.join(output_dir, 'quiz.json')
        teaching_prompts_path = os.path.join(output_dir, 'teaching_prompts.md')

        with open(lesson_path, 'r') as f:
            lesson_content = f.read()

        with open(quiz_path, 'r') as f:
            quiz_content = f.read()

        with open(teaching_prompts_path, 'r') as f:
            teaching_prompts_content = f.read()

        # Update state with the content
        state['lesson_content'] = lesson_content
        state['quiz_content'] = quiz_content
        state['teaching_prompts_content'] = teaching_prompts_content

        # Optionally, include a message from the crew
        state["crew_response"] = "The course and quiz have been prepared and are ready for the student."

        return state
