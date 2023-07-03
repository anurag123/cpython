# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:58:48 2023

@author: skc
"""
from abc import ABC, abstractmethod
import subprocess
import time
import operator
import requests
import re

class FieldTest(ABC):
    @abstractmethod
    def FT(self):
        pass

class DataBrowsing(FieldTest):
    def FT(self):
        print("Data browsing test case execution")
        try:
            subprocess.run("adb shell am start -a android.intent.action.VIEW -d http://www.gmail.com", shell=True)
            time.sleep(20)
        except Exception as e:
            print("Error in moBrowse:", e)


class DataLogging(FieldTest):
    def FT(self):
        print("Data logging test case execution")
        try:
            res = subprocess.check_output("adb logcat -d", shell=True)
            r = str(res)
            url = "http://www.gmail.com"
            if self.is_valid_url(url):
                print("PASS")
            else:
                print("FAIL")
        except Exception as e:
            print("Error in logmsg:", e)

    def is_valid_url(self, url):
        pattern = r"^http://www\.gmail\.com$"
        if re.match(pattern, url):
            return True
        else:
            return False

i=0
while i<=1:
    FT5 = DataBrowsing()
    FT5.FT()

    FT6 = DataLogging()
    FT6.FT()

    i+=1
