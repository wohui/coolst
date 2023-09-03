# !/usr/local/bin/python
# -*- coding:utf-8 -*-
from locust import HttpUser, TaskSet, task, between,run_single_user

class NoSlowQTaskSet(HttpUser):
    host = "https://dragon.video2edit.com/api/csrf/login?_=1693320195870"
    @task
    def index_page(self):
        r = self.client.get("/")
        print(r.text)


if __name__ == "__main__":
    run_single_user(NoSlowQTaskSet)