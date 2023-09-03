# !/usr/local/bin/python
# -*- coding:utf-8 -*-
from locust import HttpUser, TaskSet, task, between,run_single_user
'''
测试demo脚本，请替换成自己的压测脚本
'''
class NoSlowQTaskSet(HttpUser):
    host = "https://baidu.com"
    @task
    def index_page(self):
        r = self.client.get("/")

if __name__ == "__main__":
    run_single_user(NoSlowQTaskSet)