import requests

requests.post(
    "https://....slack.com/api/chat.postMessage",
    data={
        'channel': ...,
        'text': ...,
        'token': ...,
    },
).text
