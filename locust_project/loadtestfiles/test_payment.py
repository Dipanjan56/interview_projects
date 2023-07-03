
from locust import events, HttpUser, between

from locust_project.taskset.task1 import TestPayment


@events.test_start.add_listener
def on_start(environment, **kwargs):
    print('Starting load test')

@events.test_stop.add_listener
def on_stop(environment, **kwargs):
    print('Stopping load test')


class test_apis(HttpUser):
    wait_time = between(0.2, 1)
    tasks = [TestPayment]



