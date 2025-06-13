from locust import HttpUser, task, constant

class MyLoadTest(HttpUser):
    #https://http.cat/  --Website for API Details
    wait_time = constant(1)
    @task
    def request1(self):
        self.client.get("https://http.cat/200")
    @task
    def request2(self):
        self.client.get("https://reqres.in/api/users?page=2")
