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
    await mimic_llm("First coroutine.")


if __name__ == "__main__":

    asyncio.run(main())