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
    if (event.message.type != 'text' and
            re.match(r'\/wc18\s.*', event.message.text)):
        return

    reply_message = 'Mohon maaf perintah tidak dikenal'

    if event.message.text == '/wc18 help':
        reply_message = 'hola-hola'

    if event.message.text == '/wc18 today':
        todayURL = '{}{}'.format(BASE_URL, TODAY_MATCHES)
        with urllib.request.urlopen(todayURL) as url:
            reply_message = ''
            datas = json.loads(url.read().decode())
            for data in datas:
                if data['time'] == 'null':
                    time = int(data['datetime'][11:-7]) % 24
                    reply_message += str(time).center(44, ' ')
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