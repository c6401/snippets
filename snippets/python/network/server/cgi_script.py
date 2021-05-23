#!/usr/bin/python3
import cgitb
import json
import os
import sys
cgitb.enable()

os.environ['REQUEST_METHOD']
os.environ['CONTENT_TYPE']
os.environ['HTTP_ACCEPT']
os.environ['HTTP_COOKIE']
os.environ['HTTP_REFERER']
os.environ['PATH_INFO']
os.environ['REMOTE_ADDR']

content_length = os.environ["CONTENT_LENGTH"]
if content_length:
    body = sys.stdin.buffer.read(int(content_length)).decode('utf-8')
    data = json.loads(body)

print('Content-Type: text/text; charset=utf-8')
print('Access-Control-Allow-Origin: *')
print()
print(json.dumps({}, indent=4))
