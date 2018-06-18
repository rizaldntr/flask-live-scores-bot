import os
import re
import urllib.request
import json
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

BASE_URL = 'https://world-cup-json.herokuapp.com/matches'
TODAY_MATCHES = '/today'
CURRENT_MATCH = '/current'

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN', ''))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET', ''))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if (event.message.type != 'text' or
            re.match(r'\/wc18\s.*', event.message.text) is None):
        return

    reply_message = 'Mohon maaf perintah tidak dikenal'

    if event.message.text == '/wc18 help':
        reply_message = 'hola-hola'

    if event.message.text == '/wc18 dev':
        reply_message = [{
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/02_1_news_thumbnail_1.png"
                    },
                    {
                        "type": "text",
                        "text": "1 - 2",
                        "gravity": "center",
                        "align": "center",
                        "size": "xxl"
                    },
                    {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/02_1_news_thumbnail_1.png"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Korea Republic",
                        "gravity": "center",
                        "align": "center",
                        "size": "sm",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": "Time: 75'",
                        "gravity": "center",
                        "align": "center",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "Mexico",
                        "gravity": "center",
                        "align": "center",
                        "size": "sm",
                        "wrap": True
                    }
                    ]
                },
                {
                    "type": "separator",
                    "margin": "lg"
                }]
            }
        }]

    if event.message.text == '/wc18 today':
        todayURL = '{}{}'.format(BASE_URL, TODAY_MATCHES)
        with urllib.request.urlopen(todayURL) as url:
            reply_message = ''
            datas = json.loads(url.read().decode())
            for data in datas:
                if data['time'] == None:
                    time = (int(data['datetime'][11:-7]) + 7) % 24
                    tmp = '{}:00'.format(time)
                    tmp = tmp.center(44, ' ') + '\n'
                    reply_message += tmp
                else:
                    reply_message += data['time'].center(44, ' ') + '\n'
                tmp = '{} {} - {} {}'.format(
                    data['home_team']['country'], data['home_team']['goals'],
                    data['away_team']['country'], data['away_team']['goals']
                )
                reply_message += tmp.center(44, ' ') + '\n\n'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message))


if __name__ == "__main__":
    app.run()
