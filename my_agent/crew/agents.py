# my_agent/crew/agents.py

from crewai import Agent
from textwrap import dedent

'''
import os
import requests

# Specify the folder path where you want to save the file
folder_path = 'dataset'

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Sample .pdf data from Arxiv
pdf_url = 'https://arxiv.org/pdf/1706.03762.pdf' # @param {type:"string"}
response = requests.get(pdf_url)

# Extract the filename from the URL
filename = os.path.basename(pdf_url)

# Specify the file path including the folder and the extracted filename
pdf_file_path = os.path.join(folder_path, filename)

with open(pdf_file_path, 'wb') as file:
    file.write(response.content)

print(f"PDF file downloaded and saved to: {pdf_file_path}")


from crewai_tools import PDFSearchTool

pdf_search_tool = PDFSearchTool(pdf=pdf_file_path)
'''

class TutorAgents:
    def file_manager(self):
        return Agent(
            role='File Manager',
            goal=dedent("""\
                Prepare course materials by extracting relevant sections, ensuring they are ready for further processing by the Tutor Agent.
            """),
            backstory=dedent("""\
                I process course materials provided by the teacher, extract relevant content, and prepare them for further use by other agents.
            """),
            #tools=[pdf_search_tool],
            verbose=True
        )

    def tutor(self):
        return Agent(
            role='Learning Path Tutor',
            goal=dedent("""\
                Create personalized courses that adapt to students' learning styles and preferences.
            """),
            backstory=dedent("""\
                I'm a professor and personal tutor, designed to construct and adapt learning paths tailored to students' evolving needs.
            """),
            verbose=True
        )

    def practical(self):
        return Agent(
            role='Practical Tutor',
            goal=dedent("""\
                Create interactive quizzes that reinforce the theoretical knowledge of the course.
            """),
            backstory=dedent("""\
                I'm a professor and tutor that focuses on applying theoretical knowledge through interactive quizzes.
            """),
            verbose=True
        )

    def teacher_persona(self):
        return Agent(
            role='Teacher Prompt Persona',
            goal=dedent("""\
                Create detailed teaching prompts that guide tutors on how to effectively deliver course materials to students.
            """),
            backstory=dedent("""\
                I'm an experienced educator responsible for translating course material and quizzes into structured teaching prompts for tutors.
            """),
            verbose=True
        )
