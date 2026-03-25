class SharedState:
    def __init__(self, task):
        self.state = {
            "task": task,
            "research": "",
            "draft": "",
            "final_output": ""
        }

    def update(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state.get(key)

    def get_all(self):
        return self.state