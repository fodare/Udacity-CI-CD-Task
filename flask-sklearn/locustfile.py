from locust import HttpUser, task
import requests


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        base_url = "https://udacitytestmlappservice.azurewebsites.net"
        self.client.get(f"{base_url}")

    @task
    def predict(self):
        base_url = "https://udacitytestmlappservice.azurewebsites.net:443/predict"
        self.client.post(f"{base_url}", json={
            "CHAS": {
                "0": 0
            },
            "RM": {
                "0": 6.575
            },
            "TAX": {
                "0": 296.0
            },
            "PTRATIO": {
                "0": 15.3
            },
            "B": {
                "0": 396.9
            },
            "LSTAT": {
                "0": 4.98
            }
        })
