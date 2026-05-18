import time
import random
import asyncio
import threading

from utils import print_identity, heartbeat

async def mimic_llm(prompt: str):
    
    print_identity(identifier=prompt)

    heartbeat(identifier=prompt)


async def main():

    print_identity(identifier="run_coroutine")
    # 同步
    await mimic_llm("coroutine-1")
    await mimic_llm("coroutine-2")
    await mimic_llm("coroutine-3")



if __name__ == "__main__":

    asyncio.run(main())