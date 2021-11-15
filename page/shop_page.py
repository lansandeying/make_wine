# -*- encoding=utf-8 -*-
from lib import common
from airtest.core.api import *
import os
import traceback

path_log = os.getcwd() + r"\log"

class Goods_detail_page():
    def __init__(self):
        self.common = common.Common()
        #点击首页
        self.home="com.lihui.winemaking:id/tlIcon"
        #点击商品
        self.goods="com.lihui.winemaking:id/ivProduct"
        #商品封面图
        self.goods_banner="android.view.View"
        #商品价格
        self.goods_price="com.lihui.winemaking:id/mTvGoodPrice"
        #商品销量
        self.goods_sales="com.lihui.winemaking:id/tvSalesVolume"
        #商品名称
        self.goods_name="com.lihui.winemaking:id/mTvGoodName"
        #点击购买
        self.login="com.lihui.winemaking:id/mTvBuyNow"


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