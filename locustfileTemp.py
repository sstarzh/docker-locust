from locust import HttpLocust
from locust import TaskSet
from locust import task
import random

# For HTML reporting
from locust.web import app
from src import report
app.add_url_rule('/htmlreport', 'htmlreport', report.download_report)

randuser = random.randint(1, 100000)
randpass = random.randint(1, 100000)

h = {'Host': 'shop.f5se.com', 'User-Agent': 'wontguess'}


def login(l):
    l.client.post("/user/login", {"username":"user_{randuser}", "password":"pass_{randpass}"}, headers=h, verify=False)


def index(l):
    l.client.get("/", headers=h, verify=False)


class UserBehavior(TaskSet):
    tasks = {login: 1}

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = lambda self: random.expovariate(1)*1000
