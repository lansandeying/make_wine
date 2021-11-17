# -*- encoding=utf-8 -*-
from airtest.core.api import *
import os
import traceback
from page import pay_page
from page import order_detail_page
import time
from lib import common

path_log = os.getcwd() + r"\log"

class Pay_success_page():
    def __init__(self):
        self.common = common.Common()
        # 支付成功title
        self.mTitleTv = "com.lihui.winemaking:id/mTitleTv"
        # 返回按钮
        self.mLeftIv = "com.lihui.winemaking:id/mLeftIv"
        # 支付成功提示
        self.mTvTimer = "com.lihui.winemaking:id/mTvTimer"
        # 合同金额
        self.mTvMoney = "com.lihui.winemaking:id/mTvMoney"
        # 订单编号
        self.mTvOrderNum = "com.lihui.winemaking:id/mTvOrderNum"
        # 查看提货订单
        self.mTvGoodsOrder = "com.lihui.winemaking:id/mTvGoodsOrder"
        # 查看订单
        self.mTvOrderDetail = "com.lihui.winemaking:id/mTvOrderDetail"
        
        # 订单/提货详情页订单状态
        self.tvOrderStatus = "com.lihui.winemaking:id/tvOrderStatus"
        

    # 点击返回按钮
    def click_mLeftIv(self):
        self.common.click_by_name(self.mLeftIv)
    # 点击查看提货订单
    def click_mTvGoodsOrder(self):
        self.common.click_by_name(self.mTvGoodsOrder)
    # 点击查看订单
    def click_mTvOrderDetail(self):
        self.common.click_by_name(self.mTvOrderDetail)


    # 断言进入订单详情页
    def assert_orderStatus_detail_page(self, value2="权益期"):
        time.sleep(5)
        try:
            text_value = self.common.get_attr_text(self.tvOrderStatus)
            self.common.assert_equal(text_value, value2, "进入订单详情页成功")
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass
        
    # 断言进入提货详情页
    def assert_pickUp_detail_Status_page(self, value2="待发货"):
        time.sleep(5)
        try:
            text_value = self.common.get_attr_text(self.tvOrderStatus)
            self.common.assert_equal(text_value, value2, "进入提货详情页成功")
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass


if __name__ == "__main__":
    # 脚本初始化
    auto_setup(__file__, devices=[
        "android://127.0.0.1:5037/f8f4a508"],logdir=path_log)









