
import random
import asyncio
import threading

async def mimic_llm(prompt):
    loop = asyncio.get_running_loop()
    print("loop: ", loop)
    print("loop_id:", id(loop))
    print("thread_id:", threading.get_ident())   # 这个循环所在线程
    print("task:", asyncio.current_task().get_name())

    print("Call LLM, prompt=", prompt)
    for i in range(5):
        process_duration = random.uniform(0, 1.5)
        print(f"Heartbeat tick={i}...")
        await asyncio.sleep(process_duration)

if __name__ == "__main__":

    asyncio.run(mimic_llm())
