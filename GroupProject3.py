#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:44:52 2021
Group Project #3
@author: jeremiahjohn
"""
# This command will import the regexp module
import re

# This command will import the csv module
import csv

# This command will import the counter module 
from collections import Counter
# This command will retrieve the data from the URL
import urllib.request
web = 'https://s3.amazonaws.com/tcmg476/http_access_log'
urllib.request.urlretrieve(web,'./http_access_log.txt')

# Finding requests from last 6 Months
def user2(file):
    with open(file) as fn:
        http_access_log = fn.read()
        month1 = re.findall("Oct/1995", http_access_log)
        month2 = re.findall("Sep/1995", http_access_log)
        month3 = re.findall("Aug/1995", http_access_log)
        month4 = re.findall("Jul/1995", http_access_log)
        month5 = re.findall("Jun/1995", http_access_log)
        month6 = re.findall("May/1995", http_access_log)
        last6months = month1 + month2 + month3 + month4 + month5 + month6
        return(last6months)


# Finding all requests
def user(file):
    with open(file) as fn:
        http_access_log = fn.read()
        year1 = re.findall("1994", http_access_log)
        year2 = re.findall("1995", http_access_log)
        total = year1 + year2
        return(total)

#returns total requests
def count1(total):
    return Counter(total)
#returns last 6 months requests
def count2(last6months):
    return Counter(last6months)

def csv1(counter1):
    with open("total.csv", "w") as csvfile:
        write = csv.writer(csvfile)
        heading = ["Total Requests"]
        write.writerow(heading)
        for tots in counter1:
            write.writerow((tots, counter1[tots]))

def csv2(counter2):
    with open("last6.csv", "w") as csvfile:
        write = csv.writer(csvfile)
        heading = ["Last 6 Months","Requests"]
        write.writerow(heading)
        for tots in counter2:
            write.writerow((tots,counter2[tots]))

if __name__ == "__main__":
    csv1(count1(user("http_access_log.txt")))
    csv2(count2(user2("http_access_log.txt")))

           
