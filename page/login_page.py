#coding = utf-8
from lib import common
from conf import setting
from lib import log

class Login_page():
    def __init__(self):
        self.log = log.MyLog()
        self.common = common.Common()
        #我的菜单栏
        self.mine="com.lihui.winemaking:id/tlIcon"
        #跳转登录按钮
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

    def login(self,phone_num,code_num):
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
            self.log.error("s%" % msg)
        finally:
            pass