import asyncio
import pathlib
import sys

import pytest


ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from week2_02_timeout_and_cancel import maybe_slow_work, run_with_timeout  # noqa: E402


@pytest.mark.asyncio
async def test_timeout_happens() -> None:
    result = await run_with_timeout(delay=0.5, timeout=0.1)
    assert "timeout" in result


@pytest.mark.asyncio
async def test_cancelled_task_raises() -> None:
    task = asyncio.create_task(maybe_slow_work(1.0))
    await asyncio.sleep(0)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
