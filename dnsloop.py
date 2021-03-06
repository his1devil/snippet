#! /usr/bin/env python
# -*- coding: utf-8 -*-
import dns.resolver
import os
import httplib

iplist = []
appdomain = "https://twitter.com"

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception,e:
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip+":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)

    try:
        conn.request("GET", "/", headers = {"HOST": appdomain})
        r = conn.getresponse()
        getcontent =  r.read(15)
    finally:
        return

if __name__ == '__main__':
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error"


