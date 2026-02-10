import asyncio


async def long_job() -> None:
    try:
        for i in range(10):
            print(f"long_job tick={i}")
            await asyncio.sleep(0.3)
    except asyncio.CancelledError:
        print("long_job cancelled, cleaning up...")
        await asyncio.sleep(0.1)
        print("long_job cleanup done")
        raise


async def main() -> None:
    task = asyncio.create_task(long_job(), name="long_job")
    print(f"task created: done={task.done()}")

    await asyncio.sleep(0.8)
    print("request cancel")
    task.cancel()
    print(f"after cancel(): done={task.done()}")

    try:
        await task
    except asyncio.CancelledError:
        print("main received CancelledError")

    print(f"task final: done={task.done()} cancelled={task.cancelled()}")


if __name__ == "__main__":
    asyncio.run(main())
