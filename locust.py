import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def visit_page(self):
        self.client.get(url="/")

        
    @task
    def visit_page(self):
        self.client.post("/dev", {"amount": 20000, "interest": 2.8, "maturity": 6, "operation": "simple"})
