#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for spend_adv

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

# local import
import function as fun

DEBUG_spend_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_key":["收入","支出","記帳狀況"],"_park":["六福村","九族文化村","義大","義大世界"],"money":["支出總額","支出費用","總金額","總額","費用","金錢","錢"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_spend_adv:
        print("[spend_adv] {} ===> {}".format(inputSTR, utterance))


# 這個意圖的名字
intent = "spend_adv"

def getResult(userID, inputSTR, utterance, args, resultDICT):
    # debugInfo(inputSTR, utterance)
    
    if utterance == "去全聯支出3000":
        """
            4: 地點
            6: 說明
            10: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [4,6,10])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = result[0]      # 地點
            resultDICT["description"] = result[1]   # 說明
            resultDICT["amount"] = result[2]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "去全聯花了3000":
        """
            4: 地點
            6: 說明
            10: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [4,6,10])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = result[0]      # 地點
            resultDICT["description"] = result[1]   # 說明
            resultDICT["amount"] = result[2]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "去六福村支出3000":
        """
            3: 地點
            7: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [3,7])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = result[0]      # 地點
            resultDICT["description"] = ""          # 說明
            resultDICT["amount"] = result[1]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "去六福村花了3000":
        """
            3: 地點
            7: 金額
        """ 
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [3,7])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = result[0]      # 地點
            resultDICT["description"] = ""          # 說明
            resultDICT["amount"] = result[1]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "去台北支出3000":
        """
            6: 地點
            8: 說明
            12: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [6,8,12])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = result[0]      # 地點
            resultDICT["description"] = result[1]   # 說明
            resultDICT["amount"] = result[2]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "去台北花了3000":
        """
            6: 地點
            8: 說明
            12: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [6,8,12])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = result[0]      # 地點
            resultDICT["description"] = result[1]   # 說明
            resultDICT["amount"] = result[2]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "支出3000":
        """
            4: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [4])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate()   # 時間
            resultDICT["location"] = ""             # 地點
            resultDICT["description"] = ""          # 說明
            resultDICT["amount"] = result[0]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass


    if utterance == "昨天去全聯支出3000":
        """
            3: 時間
            9: 地點
            11: 說明
            15: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [3,9,11,15])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = result[0]   # 時間
            resultDICT["location"] = result[1]      # 地點
            resultDICT["description"] = result[2]   # 說明
            resultDICT["amount"] = result[3]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天去全聯花了3000":
        """
            3: 時間
            9: 地點
            11: 說明
            15: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [3,9,11,15])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = result[0]          # 時間
            resultDICT["location"] = result[1]      # 地點
            resultDICT["description"] = result[2]   # 說明
            resultDICT["amount"] = result[3]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天去六福村支出3000":
        # 進不來 :(
        resultDICT["intent"] = "error"
        resultDICT["err_msg"] = "不知道怎麼著但你成功進入我們無法進入的領域了！你成功證明了自己不是一個敗家子:)"
        pass


    if utterance == "昨天去六福村花了3000":
        # 進不來 :(
        resultDICT["intent"] = "error"
        resultDICT["err_msg"] = "不知道怎麼著但你成功進入我們無法進入的領域了！你成功證明了自己不是一個敗家子:)"
        pass

    if utterance == "昨天去台北支出3000":
        """
            3: 時間
            9: 地點
            10: 說明
            14: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [3,9,10,14])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = result[0]   # 時間
            resultDICT["location"] = result[1]      # 地點
            resultDICT["description"] = result[2]   # 說明
            resultDICT["amount"] = result[3]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天去台北花了3000":
        """
            3: 時間
            9: 地點
            10: 說明
            14: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [3,9,10,14])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = result[0]   # 時間
            resultDICT["location"] = result[1]      # 地點
            resultDICT["description"] = result[2]   # 說明
            resultDICT["amount"] = result[3]        # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天支出3000": 
        """
            3: 時間
            5: 說明
            9: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [3,5,9])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])   # 時間
            resultDICT["location"] = ""                     # 地點 
            resultDICT["description"] = result[1]           # 說明
            resultDICT["amount"] = result[2]                # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass
    

    if utterance == "昨天花了3000":
        """
            3: 時間
            5: 說明
            9: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [3,5,9])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.TransformDate(result[0])   # 時間
            resultDICT["location"] = ""                     # 地點
            resultDICT["description"] = result[1]           # 說明
            resultDICT["amount"] = result[2]                # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass


    if utterance == "花了3000":
        """
            4: 金額
        """
        status, result = fun.GetAdvArgs(intent, utterance, inputSTR, [4])
        
        if status == True:
            resultDICT["intent"] = intent
            resultDICT["time"] = fun.GetCurrentDate() # 時間
            resultDICT["location"] = ""           # 地點
            resultDICT["description"] = ""        # 說明
            resultDICT["amount"] = result[0]      # 金額
        else:
            resultDICT["intent"] = "error"
            resultDICT["err_msg"] = result
        pass


    # 分析完畢，儲存結果
    if resultDICT["intent"] != "error":
        fun.SaveAccountToCSV(resultDICT, userID)
    
    return resultDICT