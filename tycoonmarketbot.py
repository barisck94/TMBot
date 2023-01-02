# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:18:10 2022

@author: PC
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import json

try:
    with open('cache.json') as json_file:
        cache = json.load(json_file)
except:
    with open('cache.json', 'w') as outfile:
        cache = {
            "svid": "",
            "username": "",
            "password": "",
            "input1": ""
            }
        cachestrings = json.dumps(cache)
        outfile.write(cachestrings)
    with open('cache.json') as json_file:
        cache = json.load(json_file)

while 1:
    os.system('cls' if os.name == 'nt' else 'clear')  
    try:
        svid = str(input("server: (us/sw)\nonceki icin bos birak:\n"))
        if svid == "":
            svid = cache["svid"]
        break
    except:
        print("hata")
        pass
        
while 1:
    os.system('cls' if os.name == 'nt' else 'clear')  
    try:
        username = str(input("\nKullanıcı Adı: "))
        if username == "":
            username = cache["username"]
        break
    except:
        print("hata")
        pass

while 1:
    os.system('cls' if os.name == 'nt' else 'clear')  
    try:
        password = str(input(username + "\nŞifre: "))
        if password == "":
            password = cache["password"]
        break
    except:
        print("hata")
        pass

while 1:
    os.system('cls' if os.name == 'nt' else 'clear')  
    goodslist = dict()
    try:
        input1 = str(input('Kullanılacak Hammadeler,miktar:\n'))
        if input1 == "":
            input1 = cache["input1"]
        else:
            input1 = list(input1.split(" "))
        for i in range(len(input1)):
            liste = str(input1[i]).split(",")
            goodslist.update({str(liste[0]):int(liste[1])})
        break
    except:
        print("hata")
        pass

cache = {
    "svid": svid,
    "username": username,
    "password": password,
    "input1": input1
    }

cache = json.dumps(cache)
with open('cache.json', 'w') as outfile:
    outfile.write(cache)
    
ids = {
    "alc": 3,
    "bre": 5,
    "clo": 7,
    "cot": 9,
    "flo": 11,
    "fre": 13,
    "fro": 15,
    "fur": 17,
    "gas": 19,
    "mar": 21,
    "new": 23,
    "oil": 25,
    "pap": 27,
    "pig": 29,
    "plk": 31,
    "pls": 33,
    "sau": 35,
    "sto": 37,
    "thr": 39,
    "toy": 41,
    "whe": 43,
    "woo": 45,
    "fs": 2,
    "cs": 3,
    "mw": 4,
    "mo": 5,
    "pl": 6,
    "price": 7
    }

def bgtable (i,urlid2):
    urlid1 = str(ids[list(goodslist.keys())[i]])
    urlid2 = str(ids[urlid2])
    table = "/html/body/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr["+str(urlid1)+"]/td["+str(urlid2)+"]/div"
    table = driver.find_element(By.XPATH,table)
    table = str(str(table.text).replace("savings1: ", ""))
    table = table.replace(",", "")
    table = table.replace("i$", "")
    table = table.replace("iKr", "")
    table = int((table).replace(" ", ""))
    return table

def savings():
    savings = driver.find_element(By.XPATH,"/html/body/div[2]/table[1]/tbody/tr[2]/td[2]")
    savings = str(savings.text).replace("Savings: ","")
    savings = savings.replace("iKr","")
    savings = savings.replace("i$", "")
    savings = savings.replace(",", "")
    savings = int(savings.replace(" ",""))
    return savings

def restart():
    openlink("loginpage")
    username_input = driver.find_element("name", "userName")
    password_input = driver.find_element("name", "password")
    username_input.send_keys(username)
    password_input.send_keys(password)
    buttons("login")
    openlink("buygoods")
    
def buttons(buttonid,i=0):
    buttondict = {
        "sw":{
            "np": "/html/body/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr["+str(ids[list(goodslist.keys())[i]])+"]/td[2]/div",
            "pre": "/html/body/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/div[2]/input",
            "order": "/html/body/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/input",
            "login": '/html/body/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/input'
            },
        "us":{
            "np": "/html/body/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr["+str(ids[list(goodslist.keys())[i]])+"]/td[2]/div",
            "pre": "/html/body/div[2]/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/div[2]/input",
            "order": "/html/body/div[2]/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td/input",
            "login": "/html/body/div[2]/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/input"
            }}
    buttons1 = driver.find_element(By.XPATH, buttondict[svid][buttonid])
    buttons1.click()

def maxgoods():
    if svid == "us":
        xp = "/html/body/div[2]/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/font"
    if svid == "sw":
        xp = "/html/body/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/font"
    maxgoods = driver.find_element(By.XPATH,xp)
    maxgoods = str(maxgoods.text).replace("(max ","")
    maxgoods = maxgoods.replace(")","")
    maxgoods = maxgoods.replace(",","")
    maxgoods = maxgoods.replace(" ","")
    return maxgoods

def purchase(maxp):
    if svid == "us":
        xp = "/html/body/div[2]/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/input"
    if svid == "sw":
        xp = '/html/body/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/input'
    purchase_input1 = driver.find_element(By.XPATH,xp)
    purchase_input1.send_keys(maxp)

def openlink(link):
    links = {
        "sw":{
            "buygoods": 'https://tycoononline.nu/frame_index.php?page=marketSales',
            "loginpage": "https://tycoononline.nu/frame_index.php?page=login"
            },
        "us":{
            "buygoods": "https://usa.tycoononline.com/frame_index.php?page=marketSales",
            "loginpage": "https://usa.tycoononline.com/frame_index.php?page=login"
            }
        }
    driver.get(str(links[svid][link]))
    
rr = 400
driver = webdriver.Chrome()
restart()
atm = time.time()

while 1:
    try:
        for i in range(len(goodslist)):
            if time.time() - atm > rr:
                restart()
                openlink("buygoods")
                atm = time.time()
            forsale = bgtable(i, "fs")
            comingsoon = bgtable(i, "cs")
            mywarehouse = bgtable(i, "mw")
            myorders = bgtable(i, "mo")
            price = bgtable(i, "price")
            amount = int(list(goodslist.values())[i])
            print(list(goodslist.keys())[i],forsale,comingsoon,mywarehouse,myorders,price,amount)
            if (forsale>1 and mywarehouse<amount):
                savings1 = savings()
                maxpurchase = min((amount-mywarehouse-myorders),int((savings1/price)-10))
                if maxpurchase>1:
                    buttons("np",i)
                    max_goods = int(maxgoods())
                    maxpurchase = min((amount-mywarehouse-myorders),int((savings1/price)-1),max_goods)
                    purchase(maxpurchase)
                    buttons("pre")
                    buttons("order")
                    time.sleep(3)
                    openlink("buygoods")
                    atm = time.time()
                else:
                    time.sleep(1)
            else:
                time.sleep(1)
    except:
        restart()
        pass
    