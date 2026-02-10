import asyncio


async def producer(queue: asyncio.Queue[int], n: int) -> None:
    for i in range(n):
        await queue.put(i)
        print(f"produce {i}")
    await queue.put(-1)


async def consumer(queue: asyncio.Queue[int]) -> list[int]:
    processed: list[int] = []
    while True:
        item = await queue.get()
        try:
            if item == -1:
                await queue.put(-1)
                return processed
            await asyncio.sleep(0.1)
            processed.append(item * item)
            print(f"consume {item}")
        finally:
            queue.task_done()


async def main() -> None:
    q: asyncio.Queue[int] = asyncio.Queue(maxsize=3)
    p = asyncio.create_task(producer(q, 8))
    c1 = asyncio.create_task(consumer(q))
    c2 = asyncio.create_task(consumer(q))

    await p
    await q.join()
    r1, r2 = await asyncio.gather(c1, c2)
    all_results = sorted(r1 + r2)
    print(f"results={all_results}")


if __name__ == "__main__":
    asyncio.run(main())
