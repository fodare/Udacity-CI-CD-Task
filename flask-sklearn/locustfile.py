from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        base_url = "https://testudacityapp.azurewebsites.net/"
        self.client.get(f"{base_url}")
