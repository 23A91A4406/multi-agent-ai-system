from agents.base_agent import BaseAgent
from logs.logger import log


class ResearcherAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Researcher",
            role="Responsible for researching the given topic and gathering useful information."
        )

    def execute_task(self, state):

        task = state.get("task")

        log(f"[{self.name}] Starting research on: {task}")

        research_content = f"""
        Research Summary about {task}:

        - Multi-agent systems involve multiple AI agents working together.
        - Each agent has a specialized role.
        - Collaboration between agents improves problem solving.
        - Systems are modular and scalable.
        """

        state.update("research", research_content)

        log(f"[{self.name}] Research completed.")

        return state