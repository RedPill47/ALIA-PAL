from langgraph.graph import Graph
from langgraph.node import Node

from decision_engine import DecisionEngineAgent
from monitor_agent import MonitorAgent
from profile_agent import ProfileAgent

class LearningGraph(Graph):
    def __init__(self):
        super().__init__()

        # Initialize the agents
        self.monitor_agent = MonitorAgent()
        self.decision_engine = DecisionEngineAgent()
        self.profile_agent = ProfileAgent()

        # Create nodes for each agent in the system
        monitor_node = Node(name="Monitor Node", function=self.track_progress)
        decision_node = Node(name="Decision Node", function=self.make_decision)
        profile_node = Node(name="Profile Node", function=self.update_profile)

        # Connect the nodes (define the graph structure)
        self.add_node(monitor_node)
        self.add_node(decision_node)
        self.add_node(profile_node)

        # Define how data flows between nodes
        self.connect(monitor_node, decision_node)  # Progress flows from Monitor to Decision
        self.connect(decision_node, profile_node)  # Decision results update the profile

    def track_progress(self, data):
        """
        Function for the Monitor Node to track student's progress (e.g., quiz score).
        """
        quiz_score = data.get("quiz_score", 0)
        return self.monitor_agent.track_progress(quiz_score)

    def make_decision(self, data):
        """
        Function for the Decision Node to analyze the student's performance and decide what to do.
        """
        quiz_score = data.get("quiz_score", 0)
        task_to_modify = self.decision_engine.analyze_performance(quiz_score)
        # Send notification to CrewAI if needed
        student_profile = data.get("student_profile", {})
        self.decision_engine.notify_crewai(task_to_modify, student_profile)
        return task_to_modify

    def update_profile(self, data):
        """
        Function for the Profile Node to update the student's profile based on decisions made.
        """
        student_profile = data.get("student_profile", {})
        self.profile_agent.save_student_profile(student_profile)
        return student_profile
