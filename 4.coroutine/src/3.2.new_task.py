import time
import random
import asyncio


from utils import print_identity, heartbeat

async def mimic_llm(prompt: str):
    print_identity(identifier=prompt)
    heartbeat(identifier=prompt)

async def main():
    
    print_identity(identifier="main")
    task = asyncio.create_task(mimic_llm("First coroutine."))
    await task


if __name__ == "__main__":

    asyncio.run(main())