"""
请求中间件
"""
from flask import request, session

def auth():
    print("请求中间件")
    print(request.path)
