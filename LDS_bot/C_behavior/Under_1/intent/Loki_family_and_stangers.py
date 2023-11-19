#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for family_and_stangers

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_family_and_stangers = True
CHATBOT_MODE = True

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_family_and_stangers.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_family_and_stangers:
        print("[family_and_stangers] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[不太]確定": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[小孩][很]喜歡跟[人]玩":
        if CHATBOT_MODE:
            resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
            resultDICT["q5"] = False
        else:
            # write your code here
            pass

    if utterance == "[小孩][很]害羞": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[小孩]不喜歡[別人]碰[他]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[小孩]不太理人": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "[常常]":
        if CHATBOT_MODE:
            if "不常" in inputSTR:
                resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
                resultDICT["q5"] = False
            else:
                resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
                resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "[很少]":
        if CHATBOT_MODE:
            if "很少" in inputSTR:
                resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
                resultDICT["q5"] = False
            else:
                resultDICT["response"] = "那如果孩子手上或眼前的物品或玩具掉落，他會不會左顧右盼地去尋找呢？"
                resultDICT["q5"] = True
        else:
            # write your code here
            pass

    if utterance == "不[一定]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "沒[什麼]反應": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    if utterance == "看[心情]": #去reply裡面抓引導用問題
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            # write your code here
            pass

    return resultDICT