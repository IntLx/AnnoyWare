import subprocess
import time
import os

def run_notepad():
    for _ in range(100):
        subprocess.Popen('notepad.exe')
        time.sleep(0.1)

# Run Notepad 10 times
run_notepad()

# Restart the PC
os.system("shutdown /r /t 0")
