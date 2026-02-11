import asyncio
import random
import time


async def unstable_io(job_id: int) -> str:
    delay = random.uniform(0.05, 0.4)
    await asyncio.sleep(delay)
    if random.random() < 0.3:
        raise RuntimeError(f"job {job_id} transient error")
    return f"job {job_id} ok in {delay:.2f}s"


async def call_with_retry(job_id: int, retries: int = 2, timeout: float = 0.25) -> tuple[bool, str, float]:
    start = time.perf_counter()
    for attempt in range(retries + 1):
        try:
            async with asyncio.timeout(timeout):
                result = await unstable_io(job_id)
                return True, result, time.perf_counter() - start
        except (TimeoutError, RuntimeError) as exc:
            if attempt == retries:
                return False, f"job {job_id} failed: {exc}", time.perf_counter() - start
            await asyncio.sleep(0.05 * (attempt + 1))
    return False, f"job {job_id} failed: unreachable", time.perf_counter() - start


async def main() -> None:
    random.seed(42)
    results = await asyncio.gather(*(call_with_retry(i) for i in range(1, 21)))
    ok = [r for r in results if r[0]]
    failed = [r for r in results if not r[0]]

    for _, msg, elapsed in results:
        print(f"{msg} (elapsed={elapsed:.2f}s)")

    print(f"success={len(ok)} failed={len(failed)}")


if __name__ == "__main__":
    asyncio.run(main())
