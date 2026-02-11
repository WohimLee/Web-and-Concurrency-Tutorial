import time
import random
import asyncio
import threading


def print_identity(identifier):
    print()

    current = threading.current_thread()
    print(
        "[{}] start, thread_name={}, thread_id={}".format(
            identifier, current.name, threading.get_ident()
        )
    )


async def mimic_llm(prompt: str):
    
    print_identity(identifier=prompt)

    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{prompt}]. Heartbeat tick={i}, sleep={process_duration:.2f}s")
        await asyncio.sleep(process_duration)



if __name__ == "__main__":

    asyncio.run(mimic_llm("First coroutine."))
