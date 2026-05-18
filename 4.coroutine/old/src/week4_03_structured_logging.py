import asyncio
import logging
import random


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger("asyncio-course")


async def do_work(job_id: int) -> None:
    logger.info("job_start job_id=%s", job_id)
    await asyncio.sleep(random.uniform(0.1, 0.4))
    if random.random() < 0.2:
        logger.warning("job_retry job_id=%s reason=transient", job_id)
        await asyncio.sleep(0.1)
    logger.info("job_done job_id=%s", job_id)


async def main() -> None:
    random.seed(3)
    await asyncio.gather(*(do_work(i) for i in range(1, 8)))


if __name__ == "__main__":
    asyncio.run(main())
