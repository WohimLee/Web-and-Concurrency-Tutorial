import asyncio
import time


async def heartbeat(tag: str, duration: float = 1.2) -> None:
    end = time.perf_counter() + duration
    while time.perf_counter() < end:
        print(f"[{tag}] heartbeat")
        await asyncio.sleep(0.2)


async def busy_no_await(seconds: float = 1.2) -> None:
    print("[no_await] busy work start")
    end = time.perf_counter() + seconds
    while time.perf_counter() < end:
        _ = 1 + 1
    print("[no_await] busy work end")


async def busy_with_await(seconds: float = 1.2) -> None:
    print("[with_await] busy work start")
    end = time.perf_counter() + seconds
    i = 0
    while time.perf_counter() < end:
        i += 1
        if i % 20_000 == 0:
            await asyncio.sleep(0)
    print("[with_await] busy work end")


async def run_no_await_case() -> None:
    print("\n=== case: busy_no_await ===")
    await asyncio.gather(heartbeat("no_await"), busy_no_await())


async def run_with_await_case() -> None:
    print("\n=== case: busy_with_await ===")
    await asyncio.gather(heartbeat("with_await"), busy_with_await())


async def main() -> None:
    await run_no_await_case()
    await run_with_await_case()


if __name__ == "__main__":
    asyncio.run(main())
