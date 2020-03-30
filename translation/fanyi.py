#!/usr/bin/env python
# coding=utf-8
import requests
import re
def main():

    URL= "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    Str = ""
    Strend = ""
    resStr = '\"tgt\"\:\"(.*?)\"\}'
    with open("/home/chroot/.fanyi.txt","r") as f:
        for line in f:
            Str += line
    data = {
        "i":Str,
        "from":"AUTO",    
        "to":"AUTO",
        "doctype":"json"
    }
    res = requests.post(url = URL,data = data)
    res = res.content.decode("utf-8")
    StrJson = re.findall(resStr,res,re.S)
    for str in StrJson:
        Strend += str
    print(Strend)
main()
