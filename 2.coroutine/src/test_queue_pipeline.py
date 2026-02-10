import asyncio

import pytest


async def square_worker(queue: asyncio.Queue[int], out: list[int]) -> None:
    while True:
        item = await queue.get()
        try:
            if item == -1:
                return
            out.append(item * item)
        finally:
            queue.task_done()


@pytest.mark.asyncio
async def test_pipeline_squares_all_items() -> None:
    queue: asyncio.Queue[int] = asyncio.Queue()
    out: list[int] = []

    workers = [asyncio.create_task(square_worker(queue, out)) for _ in range(2)]

    for i in range(6):
        await queue.put(i)
    for _ in workers:
        await queue.put(-1)

    await queue.join()
    await asyncio.gather(*workers)

    assert sorted(out) == [0, 1, 4, 9, 16, 25]
