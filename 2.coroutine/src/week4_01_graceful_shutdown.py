import asyncio


async def worker(name: str, stop_event: asyncio.Event) -> None:
    try:
        i = 0
        while not stop_event.is_set():
            print(f"{name} tick={i}")
            i += 1
            await asyncio.sleep(0.3)
    except asyncio.CancelledError:
        print(f"{name} cancelled, cleanup start")
        await asyncio.sleep(0.1)
        print(f"{name} cleanup done")
        raise


async def main() -> None:
    stop_event = asyncio.Event()
    tasks = [asyncio.create_task(worker(f"w{i}", stop_event)) for i in range(3)]

    await asyncio.sleep(1.2)
    print("request graceful shutdown")
    stop_event.set()

    await asyncio.sleep(0.4)
    for t in tasks:
        if not t.done():
            t.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)
    print("all workers stopped")


if __name__ == "__main__":
    asyncio.run(main())
