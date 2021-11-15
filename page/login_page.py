# -*- encoding=utf-8 -*-
from lib import common
from airtest.core.api import *
import os
import traceback

path_log = os.getcwd() + r"\log"

class Login_page():
    def __init__(self):
        self.common = common.Common()
        #我的菜单栏
        self.mine="com.lihui.winemaking:id/tlIcon"
        #跳转登录按钮/登录成功名称按钮
        self.toLogin="com.lihui.winemaking:id/mTvUserName"
        #协议按钮
        self.agreement="com.lihui.winemaking:id/mCbAgreement"
        #账号输入框
        self.enterPhone="com.lihui.winemaking:id/etPhone"
        #获取验证码按钮
        self.getCode="com.lihui.winemaking:id/tvGetCode"
        #验证码输入框
        self.enterCode="com.lihui.winemaking:id/etCode"
        #登录按钮
        self.login="com.lihui.winemaking:id/tvLogin"


    def click_mine(self):
        self.common.click_by_nams(self.mine,1)

    def click_toLogin(self):
        self.common.click_by_name(self.toLogin)

    def click_agreement(self):
        self.common.click_by_name(self.agreement)

    def click_enterPhone(self):
        self.common.click_by_name(self.enterPhone)

    def click_getCode(self):
        self.common.click_by_name(self.getCode)

    def click_enterCode(self):
        self.common.click_by_name(self.enterCode)

    def click_login(self):
        self.common.click_by_name(self.login)

    def login_set(self,phone_num="18033084759",code_num="123456"):
        try:
            self.click_mine()
            self.click_toLogin()
            self.click_agreement()
            self.click_enterPhone()
            self.common.send_text(phone_num)
            self.click_getCode()
            self.click_enterCode()
            self.common.send_text(code_num)
            self.click_login()
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass

    def assert_login(self,value2):
        try:
            text_value = self.common.get_attr_text(self.toLogin)
            self.common.assert_equal(text_value, value2, "验证登录登录成功")
        except Exception as msg:
            traceback.print_exc("登录失败")
        finally:
            pass

#
# if __name__=="__main__":
#     pass
    # auto_setup(__file__, devices=[
    # "android://127.0.0.1:5037/emulator-5554?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH"],
    #         logdir=path_log)
