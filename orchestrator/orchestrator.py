from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from agents.critic import CriticAgent
from memory.shared_state import SharedState
from logs.logger import log


class Orchestrator:

    def __init__(self):

        # Initialize agents
        self.researcher = ResearcherAgent()
        self.writer = WriterAgent()
        self.critic = CriticAgent()

    def run(self, task):

        log("[Orchestrator] Starting workflow")

        # Create shared memory
        state = SharedState(task)

        # Step 1: Research
        log("[Orchestrator] Sending task to Researcher")
        state = self.researcher.execute_task(state)

        # Step 2: Writing
        log("[Orchestrator] Sending task to Writer")
        state = self.writer.execute_task(state)

        # Step 3: Critic review
        log("[Orchestrator] Sending task to Critic")
        state = self.critic.execute_task(state)

        log("[Orchestrator] Workflow completed")

        return state.get("final_output")