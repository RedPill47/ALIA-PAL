from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFSearchTool

from langchain_openai import ChatOpenAI

@CrewBase
class TutorAiCrewCrew():
	"""TutorAiCrew crew"""

	@agent
	def file_manager(self) -> Agent:
		return Agent(
		config=self.agents_config['file_manager'],
		verbose=True,
		tools=[PDFSearchTool()]
		)

	@agent
	def tutor(self) -> Agent:
		return Agent(
		config=self.agents_config['tutor'],
		verbose=True,
		)

	@agent
	def practical(self) -> Agent:
		return Agent(
		config=self.agents_config['practical'],
		verbose=True,
		)
	
	@agent
	def teacher_persona(self) -> Agent:
		return Agent(
		config=self.agents_config['teacher_persona'],
		verbose=True,
		)

	@task
	def process_file(self) -> Task:
		return Task(
		config=self.tasks_config['process_file'],
		)

	@task
	def adapt_learning_path(self) -> Task:
		return Task(
		config=self.tasks_config['adapt_learning_path'],
		output_file='output/lesson.md',
		)
	
	@task
	def create_quiz(self) -> Task:
		return Task(
		config=self.tasks_config['create_quiz'],
		output_file='output/quiz.json',
		)
	
	@task
	def create_teaching_prompts(self) -> Task:
		return Task(
		config=self.tasks_config['create_teaching_prompts'],
		output_file='output/teaching_prompts.md',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TutorAiCrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.hierarchical,
			memory=True,
			verbose=True,
			manager_llm=ChatOpenAI(model="gpt-4o")
		)
