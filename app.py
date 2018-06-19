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
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import flex_today_matches_builder

BASE_URL = 'https://world-cup-json.herokuapp.com/matches'
TODAY_MATCHES = '/today'
CURRENT_MATCH = '/current'
LINE_API = 'https://api.line.me/v2/bot/message/reply'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', '')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN', ''))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET', ''))


class LiveSubscribers(db.Model):
    __tablename__ = 'live_subscribers'

    id = db.Column(db.Integer, primary_key=True)
    live_id = db.Column(db.String(128), unique=True)


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
                time_str, data['home_team']['code'], data['away_team']['code']
            )
            messages.append(tmp)
        payload = {
            'replyToken': event.reply_token,
            'messages': messages
        }
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'Bearer {}'.format(
                os.getenv('LINE_CHANNEL_ACCESS_TOKEN', '')
                )}

        try:
            res = requests.post(LINE_API, json=payload, headers=headers)
        except Exception as e:
            pass

    if event.message.text == '/wc18 start live':
        try:
            live_id = event.source.group_id
        except Exception as e:
            live_id = event.source.user_id

        live = LiveSubscribers(live_id=live_id)

        try:
            db.session.add(live)
            db.session.commit()
        except Exception:
            pass

    if event.message.text == '/wc18 stop live':
        try:
            live_id = event.source.group_id
        except Exception as e:
            live_id = event.source.user_id

        try:
            db.session.query(LiveSubscribers).filter(
                LiveSubscribers.live_id == live_id).delete()
            db.session.commit()
        except Exception:
            pass


if __name__ == "__main__":
    app.run()
