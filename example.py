from orchestrator.orchestrator import Orchestrator


def main():

    task = "Write a short blog about benefits of artificial intelligence"

    orchestrator = Orchestrator()

    result = orchestrator.run(task)

    print("\n================ FINAL OUTPUT ================\n")
    print(result)


if __name__ == "__main__":
    main()