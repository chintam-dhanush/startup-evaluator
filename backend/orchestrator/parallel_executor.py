from concurrent.futures import ThreadPoolExecutor

from orchestrator.agent_registry import AGENTS


def execute_parallel(startup_data):

    report = {}

    with ThreadPoolExecutor(max_workers=len(AGENTS)) as executor:

        futures = {}

        for name, agent in AGENTS:

            future = executor.submit(agent, startup_data)

            futures[future] = name

        for future, name in futures.items():
            try:
                report[name] = future.result()
            except Exception as e:
                report[name] = {
                    "error": str(e)
                }

    return report