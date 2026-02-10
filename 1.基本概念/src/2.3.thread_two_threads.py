import time
import random
import threading


def mimic_llm(prompt):

    print(f"{prompt}, thread_id:", threading.get_ident())   # 这个循环所在线程

    print(f"{prompt}, Call LLM, prompt =", prompt)
    for i in range(5):
        process_duration = random.uniform(0, 1.5)
        print(f"{prompt} Heartbeat tick={i}...")
        time.sleep(process_duration)


def run_loops():
    
    # loop-A 
    t1 = threading.Thread(target=mimic_llm, args=("This is loop-A",), name="loop-a-thread")
    # loop-B 跑在子线程
    t2 = threading.Thread(target=mimic_llm, args=("This is loop-B",), name="loop-b-thread")
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__ == "__main__":
    run_loops()
