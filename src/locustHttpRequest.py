from locust import HttpUser, task, constant

class MyLoadTest(HttpUser):
    #https://http.cat/  --Website for API Details
    host= "https://http.cat"
    wait_time = constant(1)
    @task
    def request1(self):
        self.client.get("/200")
    @task
    def request2(self):
        self.client.get("/300")

    @task
    def request3(self):
        self.client.get("/400")