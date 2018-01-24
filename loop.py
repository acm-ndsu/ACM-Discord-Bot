import subprocess
import time
from datetime import datetime, timedelta


one_hour = timedelta(minutes=60)

while True:

    print("Starting bot:")
    process = subprocess.Popen(["python", "main.py"])


    timeout = datetime.now().replace(microsecond=0, second=0, minute=0) + one_hour
    current_time = datetime.now()

    print("Sleeping till: " ,timeout)
    while current_time < timeout:
        time.sleep(1)
        current_time = datetime.now()



    print("Killing bot.")
    process.kill()

    print()
    print("Pulling changes:")
    git = subprocess.Popen(["git", "pull"])
    git.wait()
    print("Finished pulling changes.")





