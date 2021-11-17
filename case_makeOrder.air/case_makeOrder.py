# -*- encoding=utf-8 -*-
from page import alert_page,login_page
import os
from airtest.core.api import *
from airtest.core.android.adb import *
from lib import common

# al=alert_page.Alert_page()
# al.enter_home()

class Case_makeOrder():
    def __init__(self):
        self.alert=alert_page.Alert_page()
        self.login=login_page.Login_page()


    def case_login_success(self,phone_num,code_num,user_name):
        self.alert.enter_home()
        self.login.login_set(phone_num,code_num)
        self.login.assert_login(user_name)
#
#
lg=Case_login()
lg.case_login_success("18033084759","123456","QMYN_4759")