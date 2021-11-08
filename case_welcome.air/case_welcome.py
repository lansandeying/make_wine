#coding=utf-8

# from page import alert_page
#
# class EnterApp():
#     def __int__(self):
#         self.po=alert_page.Alert_page
#     def enterApp_success(self):
#         self.po.enter_home()
#     def enterApp_fail(self):
#         self.po.close_app()
#
# if __name__=="__main__":
#     EnterApp.enterApp_success()
from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android.recorder import *
from airtest.core.android.adb import *
import os
try:
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    poco("com.lihui.winemaking:id/ivInviteReward").click()
    keyevent("BACK")
finally:
    pass