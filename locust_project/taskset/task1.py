from locust import SequentialTaskSet, task

from locust_project.common import api_request_locust


class TestPayment(SequentialTaskSet):
    headers = {}

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = {'Authorization': 'Bearer sk_test_4eC39HqLyjWDarjtT1zdp7dc'}

    @task
    def payment(self):
        endpoint = '/v1/customers'
        payload = {'description': 'My First Test Customer (created for API docs at https://www.stripe.com/docs/api)'}
        api_request_locust.post(self, endpoint, headers=self.headers, request_body=payload)

    @task
    def stop_locust(self):
        self.user.environment.runner.quit()
