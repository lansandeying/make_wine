# -*- encoding=utf-8 -*-
from lib import common
from airtest.core.api import *
import os
import traceback
from page import order_detail_page

path_log = os.getcwd() + r"\log"

class Pay_page():
    def __init__(self):
        self.common = common.Common()
        #支付订单title
        self.mTitleTv="com.lihui.winemaking:id/mTitleTv"
        #支付金额
        self.mTvPrice="com.lihui.winemaking:id/mTvPrice"
        #订单编号
        self.mTvOrderNo="com.lihui.winemaking:id/mTvOrderNo"
        #订单总计
        self.mTvOrderPrice="com.lihui.winemaking:id/mTvOrderPrice"
        #可用余额
        self.mTvBalance="com.lihui.winemaking:id/mTvBalance"
        #账户充值
        self.mTvOfflineCharge="com.lihui.winemaking:id/mTvOfflineCharge"
        #勾选余额支付
        self.mCbBalance="com.lihui.winemaking:id/mCbBalance"
        #勾选微信支付
        self.mCbWePay="com.lihui.winemaking:id/mCbWePay"
        #立即支付
        self.mTvBuyNow="com.lihui.winemaking:id/mTvBuyNow"
        
        #点击返回
        self.mLeftIv="com.lihui.winemaking:id/mLeftIv"
        #放弃
        self.tvCancel="com.lihui.winemaking:id/tvCancel"
        #继续支付
        self.tvConfirm="com.lihui.winemaking:id/tvConfirm"
        #放弃支付进入订单列表页,标题为"订单"
        self.mTitleTv="com.lihui.winemaking:id/mTitleTv"
        
        #支付密码页title
        self.mTitleTv="com.lihui.winemaking:id/mTitleTv"
        

    def click_mTvOfflineCharge(self):
        self.common.click_by_name(self.mTvOfflineCharge)

    def click_mCbBalance(self):
        self.common.click_by_name(self.mCbBalance)

    def click_mCbWePay(self):
        self.common.click_by_name(self.mCbWePay)

    def click_mTvBuyNow(self):
        self.common.click_by_name(self.mTvBuyNow)

    #余额支付    
    def pay_by_mCbBalance(self):
        try:
            self.click_mCbBalance()
            self.click_mTvBuyNow()
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass

    #微信支付
    def pay_by_mCbWePay(self):
        try:
            self.click_mCbWePay()
            self.click_mTvBuyNow()
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass

    #断言进入输入密码页
    def assert_secret_page(self, value2="请输入支付密码"):
        try:
            text_value = self.common.get_attr_text(self.mTitleTv)
            self.common.assert_equal(text_value, value2, "进入输入密码页成功")
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass



if __name__=="__main__":
    # 脚本初始化
    auto_setup(__file__, devices=[
        "android://127.0.0.1:5037/emulator-5554?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH"],
               logdir=path_log)
    g = order_detail_page.Order_detail_page()
    g.enter_goods_detail()
    g.assert_goods_detail()
    g.buy_goods()
    g.assert_order_detail()
    g.make_order()
    g.assert_pay_page()

    p = Pay_page()
    p.pay_by_mCbBalance()
    p.assert_secret_page()   



