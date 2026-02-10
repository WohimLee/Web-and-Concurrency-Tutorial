import asyncio


async def service_task(name: str, fail_at: int | None = None) -> None:
    for i in range(10):
        await asyncio.sleep(0.2)
        print(f"{name} tick={i}")
        if fail_at is not None and i == fail_at:
            raise RuntimeError(f"{name} failed at tick={i}")


async def main() -> None:
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(service_task("fetch"))
            tg.create_task(service_task("process", fail_at=3))
            tg.create_task(service_task("report"))
    except* RuntimeError as eg:
        for exc in eg.exceptions:
            print(f"TaskGroup caught: {exc}")

    print("service shutdown complete")


if __name__ == "__main__":
    asyncio.run(main())
