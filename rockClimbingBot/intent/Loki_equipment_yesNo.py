#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for equipment_yesNo

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
import random

DEBUG_equipment_yesNo = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_pants":["單車褲","瑜珈褲","短褲","運動褲"],"_rocks":["岩石","岩點","手點","攀岩鞋","攀岩鞋子","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_tmpFix":["規則"],"_whatIs":["星光票"],"_clothes":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登"],"_cityAlias":["區域","地區","城市","縣市","都市"],"_gymsShort":["8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_equipment_yesNo:
        print("[equipment_yesNo] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[上攀][裝備]會不[會]很難買？":
        if args[1] in userDefinedDICT["_climbing"]:
            resultDICT["_equipment_YesNo"] = "不會"
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[可以]不買[裝備]嗎":
        resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "[可以]穿[牛仔褲][抱石]嗎？":
        if args[2] in userDefinedDICT["_climbing"]:
            if args[1] not in userDefinedDICT['_clothesPants'] and args[1] not in userDefinedDICT['_shoes'] and args[1] not in userDefinedDICT['_peClothes']:
                resultDICT["_equipment_YesNo"] = '最好不要，這樣會提高受傷機率'
            else:
                resultDICT["_equipment_YesNo"] = '可以！穿{0}{1}當然沒問題'.format(args[1], args[2])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[可以]穿[牛仔褲]攀岩嗎？":
        if args[1] not in userDefinedDICT['_clothesPants'] and args[1] not in userDefinedDICT['_shoes'] and args[1] not in userDefinedDICT['_peClothes']:
            resultDICT["_equipment_YesNo"] = '最好不要，這樣會提高受傷機率'
        else:
            resultDICT["_equipment_YesNo"] = '可以！穿{0}{1}當然沒問題'.format(args[1], args[2])

    if utterance == "[可以]穿[運動鞋]嗎":
        if args[1] == "運動鞋":
            resultDICT["_equipment_YesNo"] = "最好是穿岩鞋攀岩比較安全哦！"
        elif args[1] in userDefinedDICT['_clothesPants'] and args[1] in userDefinedDICT['_shoes'] and args[1] in userDefinedDICT['_peClothes']:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["_equipment_YesNo"] = '最好不要，這樣會提高受傷機率'

    if utterance == "[安全吊帶]租得到嘛":
        if args[0] in userDefinedDICT["_shoes"] or "岩粉" in args[0] or args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["_equipment_YesNo"] = "通常可以"
        else:
            resultDICT["_equipment_YesNo"] = "通常不行"

    if utterance == "[安全吊帶]買得到嘛":
        if args[0] in userDefinedDICT["_shoes"] or "岩粉" in args[0] or args[0] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[岩粉][必須]買嗎":
        resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "[岩粉]有需要買嗎":
        resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "[岩鞋][岩館]租得到嗎":
        if args[1] in userDefinedDICT["_climbingGym"]:
            if args[0] in userDefinedDICT["_shoes"] or "岩粉" in args[0] or args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["_equipment_YesNo"] = "通常可以"
            else:
                resultDICT["_equipment_YesNo"] = "通常不行"
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[岩鞋]在[岩館]買得到嗎":
        if args[1] in userDefinedDICT["_climbingGym"]:
            if args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_climbingEquip"] or args[0] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["_equipment_YesNo"] = "有些會賣{}，有些不會，這我不太確定耶".format(args[0])
            else:
                resultDICT["_equipment_YesNo"] = "通常不會"
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[岩館][可以]買[鞋子]嗎":
        if args[0] in userDefinedDICT["_climbingGym"]:
            if args[2] in userDefinedDICT["_shoes"] or args[2] in userDefinedDICT["_climbingEquip"] or args[2] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["_equipment_YesNo"] = "有些會賣{}，有些不會，這我不太確定耶".format(args[2])
            else:
                resultDICT["_equipment_YesNo"] = "通常不會"
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[岩館]買得到[鞋子]嗎":
        if args[0] in userDefinedDICT["_climbingGym"]:
            if args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_climbingEquip"] or args[1] in userDefinedDICT["_topRopingEquip"]:
                resultDICT["_equipment_YesNo"] = "有些會賣{}，有些不會，這我不太確定耶".format(args[1])
            else:
                resultDICT["_equipment_YesNo"] = "通常不會"
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Not_sure"])

    if utterance == "[必須]買[岩粉]嗎":
        resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "[抱石][一定]要穿[運動服]嗎":
        if args[0] in userDefinedDICT["_climbing"]:
            if args[2] in userDefinedDICT["_clothesPants"] or args[2] in userDefinedDICT["_shoes"] or args[2] in userDefinedDICT["_peClothes"]:
                resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_need"])
            else:
                resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石][可以]穿[短袖]嗎？":
        if args[0] not in userDefinedDICT["_climbing"]:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[1] in userDefinedDICT["_clothesPants"] or args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_peClothes"]:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])

    if utterance == "[抱石]租得到[鞋子]嗎":
        if args[0] in userDefinedDICT["_climbing"]:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[抱石]要買[鞋子]嗎":
        if args[0] not in userDefinedDICT["_climbing"]:
            resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])
            return resultDICT

    if utterance == "[抱石]需要穿[運動褲]嗎":
        if args[0] not in userDefinedDICT["_climbing"]:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])
            return resultDICT
        if args[1] in userDefinedDICT["_clothesPants"] or args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_peClothes"]:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_need"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])

    if utterance == "[新手]有需要買[裝備]嗎":
        resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "[衣著]有限制嗎？":
        if args[0] in userDefinedDICT["_clothesPants"]:
            resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]
        else:
            resultDICT["_equipment_YesNo"] = "應該沒有"

    if utterance == "去[岩館]要帶[岩粉]嗎":
        if args[1] in userDefinedDICT["_climbingEquip"] or args[1] in userDefinedDICT["_shoes"] or args[1] in userDefinedDICT["_topRopingEquip"]:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_need"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])

    if utterance == "攀岩[一定]要穿[運動服]嗎":
        resultDICT["_equipment_YesNo"] = "攀岩{}".format(defaultResponse["_equipment_wear"])

    if utterance == "攀岩[可以]穿短袖嗎？":
        resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])

    if utterance == "攀岩[裝備]會不[會]很難買？":
        resultDICT["_equipment_YesNo"] = '不會。很多岩館都有賣，也可以逛逛戶外休閒用品店或網路商店'

    if utterance == "攀岩租得到[鞋子]嗎":
        if args[0] in userDefinedDICT["_peClothes"] or args[0] == "岩鞋" or args[0] == "裝備":
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])

    if utterance == "攀岩要買[鞋子]嗎":
        resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "攀岩需要穿[運動褲]嗎":
        if args[0] in userDefinedDICT["_peClothes"] or args[0] == "岩鞋" or args[0] == "裝備":
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_need"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])

    if utterance == "有[dress] code嗎？":
        resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "有規定要穿什麼嗎":
        resultDICT["_equipment_YesNo"] = defaultResponse["_equipment_wear"]

    if utterance == "穿[短袖][可以][抱石]嗎":
        if args[2] in userDefinedDICT["_climbing"]:
            if args[0] in userDefinedDICT["_clothesPants"] or args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
                resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
            else:
                resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "穿[短袖][可以]去攀岩嗎":
        if args[0] in userDefinedDICT["_clothesPants"] or args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])

    if utterance == "穿[短袖][可以]攀岩嗎":
        if args[0] in userDefinedDICT["_clothesPants"] or args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])

    if utterance == "要帶[岩粉]嗎":
        if args[0] in userDefinedDICT["_clothesPants"] or args[0] in userDefinedDICT["_shoes"] or args[0] in userDefinedDICT["_peClothes"]:
            resultDICT["_equipment_YesNo"] = "{} 帶著比較好".format(random.choice(defaultResponse["_Yes_can"]))
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_need"])

    if utterance == "[可以]穿[一般][運動鞋]去[抱石]嗎":
        if args[3] in userDefinedDICT["_climbing"]:
            if args[2] in userDefinedDICT["_clothesPants"] or args[2] == "岩鞋":
                resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
            else:
                resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "[可以]穿[一般][運動鞋]去攀岩嗎":
        if args[2] in userDefinedDICT["_clothesPants"] or args[2] == "岩鞋":
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])

    if utterance == "[可以]穿[牛仔褲][抱石]嗎？":
        if args[2] in userDefinedDICT["_climbing"]:
            if args[1] in userDefinedDICT["_clothesPants"] or args[1] == "岩鞋":
                resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
            else:
                resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_not_rock_climbing"])

    if utterance == "攀岩[可以]穿[短袖]嗎？":
        if args[1] in userDefinedDICT["_clothesPants"] or args[1] == "岩鞋":
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_Yes_can"])
        else:
            resultDICT["_equipment_YesNo"] = random.choice(defaultResponse["_No_not"])

    if utterance == "有dress code嗎？":
        # write your code here
        pass

    return resultDICT