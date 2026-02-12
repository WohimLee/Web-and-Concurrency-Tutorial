import time
import random
import asyncio
import threading

from utils import print_identity

async def mimic_llm(prompt: str):
    
    print_identity(identifier=prompt)

    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{prompt}]. Heartbeat tick={i}, sleep={process_duration:.2f}s")
        await asyncio.sleep(process_duration)

def main():
    asyncio.run(mimic_llm("First coroutine."))


if __name__ == "__main__":
    main()
    
