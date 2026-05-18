import asyncio


async def maybe_slow_work(delay: float) -> str:
    try:
        await asyncio.sleep(delay)
        return f"done in {delay:.2f}s"
    except asyncio.CancelledError:
        print(f"work({delay:.2f}) cancelled, releasing resources")
        raise


async def run_with_timeout(delay: float, timeout: float) -> str:
    try:
        async with asyncio.timeout(timeout):
            return await maybe_slow_work(delay)
    except TimeoutError:
        return f"timeout: delay={delay:.2f}, timeout={timeout:.2f}"


async def manual_cancel_demo() -> None:
    task = asyncio.create_task(maybe_slow_work(2.0))
    await asyncio.sleep(0.5)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("manual cancel completed")


async def main() -> None:
    print(await run_with_timeout(0.3, 1.0))
    print(await run_with_timeout(1.2, 0.5))
    await manual_cancel_demo()


if __name__ == "__main__":
    asyncio.run(main())
