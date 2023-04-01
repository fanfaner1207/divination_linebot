# divination_linebot

簡介：這是一個骰子卡小linebot 在沒有牌的情況使用

google cloud run 有使用到docker
用docker執行python flask打包過後的容器
requirements.txt內是一些需要安裝在docker的python套件跟版本

＃注意
使用前記得要在根目錄新增secret.py檔
裡面要有兩行程式
CHANNEL_ACCESS_TOKEN=""
CHANNEL_SECRET=""
都在line developers
一個在basic settings
另一個在messaging api

本來要用google cloud secret manager安全性超棒
但是Webhook settings的verify一直timeout
也就是安全性的代價是慢到爆
也想過設定環境變數的yaml檔
但密碼還是被留在檔案內
乾脆寫個小python檔直接存變數
還不用像txt檔要read file

＃line developers要注意的點
webhook URL 要在網址尾巴補上/callback
伺服器必須要有一個 "/callback" 的位置，用來接收 LINE 發送過來的資訊，並且回傳'OK'
