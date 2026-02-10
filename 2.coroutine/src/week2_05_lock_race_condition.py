import asyncio


async def increase_without_lock(counter: dict[str, int], n: int) -> None:
    for _ in range(n):
        value = counter["v"]
        await asyncio.sleep(0)
        counter["v"] = value + 1


async def increase_with_lock(counter: dict[str, int], n: int, lock: asyncio.Lock) -> None:
    for _ in range(n):
        async with lock:
            value = counter["v"]
            await asyncio.sleep(0)
            counter["v"] = value + 1


async def run_without_lock() -> int:
    counter = {"v": 0}
    await asyncio.gather(*(increase_without_lock(counter, 1000) for _ in range(5)))
    return counter["v"]


async def run_with_lock() -> int:
    counter = {"v": 0}
    lock = asyncio.Lock()
    await asyncio.gather(*(increase_with_lock(counter, 1000, lock) for _ in range(5)))
    return counter["v"]


async def main() -> None:
    no_lock = await run_without_lock()
    with_lock = await run_with_lock()
    print(f"without lock: {no_lock}")
    print(f"with lock:    {with_lock}")


if __name__ == "__main__":
    asyncio.run(main())
