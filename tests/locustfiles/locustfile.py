import random

from locust import HttpUser, task, between, constant, constant_pacing, tag


class SampleWebUser(HttpUser):

    wait_time = between(.3, .8)  # the wait time between running each tasks
    # wait_time = constant(.3)
    # wait_time = constant_pacing(1)  # running the task and waiting time of it must last 1 second

    weight = 2

    def on_start(self):
        print('start')

    @task(2)
    def get_stats(self):
        self.client.get('/api/stats/')

    @tag('order')
    @task(3)
    def get_delay(self):
        self.client.get('/api/delay/')

    @tag('order')
    @task
    def create_order(self):
        data = {
            'order_id': random.randint(1, 100),
            'user_id': random.randint(1, 100),
            'product_id': random.randint(1, 100),
            'discount_id': random.randint(1, 100),
        }
        self.client.post('/api/order/create/', json=data)

    @task
    def orders_list(self):
        self.client.get('/api/order/list/')

    def on_stop(self):
        print('end')