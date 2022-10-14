#!/usr/bin/env python
# coding=utf-8
import requests
import pyperclip
import re
import os
import sys
import json
#获取家目录路径
path = os.environ['HOME'] + "/.terlist"

def readConfig():
    file_path = os.environ['HOME'] + "/.config/ters.json"
    if os.path.exists(file_path):
        with open(file_path,mode='r',encoding='utf-8') as f:
            json_data = json.load(f)
            return json_data
    else:
        return {}

def main():

    URL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    resStr = '\"tgt\"\:\"(.*?)\"\}'
    Strend = ""
    #获取标准缓冲区

    Str = " ".join(sys.argv)[len(sys.argv[0]) + 1:]
    if len(sys.argv) >= 2:
        if len(re.findall(".*? -l$", " ".join(sys.argv), re.S)) == 1:
            os.system("tac ~/.terlist/.terlist | less")
            return

    conf = readConfig()
    if conf == {}:
        data = {"i": Str, "from": "AUTO", "to": "AUTO", "doctype": "json"}
    else:
        data = {"i": Str, "from": conf['from'], "to": conf['to'], "doctype": "json"}
    res = requests.post(url=URL, data=data)
    res = res.content.decode("utf-8")
    StrJson = re.findall(resStr, res, re.S)
    for st in StrJson:
        Strend += st
    print("FROM = " + Str + "\nTO   = " + Strend)
    str = "echo \"" + Strend + "\" | xclip -selection clipboard"
    os.system(str)
    if (len(sys.argv)) == 2 and ord(list(Str)[0]) < 1000:
        if ord(list(Str)[0]) > 1000 or ord(list(Strend)[0]) > 1000:
            Terlist(Str, Strend)


def Terlist(a, b):
    if not os.path.exists(path):
        os.mkdir(path)
        f = open(path + "/terlist","w")
        f.close()
    else:
        with open(path + "/terlist") as f:
            fc = f.read()
            if len(re.findall(a, fc)) < 1:
                with open(path + "/terlist", "a+") as f:
                    f.write(a + " " + b + '\n')
                    print("加入生僻字>>  " + a + ":" + b)


main()
