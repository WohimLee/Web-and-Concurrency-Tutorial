# parent_child.py
import os, subprocess, sys

'''
subprocess
'''

print("parent PID:", os.getpid())
subprocess.run([sys.executable, "-c", "import os; print('child PID:', os.getpid())"])