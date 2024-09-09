import time

from locust import HttpUser, task, between

class DoPerformance(HttpUser):
    wait_time = between (1, 5)

    def on_start(self) -> None:
        self.client.post("/login", json={"username":"foo", "password":"bar"})


    @task
    def google(self):
        self.client.get('/sada')
        time.sleep(1)

    @task(3)
    def google(self):
        self.client.get('/asdsa')