import subprocess
import time
from datetime import datetime, timedelta


one_hour = timedelta(minutes=60)
timeout = datetime.now().replace(microsecond=0, second=0, minute=0) + one_hour

while True:

    print("Starting bot:")
    process = subprocess.Popen(["python", "main.py"])


    print("Sleeping till: " ,timeout)
    current_time = datetime.now()
    while current_time < timeout:
        time.sleep(1)

    timeout = datetime.now().replace(microsecond=0, second=0, minute=0) + one_hour


    print("Killing bot.")
    process.kill()

    print()
    print("Pulling changes:")
    git = subprocess.Popen(["git", "pull"])
    git.wait()
    print("Finished pulling changes.")





