from agents.base_agent import BaseAgent
from logs.logger import log


class CriticAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Critic",
            role="Responsible for reviewing and improving the draft."
        )

    def execute_task(self, state):

        draft = state.get("draft")

        log(f"[{self.name}] Reviewing draft.")

        final_output = f"""
        Final Improved Blog Post:

        {draft}

        Conclusion:
        Multi-agent AI systems represent a powerful paradigm where collaboration between specialized agents leads to more efficient and scalable solutions.
        """

        state.update("final_output", final_output)

        log(f"[{self.name}] Review completed. Final output ready.")

        return state