import os
import secret
from flask import Flask,request,abort
from linebot import WebhookHandler,LineBotApi
from linebot.models import MessageEvent,TextMessage,TextSendMessage
from linebot.exceptions import InvalidSignatureError
import random
import time

planet =list([
    "月亮",
    "太陽",  
    "水星",  
    "金星",  
    "火星",  
    "木星",  
    "土星",  
    "天王星",  
    "海王星",  
    "冥王星",  
    "星球"])
starSign =list([
    '牡羊座',
    '金牛座',
    '雙子座',
    '巨蟹座',
    '獅子座',
    '處女座',
    '天秤座',
    '天蠍座',
    '射手座',
    '摩羯座',
    '水瓶座',
    '雙魚座',
    '星座'
])
errorMessage=list([
    "臭臭寶寶",
    "亂輸入",
    "打屁屁",
    "臭寶寶",
    "哼"
    ,"寶寶你要聽話餒"
    ,"摸摸頭"])

# 效率不好
# from google.cloud import secretmanager
# client=secretmanager.SecretManagerServiceClient()
# response=client.access_secret_version("projects/263333602709/secrets/CHANNEL_ACCESS_TOKEN")
# CHANNEL_ACCESS_TOKEN=response.payload.data.decode("UTF-8")
# response=client.access_secret_version("projects/263333602709/secrets/CHANNEL_SECRET")
# CHANNEL_SECRET=response.payload.data.decode("UTF-8")

app = Flask(__name__)
line_bot_api = LineBotApi(secret.CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(secret.CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent,message=TextMessage)
def handler_text_message(event):
    message = event.message.text
    random.seed(time.time())
    if(message=="骰子卡"):
        starSignNum= random.randint(0, 11)
        planetNum= random.randint(0, 9)
        house= random.randint(1, 12)
        message=planet[planetNum]+","+starSign[starSignNum]+","+str(house)+"宮"
    else:
        message=errorMessage[random.randint(0,6)]+" 妳只能輸入'骰子卡'"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",8080)))