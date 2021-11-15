# -*- encoding=utf-8 -*-
from lib import common
from airtest.core.api import *
import os
import traceback
from page import home_page

path_log = os.getcwd() + r"\log"



class Goods_detail_page(home_page.Home_page):
    def __init__(self):
        super().__init__()
        #商品封面图
        self.goods_banner="android.view.View"
        #商品价格
        self.goods_price="com.lihui.winemaking:id/mTvGoodPrice"
        #商品销量
        self.goods_sales="com.lihui.winemaking:id/tvSalesVolume"
        #商品名称
        self.goods_name="com.lihui.winemaking:id/mTvGoodName"
        #点击购买
        self.buy="com.lihui.winemaking:id/mTvBuyNow"


    def click_goods_banner(self):
        self.common.click_by_name(self.goods_banner)

    def click_goods_price(self):
        self.common.click_by_name(self.goods_price)

    def click_goods_sales(self):
        self.common.click_by_name(self.goods_sales)

    def click_goods_name(self):
        self.common.click_by_name(self.goods_name)

    def click_buy(self):
        self.common.click_by_name(self.buy)

    def login_set(self):
        try:
            self.click_buy()
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass

    def assert_goods_detail(self, value2="立即购买"):
        try:
            text_value = self.common.get_attr_text(self.buy)
            self.common.assert_equal(text_value, value2, "进入商品详情成功")
        except Exception as msg:
            traceback.print_exc("进入商品详情失败")
        finally:
            pass