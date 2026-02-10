import time
import random
import asyncio


async def mimic_llm(task_id: str) -> str:
    
    print(f"Task: {task_id} start.")

    print("Calling LLM...")
    process_duration = random.uniform(2, 5)
    await asyncio.sleep(process_duration)

    print(f"Task: {task_id} done.")
    return f"dummy llm results for {task_id}"


async def single_task() -> None:
    start = time.perf_counter()
    task_id = "task-888"
    result  = await mimic_llm(task_id=task_id)
    elapsed = time.perf_counter() - start

    print(f"Task: {task_id}. Result: {result}. Elapsed={elapsed:.2f}s")


async def multi_tasks() -> None:
    start = time.perf_counter()
    tasks = [asyncio.create_task(mimic_llm(f"task-{i}")) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start

    print(f"Results: {results}. Elapsed={elapsed:.2f}s")


if __name__ == "__main__":
    # asyncio.run(single_task())
    asyncio.run(multi_tasks())
