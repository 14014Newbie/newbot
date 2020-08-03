# -*- coding: utf-8 -*-
# Kalo ga jalan ini sc berarti gua masih nub :v
from Newbielib import *
from Newbielib.akad.ttypes import Message 
from Newbielib.akad.ttypes import ContentType as Type 
import json, requests, sys 
from akad.ttypes import ContentType as Type 
from akad.ttypes import Message 
from multiprocessing import Pool, Process 
from time import sleep 
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib3, wikipedia, html5lib 
from datetime import timedelta, date 
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest 
_session = requests.session()
from datetime import datetime 
from bs4 import BeautifulSoup 
from googletrans import Translator 
from gtts_token.gtts_token import Token  
from gtts import gTTS 
import youtube_dl

#line = LINE('EMAIL', 'PASSWORD')
#line = LINE('AUTHTOKEN')
line = LINE() #loginqr
line.log("Auth Token : " + str(line.authToken))

# Initialize OEPoll with LINE instance
oepoll = OEPoll(line)

class Callback:
    def __init__(self, line, chatId):
        self.line = line
        self.chatId = chatId
    def callback(self, message):
        self.line.sendMessage(self.chatId, str(message))

# Receive messages from OEPoll
def RECEIVE_MESSAGE(op):
    msg = op.message

    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from
    
    # Check content only text message
    if msg.contentType == 0:
        # Check only group chat
        if msg.toType == 2:
            # Check if want get token
            if str(text).lower() == 'gettoken':
                callback = Callback(line, receiver)
                login = LINE(callback=callback.callback)
                line.sendMessage(login.profile.mid, "Auth Token : " + login.authToken)
            # Print log
            line.log(txt)

# Add function to OEPoll
oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE
})

while True:
    oepoll.trace()
