#!/usr/bin/python3
import asyncio
import cgitb
import os
import sys
cgitb.enable()

async def main():
    path = os.environ['PATH_INFO'][1:]

    if os.environ['REQUEST_METHOD'] == 'GET':
        print('Content-Type: text/text; charset=utf-8')
        print('Access-Control-Allow-Origin: *')
        print()
        print(...)

    elif os.environ['REQUEST_METHOD'] == 'POST':
        content_length = os.environ["CONTENT_LENGTH"]
        if content_length:
            data = sys.stdin.buffer.read(int(content_length)).decode('utf-8')

        print('Content-Type: text/text; charset=utf-8')
        print('Access-Control-Allow-Origin: *')
        print()
        print('ok')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
