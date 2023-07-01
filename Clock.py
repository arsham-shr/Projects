import datetime
import time

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time, end="\r", flush=True)
    time.sleep(1)
