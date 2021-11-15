#coding=utf-8
import time
from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android.adb import *
import os
from lib import log
import traceback


class Common():
    def __init__(self):
        self.log = log.MyLog()
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


    @staticmethod
    def now_Time(doing):
        return doing +": "+ time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())

    def star_app(self,app_name):
        start_app(app_name)

    def stop_app(self,app_name):
        stop_app(app_name)

    def clear_app(self,app_name):
        clear_app(app_name)

    def send_text(self,value):
        text(value)

    def back(self):
        keyevent("BACK")

    def click_by_name(self,name_value):
        try:
            self.poco(name=name_value).wait_for_appearance()
        except Exception as msg:
            print("%s" % msg)
        else:
            self.poco(name=name_value).click()

    def click_by_nams(self,name_value,index):
        try:
            self.poco(name=name_value).wait_for_appearance()
        except Exception as msg:
            print("%s" % msg)
        else:
            self.poco(name=name_value)[index].click()

    def click_by_text(self,text_value):
        try:
            self.poco(text=text_value).wait_for_appearance()
        except Exception as msg:
            print("%s" % msg)
        else:
            self.poco(text=text_value).click()

    def get_attr_text(self,name_value):
        try:
            self.poco(name=name_value).wait_for_appearance()
        except Exception as msg:
            traceback.print_exc()
        else:
            return self.poco(name=name_value).get_text()

    def swipe_by_name_up(self,name_value):
        try:
            self.poco(name=name_value).wait_for_appearance()
        except Exception as msg:
            print("%s" % msg)
        else:
            self.poco(name=name_value).swipe('up')

    def swipe_by_name_down(self,name_value):
        try:
            self.poco(name=name_value).wait_for_appearance()
        except Exception as msg:
            print("%s" % msg)
        else:
            self.poco(name=name_value).swipe('down')

    def swipe_up(self):
        self.poco.swipe([0.5, 0.9], [0.5, 0.1])

    def swipe_down(self):
        self.poco.swipe([0.5, 0.1], [0.5, 0.9])

    def get_text_by_name(self,name_value):
        # 获取控件的“text”属性值
        return self.poco(name_value).attr("text")

    def assert_equal(self,value1,value2,mes):
        assert_equal(value1, value2, mes)

    def assert_not_equal(self,value1,value2,mes):
        assert_not_equal(value1, value2, mes)


if __name__=="__main__":
    print(Common.now_Time("xianaza"))

