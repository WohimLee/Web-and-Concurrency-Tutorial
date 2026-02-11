import asyncio
import math
import time


def cpu_heavy(n: int) -> int:
    count = 0
    for x in range(2, n):
        is_prime = True
        limit = int(math.sqrt(x)) + 1
        for d in range(2, limit):
            if x % d == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count


async def heartbeat(label: str, seconds: float = 1.2) -> None:
    start = time.perf_counter()
    while time.perf_counter() - start < seconds:
        print(f"[{label}] heartbeat")
        await asyncio.sleep(0.2)


async def blocking_case() -> None:
    print("\n=== blocking case ===")
    hb = asyncio.create_task(heartbeat("blocking"))
    cpu_heavy(70_000)
    await hb


async def executor_case() -> None:
    print("\n=== executor case ===")
    hb = asyncio.create_task(heartbeat("executor"))
    await asyncio.to_thread(cpu_heavy, 70_000)
    await hb


async def main() -> None:
    await blocking_case()
    await executor_case()


if __name__ == "__main__":
    asyncio.run(main())
