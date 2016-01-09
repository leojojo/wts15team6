#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy

consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

# Mentionの取得
# 自分宛てのツイートを取得して表示
mentions = api.mentions_timeline(count=10)
for tweet in mentions:
    print tweet.user.screen_name, tweet.text

# ツイートを送信
try:
    api.update_status(status='Hello, world!')
    # api.update_status(status=u'こんにちは世界さん')
except tweepy.TweepError as e:
    print e