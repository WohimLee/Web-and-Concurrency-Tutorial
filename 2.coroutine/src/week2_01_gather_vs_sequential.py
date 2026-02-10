import asyncio
import time


async def fake_io(name: str, delay: float = 0.4) -> str:
    await asyncio.sleep(delay)
    return name


async def run_sequential(n: int) -> float:
    start = time.perf_counter()
    for i in range(n):
        await fake_io(f"task-{i}")
    return time.perf_counter() - start


async def run_gather(n: int) -> float:
    start = time.perf_counter()
    tasks = [fake_io(f"task-{i}") for i in range(n)]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start


async def main() -> None:
    n = 10
    t1 = await run_sequential(n)
    t2 = await run_gather(n)
    print(f"sequential: {t1:.2f}s")
    print(f"gather:     {t2:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
