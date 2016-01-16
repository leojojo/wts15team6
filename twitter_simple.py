#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import codecs
import os
import re
import sys

consumer_key        = 'tMW349UNzlmIRztNIyp8coJSa'
consumer_secret     = '3h5sUb2WJC1jaGflGPvuvxJ0vGh5VYXq4qmoyAmTQdD5sRraGI'
access_token        = '4620166219-RfRL8kwOJbQ9tuHZLWhDYTP5CoufZ1joUJWFkXd'
access_token_secret = 'B7CD5FxXwoeiTNXWbOrklmUWacfwFOE8yFm6Qe98LunTp'

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

# Brokenクラス
class Broken():
  def __init__(self,_date,_username, _text):
    self.date    = _date;
    self.username= _username;
    self.text    = _text;

# 取得したデータ(Brokenクラス)の配列
BrokenList = []

sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

# 検索してデータを格納
keywords = u'別れ(まし)*た' #either 別れた or 別れました
for tweet in api.search(q=keywords, count=10):
  tweet.created_at, tweet.user.screen_name, tweet.text
  if re.search(u'^RT @[a-zA-Z0-9_]*:', broken.text) or re.search(u'bot', broken.user_name):  #ignore tweets starting with RT @[alphanum]: or with username with bot
      pass
  else:
      BrokenList.append(Broken(tweet.created_at, tweet.user.screen_name, tweet.text))

fp = codecs.open('output.txt','w','utf-8')

# 表示
for broken in BrokenList:
    print broken.date, broken.username, broken.text
    fp.write(broken.text + "\n")

fp.close()

# 外部コマンドの実行には `os.system()` を使う
os.system('chasen < output.txt > output.txt.chasen')

# 人名の一文字目を格納する配列
names = []
initial = ""

# 練習問題3(第4回課題)を参照
for line in codecs.open('output.txt.chasen','r','utf-8'):
    line = line.rstrip('\r\n')
    if line == "EOS":
      print names
      names = []
    else:
      lis = line.split("\t")
      if re.search(ur"人名",lis[3]):  #村井^Iムライ^I村井^I名詞-固有名詞-人名-姓^I^I
        if re.search(ur"^[カキクケコ]", lis[1]):
          initial = "K"
        elif re.search(ur"^[サシスセソ]", lis[1]):
          initial = "S"
        elif re.search(ur"^[タツテト]", lis[1]):
          initial = "T"
        elif re.search(ur"^[チ]", lis[1]):
          initial = "C"
        elif re.search(ur"^[ナニヌネノ]", lis[1]):
          initial = "N"
        elif re.search(ur"^[ハヒヘホ]", lis[1]):
          initial = "H"
        elif re.search(ur"^[フ]", lis[1]):
          initial = "F"
        elif re.search(ur"^[マミムメモ]", lis[1]):
          initial = "M"
        elif re.search(ur"^[ヤユヨ]", lis[1]):
          initial = "Y"
        elif re.search(ur"^[ガギグゲゴ]", lis[1]):
          initial = "G"
        elif re.search(ur"^[ザジヂズヅゼゾ]", lis[1]):
          initial = "Z"
        elif re.search(ur"^[ダデド]", lis[1]):
          initial = "D"
        elif re.search(ur"^[バビブベボ]", lis[1]):
          initial = "B"
        elif re.search(ur"^[パピプペポ]", lis[1]):
          initial = "P"
        elif re.search(ur"^[ア]", lis[1]):
          initial = "A"
        elif re.search(ur"^[イ]", lis[1]):
          initial = "I"
        elif re.search(ur"^[ウ]", lis[1]):
          initial = "U"
        elif re.search(ur"^[エ]", lis[1]):
          initial = "E"
        elif re.search(ur"^[オ]", lis[1]):
          initial = "O"

# 一旦false
if False:
    # ツイートを送信
    try:
        api.update_status(status='Hello, world!')
        # api.update_status(status=u'こんにちは世界さん')
    except tweepy.TweepError as e:
        print e
