import requests

requests.post(
    "https://unhaggle-chat.slack.com/api/chat.postMessage",
    data={
        'channel': ...,
        'text': ...,
        'token': ...,
    },
).text
