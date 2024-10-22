# src/langgraph_system/edges.py

from langgraph import Edge

class EdgeFetchStudentProfile(Edge):
    def __init__(self, from_node, to_node, condition=None):
        super().__init__(from_node, to_node, condition)

    def transfer(self, data):
        data.update({'action': 'fetch'})
        return data

class EdgeUpdateStudentProfile(Edge):
    def __init__(self, from_node, to_node, condition=None):
        super().__init__(from_node, to_node, condition)

    def transfer(self, data):
        data.update({'action': 'update'})
        return data

class EdgeMonitorToDecision(Edge):
    def __init__(self, from_node, to_node, condition=None):
        super().__init__(from_node, to_node, condition)

    def transfer(self, data):
        # Pass student activity data
        return data

class EdgeDecisionToCrewAI(Edge):
    def __init__(self, from_node, to_node, condition):
        super().__init__(from_node, to_node, condition)

    def transfer(self, data):
        return data

class EdgeDecisionToMonitor(Edge):
    def __init__(self, from_node, to_node, condition):
        super().__init__(from_node, to_node, condition)

    def transfer(self, data):
        return data
