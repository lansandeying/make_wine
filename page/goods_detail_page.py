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
        #减少
        self.reduce="com.lihui.winemaking:id/mImgReduce"
        #增加
        self.add="com.lihui.winemaking:id/mImgAdd"
        #输入数字
        self.etAmount="com.lihui.winemaking:id/etAmount"
        #点击立即购买
        self.buyNow="com.lihui.winemaking:id/mTvBuyNow"
        
        #确认订单
        self.mTvPlaceOrder="com.lihui.winemaking:id/mTvPlaceOrder"

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
    
    def click_reduce(self):
        self.common.click_by_name(self.reduce)
        
    def click_add(self):
        self.common.click_by_name(self.add)
        
    def click_etAmount(self):
        self.common.click_by_name(self.etAmount)
        
    def click_buyNow(self):
        self.common.click_by_name(self.buyNow)
        
    def buy_goods(self):
        try:
            self.click_buy()
            for i in range(3):                
                self.click_add()
            for i in range(2):  
                self.click_reduce()
            self.click_buyNow()
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass
        
    def assert_order_detail(self, value2="确认订单"):
        try:
            text_value = self.common.get_attr_text(self.mTvPlaceOrder)
            self.common.assert_equal(text_value, value2, "进入确认订单页成功")
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass


if __name__=="__main__":
    # 脚本初始化
    auto_setup(__file__, devices=[
        "android://127.0.0.1:5037/emulator-5554?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH"],
               logdir=path_log)
    g=Goods_detail_page()
    
