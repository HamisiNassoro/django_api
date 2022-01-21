from celery import app
# from celery import task
import time
import requests
from event_controller.models import Dog

@app.shared_task()
def test(value):
    time.sleep(5)          #sleeps for 5 secs
    print(value)

@app.shared_task()
def populate_dog():
    url = 'https://dog.ceo/api/breeds/image/random'

    try:
        res = requests.get(url)
    except requests.ConnectionError as e:
        raise Exception("Failed Operation", e)

    if res.status_code in [200, 201]:
        #create dog entry
        # print(res.json())
        data = res.json()
        image_url = data.get("message", "")
        Dog.objects.create(url=image_url)