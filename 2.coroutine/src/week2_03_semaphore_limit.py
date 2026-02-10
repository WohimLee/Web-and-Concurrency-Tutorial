import asyncio
import random
import time


async def bounded_work(item: int, sem: asyncio.Semaphore, state: dict[str, int]) -> None:
    async with sem:
        state["running"] += 1
        state["peak"] = max(state["peak"], state["running"])
        await asyncio.sleep(random.uniform(0.1, 0.4))
        state["running"] -= 1
        print(f"item={item} done")


async def main() -> None:
    total = 20
    limit = 5
    sem = asyncio.Semaphore(limit)
    state = {"running": 0, "peak": 0}

    start = time.perf_counter()
    await asyncio.gather(*(bounded_work(i, sem, state) for i in range(total)))
    elapsed = time.perf_counter() - start

    print(f"limit={limit}, total={total}, elapsed={elapsed:.2f}s, peak_running={state['peak']}")


if __name__ == "__main__":
    asyncio.run(main())
