# -*- encoding=utf-8 -*-
from lib import common
from airtest.core.api import *
import os
import traceback
from page import goods_detail_page

path_log = os.getcwd() + r"\log"

class Order_detail_page(goods_detail_page.Goods_detail_page):
    def __init__(self):
        super().__init__()
        #个人收货信息模块
        self.mCLPerson="com.lihui.winemaking:id/mCLPerson"
        #确认订单title
        self.mTitleTv="com.lihui.winemaking:id/mTitleTv"
        #用户名称
        self.mTvUserName="com.lihui.winemaking:id/mTvUserName"
        #电话号码
        self.mTvUserPhone="com.lihui.winemaking:id/mTvUserPhone"
        #收货地址
        self.mTvUserAddress="com.lihui.winemaking:id/mTvUserAddress"
        #商品名称
        self.mTvGoodName="com.lihui.winemaking:id/mTvGoodName"
        #商品规格
        self.mTvSpec="com.lihui.winemaking:id/mTvSpec"
        #商品权益周期
        self.mTvPeriod="com.lihui.winemaking:id/mTvPeriod"
        #商品金额
        self.mTvGoodPrice="com.lihui.winemaking:id/mTvGoodPrice"
        #商品个数
        self.mTvCount="com.lihui.winemaking:id/mTvCount"
        #商品津贴
        self.mTvRewardMoney="com.lihui.winemaking:id/mTvRewardMoney"
        #购买协议
        self.mTvAgreement="com.lihui.winemaking:id/mTvAgreement"
        #勾选协议
        self.mCbAgreement="com.lihui.winemaking:id/mCbAgreement"
        #合计金额
        self.mTvTotalMoney="com.lihui.winemaking:id/mTvTotalMoney"
        #确认订单
        self.mTvPlaceOrder="com.lihui.winemaking:id/mTvPlaceOrder"
        
        #立即支付
        self.mTvBuyNow="com.lihui.winemaking:id/mTvBuyNow"

    def click_mCLPerson(self):
        self.common.click_by_name(self.mCLPerson)

    def click_mCbAgreement(self):
        self.common.click_by_name(self.mCbAgreement)

    def click_mTvPlaceOrder(self):
        self.common.click_by_name(self.mTvPlaceOrder)

    def make_order(self):
        try:
            self.click_mCbAgreement()
            self.click_mTvPlaceOrder()
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass

    def assert_pay_page(self, value2="立即支付"):
        try:
            text_value = self.common.get_attr_text(self.mTvBuyNow)
            self.common.assert_equal(text_value, value2, "进入支付订单页成功")
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass

if __name__=="__main__":
    # 脚本初始化
    auto_setup(__file__, devices=[
        "android://127.0.0.1:5037/emulator-5554?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH"],
               logdir=path_log)
    g=Order_detail_page()
    g.enter_goods_detail()
    g.assert_goods_detail()
    g.buy_goods()
    g.assert_order_detail()
    g.make_order()

    
    
    