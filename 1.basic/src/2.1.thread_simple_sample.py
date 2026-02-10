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

if __name__ == "__main__":

    mimic_llm(prompt="Dummy prompt")
