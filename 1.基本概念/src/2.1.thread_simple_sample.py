import time
import random
import threading

def mimic_llm(prompt):

    print(f"{prompt}thread_id: ", threading.get_ident())   # 这个循环所在线程

    print(f"{prompt}Call LLM, prompt=", prompt)
    for i in range(5):
        process_duration = random.uniform(0, 1.5)
        print(f"{prompt} Heartbeat tick={i}...")
        time.sleep(process_duration)

if __name__ == "__main__":

    mimic_llm(prompt="Dummy prompt")
