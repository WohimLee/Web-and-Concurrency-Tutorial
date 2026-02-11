import asyncio
import time


def blocking_io(delay: float) -> float:
    time.sleep(delay)
    return delay


async def run_sync_style(n: int, delay: float) -> float:
    start = time.perf_counter()
    for _ in range(n):
        blocking_io(delay)
    return time.perf_counter() - start


async def run_async_style(n: int, delay: float) -> float:
    start = time.perf_counter()
    tasks = [asyncio.to_thread(blocking_io, delay) for _ in range(n)]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start


async def main() -> None:
    n = 20
    delay = 0.1
    t_sync = await run_sync_style(n, delay)
    t_async = await run_async_style(n, delay)
    print(f"sync style elapsed:  {t_sync:.2f}s")
    print(f"async style elapsed: {t_async:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
