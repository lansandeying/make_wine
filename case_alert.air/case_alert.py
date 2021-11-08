#coding=utf-8

from page import alert_page
#
# class EnterApp():
#     def __int__(self):
#         self.po=alert_page.Alert_page
#     def enterApp_success(self):
#         self.po.enter_home()
#     def enterApp_fail(self):
#         self.po.close_app()
#


from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android.recorder import *
from airtest.core.android.adb import *
import os
path_log = os.getcwd() + r"\log"
# 脚本初始化
auto_setup(__file__, devices=[
    "android://127.0.0.1:5037/emulator-5554"],
           logdir=path_log)
# try:
#     poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#     clear_app("com.lihui.winemaking")
#     start_app("com.lihui.winemaking")
#     poco("com.lihui.winemaking:id/tvAgree").click()
# finally:
#     pass

# if __name__=="__main__":
#      EnterApp.enterApp_success()
po=alert_page.Alert_page()
po.enter_home()