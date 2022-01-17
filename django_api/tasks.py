from celery import task

@task()
def test():
    print("Hello Async")