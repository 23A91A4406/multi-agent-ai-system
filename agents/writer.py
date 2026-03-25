from agents.base_agent import BaseAgent
from logs.logger import log


class WriterAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Writer",
            role="Responsible for writing content using research provided."
        )

    def execute_task(self, state):

        research = state.get("research")

        log(f"[{self.name}] Writing draft using research.")

        draft = f"""
        Blog Draft:

        {research}

        Multi-agent AI systems are an emerging approach in artificial intelligence where multiple specialized agents collaborate to solve complex problems. 
        This approach enables better scalability, modular design, and improved decision-making capabilities.
        """

        state.update("draft", draft)

        log(f"[{self.name}] Draft writing completed.")

        return state