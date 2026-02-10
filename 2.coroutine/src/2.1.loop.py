import time
import random
import asyncio
import threading

async def mimic_llm(prompt: str):
    current = threading.current_thread()
    print(f"[{prompt}] start, thread_name={current.name}, thread_id={threading.get_ident()}")

    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{prompt}]. Heartbeat tick={i}, sleep={process_duration:.2f}s")
        time.sleep(process_duration)

async def run_coroutine():
    current = threading.current_thread()
    print(f"[run_coroutine] start, thread_name={current.name}, thread_id={threading.get_ident()}")
    await mimic_llm("First coroutine.")


if __name__ == "__main__":

    # asyncio.run(mimic_llm("First coroutine."))
    asyncio.run(run_coroutine())