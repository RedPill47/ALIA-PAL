# my_agent/crew/tasks.py

from crewai import Task
from textwrap import dedent

class TutorTasks:
    def process_file(self, agent, pdf, query):
        description = dedent(f"""\
            Take a deep breath and work on this step by step.
            Extract and process information from the provided {pdf} file.
            Scan the entire document for the {query} requested.
            Make sure you extract only the {query} from the document.
        """)
        expected_output = dedent(f"""\
            Extracted {query} as it is, from the {pdf} file, without any modification.
        """)
        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )

    def adapt_learning_path(self, agent, student_name, student_level, learning_preferences, feedback):
        description = dedent(f"""\
            Take a deep breath and work on this step by step.
            Create a comprehensive and engaging course based on the provided lesson for {student_name} and tailor it according to the student's preferences: {learning_preferences}, their level: {student_level}, and progress.
            DO NOT include the quiz in the lesson; let the Practical Tutor Agent handle that.
            Make sure to adapt the content and follow the given feedback to improve the learning experience: {feedback}.
        """)
        expected_output = dedent("""\
            A complete and ready-to-deliver tailored lesson explaining the important concepts of the course.
            Formatted as markdown without '```'
        """)
        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent,
            output_file='lesson.md'
        )

    def create_quiz(self, agent, student_level, learning_preferences, feedback):
        description = dedent(f"""\
            Take a deep breath and work on this step by step.
            Create an interactive quiz based on the provided lesson.
            Ensure the quiz is engaging and reinforces the theoretical knowledge of the course.
            Take into account the student's preferences: {learning_preferences}, their level: {student_level}, and progress.
            Make sure to adapt the content and follow the given feedback to improve the learning experience: {feedback}.
            Ensure to check with a human if the draft is good before finalizing your answer.
        """)
        expected_output = dedent("""\
            An interactive quiz of 10 questions based on the provided tailored lesson.
            Formatted as JSON with the quiz questions and answers without '```'.
        """)
        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent,
            output_file='quiz.json'
        )

    def create_teaching_prompts(self, agent, student_name, feedback):
        description = dedent(f"""\
            Take a deep breath and work on this step by step.
            Create a detailed teaching prompt that guides an AI agent tutor on how to effectively deliver the course material and the quiz to the student {student_name}.
            Ensure the prompts are structured and easy to follow for an LLM.
            Make sure to adapt the content and follow the given feedback to improve the learning experience: {feedback}.
        """)
        expected_output = dedent("""\
            A detailed teaching prompt explaining how to teach each section of the lesson and quiz in the best way.
            Formatted as markdown without '```'
        """)
        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent,
            output_file='teaching_prompts.md'
        )
