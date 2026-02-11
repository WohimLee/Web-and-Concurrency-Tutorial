import asyncio
import random
import time


async def producer(queue: asyncio.Queue[int], total: int) -> None:
    for i in range(total):
        await queue.put(i)
    for _ in range(3):
        await queue.put(-1)


async def worker(name: str, queue: asyncio.Queue[int], out: list[float]) -> None:
    while True:
        item = await queue.get()
        try:
            if item == -1:
                return
            cost = random.uniform(0.03, 0.15)
            await asyncio.sleep(cost)
            out.append(cost)
            print(f"{name} handled {item}")
        finally:
            queue.task_done()


async def main() -> None:
    random.seed(7)
    total = 50
    queue: asyncio.Queue[int] = asyncio.Queue(maxsize=8)
    costs: list[float] = []

    start = time.perf_counter()
    p = asyncio.create_task(producer(queue, total))
    workers = [asyncio.create_task(worker(f"worker-{i}", queue, costs)) for i in range(3)]

    await p
    await queue.join()
    await asyncio.gather(*workers)

    elapsed = time.perf_counter() - start
    avg = (sum(costs) / len(costs)) if costs else 0.0
    print(f"processed={len(costs)} avg_cost={avg:.3f}s elapsed={elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
