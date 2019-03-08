from selenium import webdriver
from bs4 import BeautifulSoup
import re
import selenium
import time
import datetime


cridit = 0
def divide(cell):
    values = cell.split("\n")
    code = values[0]
    b = int(credit(code))
    marks = int(values[4])
    a = int(grade(marks,b))
    return a,b



def credit(code):
    if(re.search("^[0-9][0-9][A-Z][A-Z][A-Z][0-9][0-9]$",code)):
        return 2
    elif(re.search("^[0-9][0-9][A-Z][A-Z][0-9][0-9]$",code)):
        return 4
    elif(re.search("^[0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$",code)):
        return 3

def grade(a,b):
    if(a < 40):
        # print(0,b)
        return 0*b
    elif(a < 45 and a >=40):
        # print(4,b)
        return 4*b
    elif(a < 50 and a >=45):
        # print(5,b)
        return 5*b
    elif(a < 60 and a >=50):
        # print(6,b)
        return 6*b
    elif(a < 70 and a >=60):
        # print(7,b)
        return 7*b
    elif(a < 80 and a >=70):
        # print(8,b)
        return 8*b
    elif(a < 90 and a >=80):
        # print(9,b)
        return 9*b
    elif(a >=90):
        # print(10,b)
        return 10*b
def haveToCall(u):
    try:
        print("wating....")
        options = webdriver.Safari(executable_path = '/usr/bin/safaridriver')
        print("still...wating...")
        options.get("http://results.vtu.ac.in/resultsvitavicbcs_19/index.php")
        boxusn = options.find_element_by_name("lns")
        print("Enter USN")
        usn ="1bo16is0"+str(u)
        boxusn.send_keys(usn)
        print("enter captcha number carefully")
        cap = input()
        boxcap = options.find_element_by_name("captchacode")
        boxcap.send_keys(cap)
        submit = options.find_element_by_id("submit")
        submit.click()
        sub = [] #empty list
        # smaple = input()
        time.sleep(1)
        html = options.page_source
        # print(html)
        soup = BeautifulSoup(html,'html.parser')
        options.quit()
        tableRows = soup.findAll('div',{"class":"divTableRow"})
        tableRows.pop(9)
        tableRows.pop(0)
        for cell in tableRows:
            sub.append(cell.text.strip())
        total = 0
        cridit = 0
        for i in sub:
            a,b = divide(i)
            total = total + a
            cridit = cridit + b
        forName = []

        name = soup.find('table',{"table":""})
        mid = str(name.text)
        forName = mid.split("\n")
        realName = forName[7]
        sgpa = total/cridit
        per = sgpa * 9.5
        sgpa = round(sgpa,2)
        per = round(per,2)
        if(per > 60):
            print("Congration")
        print(realName+" your")
        print("SGPA is ",sgpa," percent",per )
        timestamp = str(datetime.datetime.now())
        file = open("resultSamClass.csv","a")
        file.write(usn+","+realName+","+str(sgpa)+","+str(per)+","+str(timestamp)+"\n")
        file.close()
    except:
        print("Something has Happened \n Try again ")
        options.quit()
