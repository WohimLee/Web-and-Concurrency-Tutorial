import time
import random
import threading


def mimic_llm(prompt: str):
    current = threading.current_thread()
    print(f"[{prompt}] start, thread_name={current.name}, thread_id={threading.get_ident()}")

    for i in range(5):
        process_duration = random.uniform(0.2, 1.0)
        print(f"[{prompt}]. Heartbeat tick={i}, sleep={process_duration:.2f}s")
        time.sleep(process_duration)

    print(f"[{prompt}] done")


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
