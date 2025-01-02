# my_agent/crew/crew.py
import os
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
        # 1. Retrieve parameters from state
        pdf = state.get("pdf")
        query = state.get("query", "course material")
        student_name = state.get("student_name")
        student_level = state.get("student_level")
        learning_preferences = state.get("learning_preferences")
        feedback = state.get("feedback")

        # 2. Initialize tasks
        tasks = TutorTasks()
        task_list = [
            tasks.process_file(self.file_manager, pdf, query),
            tasks.adapt_learning_path(self.tutor, student_name, student_level, learning_preferences, feedback),
            tasks.create_quiz(self.practical, student_level, learning_preferences, feedback),
            tasks.create_teaching_prompts(self.teacher_persona, student_name, feedback),
        ]

        # 3. Set up the crew (example: sequential process, verbose on)
        crew = Crew(
            agents=self.agents,
            tasks=task_list,
            process=Process.sequential,
            verbose=True,
        )

        # 4. Run the crew
        result = crew.kickoff()
        print("\n--- Crew Execution Result ---\n", result, "\n")

        # 5. Pass the crew result to the state
        # This ensures your monitor_agent_node can see the crew's final result.
        # We store it in "crew_response" (or any key you prefer).
        state["crew_response"] = f"**Crew Final Output**:\n{result}"

        # 6. Return state unmodified beyond adding crew_response
        return state