import json
import requests

def slack_remind(text, token):
    return requests.post(
        "https://unhaggle-chat.slack.com/api/chat.command",
        data={
            'channel': 'D79BE1MA8', 'command': '/remind',
            'blocks': json.dumps(
                [{"type": "rich_text", "elements": [{"type":
                "rich_text_section", "elements": [{"type": "user", "user_id":
                "U78L2A0C8"}, {"type": "text", "text": text}]}]}]
            ),
            'token': token,
        }
    ).json()
