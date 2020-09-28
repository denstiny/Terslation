#!/usr/bin/env python
# coding=utf-8
import requests
import re
import sys


def main():

    URL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    resStr = '\"tgt\"\:\"(.*?)\"\}'
    Strend = ""
    Str = ""
    print(type(Str))
    Str = input()

    data = {"i": Str, "from": "AUTO", "to": "AUTO", "doctype": "json"}
    res = requests.post(url=URL, data=data)
    res = res.content.decode("utf-8")
    StrJson = re.findall(resStr, res, re.S)
    for st in StrJson:
        Strend += st
    print("InputStr = " + Str + "\nTerlat   = " + Strend)
    pass


main()
