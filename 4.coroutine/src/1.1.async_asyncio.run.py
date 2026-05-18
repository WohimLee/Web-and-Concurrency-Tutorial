import random
import asyncio

from utils import print_identity, heartbeat

async def mimic_llm(prompt: str):
    
    print_identity(identifier=prompt)

    heartbeat(identifier="prompt")



if __name__ == "__main__":

    asyncio.run(mimic_llm("First coroutine."))
