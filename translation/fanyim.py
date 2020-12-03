#!/usr/bin/env python
# coding=utf-8
import requests
import re
import os
import sys
#获取家目录路径
path = os.environ['HOME'] + "/.terlist/"


def main():

    URL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    resStr = '\"tgt\"\:\"(.*?)\"\}'
    Strend = ""
    #获取标准缓冲区

    Str = " ".join(sys.argv)[len(sys.argv[0]) + 1:]
    if len(sys.argv) >= 2:
        if len(re.findall(".*? -l$", " ".join(sys.argv))) == 1:
            os.system("tac ~/.terlist/.terlist | less")
            return

    data = {"i": Str, "from": "AUTO", "to": "AUTO", "doctype": "json"}
    res = requests.post(url=URL, data=data)
    res = res.content.decode("utf-8")
    StrJson = re.findall(resStr, res, re.S)
    for st in StrJson:
        Strend += st
    print("InputStr = " + Str + "\nTerlat   = " + Strend)
    if (len(sys.argv)) == 2:
        if ord(list(Str)[0]) > 1000 or ord(list(Strend)[0]) > 1000:
            Terlist(Str, Strend)


def Terlist(a, b):
    with open(path + ".terlist") as f:
        fc = f.read()
        if len(re.findall(a, fc)) < 1:
            with open(path + ".terlist", "a+") as f:
                f.write(a + " " + b + '\n')
                print(a + " " + b + " 加入生僻字")


main()
