# coding:utf-8

import pyttsx
engine = pyttsx.init()
engine.say('hello world')
engine.say('你好，郭璞')
engine.runAndWait()
# 朗读一次
engine.endLoop()