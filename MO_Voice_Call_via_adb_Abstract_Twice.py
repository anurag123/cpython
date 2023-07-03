# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:55:31 2023

@author: skc
"""
from abc import ABC, abstractmethod
import subprocess
import time
import operator

class FieldTest(ABC):
    @abstractmethod
    def FT(self):
        pass


class VoiceCalling(FieldTest):
    def FT(self):
        print("Voice calling test case execution")
        try:
            subprocess.run("adb shell am start -a android.intent.action.CALL -d tel:$08978665826")
            time.sleep(20)
        except Exception as e:
            raise e
class CallTerm(FieldTest):
    def FT(self):
        print("Call termination test case execution")
        try:
            subprocess.run("adb shell input keyevent 6")
        except Exception as e:
            raise e
class CallLogging(FieldTest):
    def FT(self):
        print("Call logging test case execution")
        try:
            res = subprocess.check_output("adb logcat -d", shell=True)
            r = str(res)
            result = "id=1,ACTIVE"
            if operator.contains(r, result):
                print("PASS")
            else:
                print("FAIL")
        except Exception as e:
            raise e

i=0
while i<=1:
    FT1 = VoiceCalling()
    FT1.FT()

    FT2 = CallTerm()
    FT2.FT()

    FT3 = CallLogging()
    FT3.FT()

    i=i+1