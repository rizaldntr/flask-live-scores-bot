import os
import re
import requests
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

from utils import flex_today_matches_builder

BASE_URL = 'https://world-cup-json.herokuapp.com/matches'
TODAY_MATCHES = '/today'
CURRENT_MATCH = '/current'
LINE_API='https://api.line.me/v2/bot/message/reply'

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

    if event.message.text == '/wc18 help':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Halo'))

    if event.message.text == '/wc18 today':
        todayURL = '{}{}'.format(BASE_URL, TODAY_MATCHES)
        res = requests.get(todayURL)
        datas = json.loads(res.content)
        messages = []            
        for data in datas:
            if data['time'] is None:
                time = (int(data['datetime'][11:-7]) + 7) % 24
                time_str = '{}:00'.format(time)
            else:
                time_str = 'Time: {}\''.format(data['time'])
            tmp = flex_today_matches_builder(
                data['home_team']['country'], data['away_team']['country'],
                data['home_team']['goals'], data['away_team']['goals'],
                time_str
            )
            messages.append(tmp)
        payload = {
            'to': event.reply_token,
            'messages': messages
            }
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'Bearer {}'.format(line_bot_api)}
        res = requests.post(LINE_API, data=payload, headers=headers)

if __name__ == "__main__":
    app.run()
