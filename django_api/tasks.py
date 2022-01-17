from celery import app

@app.shared_task()
def test():
    print("Hello Async")