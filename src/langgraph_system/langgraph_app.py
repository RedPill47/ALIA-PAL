# src/langgraph_system/langgraph_app.py

from langgraph import LangGraph
from .nodes import (
    StudentProfileNode,
    MonitorNode,
    DecisionEngineNode,
    TeacherProfileNode,
    EducationalCrewAINode
)
from .edges import (
    EdgeFetchStudentProfile,
    EdgeUpdateStudentProfile,
    EdgeMonitorToDecision,
    EdgeDecisionToCrewAI,
    EdgeDecisionToMonitor
)
from tutor_ai_crew.crew import TutorAiCrewCrew

class LangGraphApp:
    def __init__(self):
        # Initialize nodes
        self.student_profile_node = StudentProfileNode(config={'name': 'Student Profile Node'})
        self.monitor_node = MonitorNode(config={'name': 'Monitor Node'})
        self.decision_engine_node = DecisionEngineNode(config={'name': 'Decision Engine Node'})
        self.teacher_profile_node = TeacherProfileNode(config={'name': 'Teacher Profile Node'})
        self.educational_crewai_node = EducationalCrewAINode(
            config={'name': 'Educational CrewAI Node'},
            crew_ai=TutorAiCrewCrew()
        )

        # Initialize edges
        self.edges = [
            EdgeFetchStudentProfile(self.monitor_node, self.student_profile_node),
            EdgeMonitorToDecision(self.monitor_node, self.decision_engine_node),
            EdgeDecisionToCrewAI(
                self.decision_engine_node,
                self.educational_crewai_node,
                condition=lambda data: data.get('adjustment_needed') == True
            ),
            EdgeDecisionToMonitor(
                self.decision_engine_node,
                self.monitor_node,
                condition=lambda data: data.get('adjustment_needed') == False
            )
        ]

        # Build the graph
        self.graph = LangGraph()
        self.graph.add_node(self.student_profile_node)
        self.graph.add_node(self.monitor_node)
        self.graph.add_node(self.decision_engine_node)
        self.graph.add_node(self.educational_crewai_node)
        self.graph.add_edges(self.edges)

    def run(self, student_id):
        # Start the process by simulating student interaction
        data = {'student_id': student_id}

        # Fetch student profile
        data = self.monitor_node.send(data, self.student_profile_node)
        data = self.student_profile_node.process(data)

        # Monitor collects student activity
        data = self.monitor_node.process(data)

        # Update student profile with new activity
        update_data = {
            'student_id': student_id,
            'action': 'update',
            'updated_profile': data.get('student_activity')
        }
        self.monitor_node.send(update_data, self.student_profile_node)
        self.student_profile_node.process(update_data)

        # Decision Engine makes a decision
        data = self.monitor_node.send(data, self.decision_engine_node)
        decision_data = self.decision_engine_node.process(data)

        # Conditional routing based on decision
        if decision_data.get('adjustment_needed'):
            # Proceed to Educational CrewAI Node
            self.decision_engine_node.send(decision_data, self.educational_crewai_node)
            self.educational_crewai_node.process(decision_data)
        else:
            # Return to Monitor Node
            self.decision_engine_node.send(decision_data, self.monitor_node)
            # Continue monitoring
            self.monitor_node.process(decision_data)
