import random
import asyncio
import threading


async def mimic_llm(prompt):
    loop = asyncio.get_running_loop()
    print(f"{prompt}, loop: {loop}")
    print(f"{prompt}, loop_id: {id(loop)}")
    print(f"{prompt}, thread_id:{threading.get_ident()}")   # 这个循环所在线程
    print(f"{prompt}, task:", asyncio.current_task().get_name())

    print("Call LLM, prompt =", prompt)
    for i in range(5):
        process_duration = random.uniform(1, 1.5)
        print(f"{prompt}. Heartbeat tick={i}...")
        await asyncio.sleep(process_duration)

def run_loop_in_thread(prompt) -> None:
    # 新线程里要显式创建并设置事件循环
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(mimic_llm(prompt=prompt))
    finally:
        loop.close()
        asyncio.set_event_loop(None)


def run_loops():
    
    # loop-A 跑在主线程
    asyncio.run(mimic_llm("This is loop-A")) # 阻塞调用

    # loop-B 跑在子线程
    t = threading.Thread(target=run_loop_in_thread, args=("This is loop-B",), name="loop-b-thread")
    t.start()
    t.join()


if __name__ == "__main__":
    run_loops()
