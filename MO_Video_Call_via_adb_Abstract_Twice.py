# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:03:41 2023

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

class VideoCall(FieldTest):
    def FT(self):
        print("Video Calling test case execution")
        try:
             subprocess.run("adb shell am start -a android.intent.action.CALL -d tel:08978665826 --ei android.telecom.extra.START_CALL_WITH_VIDEO_STATE 3")
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
            res=subprocess.check_output("adb logcat -d",shell=True) 
            r=str(res)
            result="id=1,ACTIVE"
            if operator.contains(r,result):
                print("PASS")
            else:
                print("FAIL")
                    
        except Exception as e:
            raise e        


i=0
while i <= 1:                    
    FT4= VideoCall()
    FT4.FT()

    FT2 = CallTerm()
    FT2.FT()

    FT3 = CallLogging()
    FT3.FT()

    i=i+1
         