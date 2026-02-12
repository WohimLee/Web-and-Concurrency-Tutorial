import time
import random
import asyncio


from utils import print_identity


async def mimic_llm(prompt: str):
    print_identity(identifier=prompt)
    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{prompt}]. Heartbeat tick={i}, sleep={process_duration:.2f}s")
        time.sleep(process_duration)

async def main():
    
    print_identity(identifier="main")
    await mimic_llm("First coroutine.")


if __name__ == "__main__":

    asyncio.run(main())