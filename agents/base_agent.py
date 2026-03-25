class BaseAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def execute_task(self, state):
        raise NotImplementedError("Agents must implement execute_task method")