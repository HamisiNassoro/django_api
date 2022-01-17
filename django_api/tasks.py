from celery import app
import time

@app.shared_task()
def test():
    time.sleep(5)          #sleeps for 5 secs
    print("Hello Async")