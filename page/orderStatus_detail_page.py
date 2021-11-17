# -*- encoding=utf-8 -*-
from airtest.core.api import *
import os
import traceback
from page import pay_page
from page import order_detail_page
import time
from lib import common

path_log = os.getcwd() + r"\log"

class OrderStatus_detail_page():
    def __init__(self):
        self.common = common.Common()        
        # 返回按钮
        self.mLeftIv = "com.lihui.winemaking:id/mLeftIv"
        # 订单状态
        self.tvOrderStatus = "com.lihui.winemaking:id/tvOrderStatus"
        # 提货记录
        self.tvPickUpRecord = "com.lihui.winemaking:id/tvPickUpRecord"
        # 收货人
        self.tvAddressName = "com.lihui.winemaking:id/tvAddressName"
        # 收货人手机号
        self.ivAddressPhone = "com.lihui.winemaking:id/ivAddressPhone"
        # 收获人地址
        self.tvAddressDetail = "com.lihui.winemaking:id/tvAddressDetail"
        # 商品名称
        self.tvGoodsName = "com.lihui.winemaking:id/tvGoodsName"
        # 商品规格
        self.tvSpec = "com.lihui.winemaking:id/tvSpec"
        # 订单权益周期
        self.tvCycle = "com.lihui.winemaking:id/tvCycle"
        # 订单份数
        self.tvQuantity = "com.lihui.winemaking:id/tvQuantity"
        # 订单金额
        self.tvPrice = "com.lihui.winemaking:id/tvPrice"
        # 订单支付金额
        self.tvMoney = "com.lihui.winemaking:id/tvMoney"
        # 订单编号
        self.tvOrderNoValue = "com.lihui.winemaking:id/tvOrderNoValue"
        # 下单时间
        self.tvOrderTimeValue = "com.lihui.winemaking:id/tvOrderTimeValue"
        # 支付方式
        self.tvOrderPayTypeValue = "com.lihui.winemaking:id/tvOrderPayTypeValue"
        # 支付时间
        self.tvOrderPayTimeValue = "com.lihui.winemaking:id/tvOrderPayTimeValue"
        # 支付金额
        self.tvOrderPayMoneyValue = "com.lihui.winemaking:id/tvOrderPayMoneyValue"
        # 查看购买协议
        self.tvCheckBuyProtocol = "com.lihui.winemaking:id/tvCheckBuyProtocol"
        # 剩余可以数量
        self.tvRemainQuantityValue = "com.lihui.winemaking:id/tvRemainQuantityValue"
        # 提货
        self.tvOrderPickUp = "com.lihui.winemaking:id/tvOrderPickUp"
    #点击返回    
    def click_mLeftIv(self):
        self.common.click_by_name(self.mLeftIv)
    #点击提货记录    
    def click_tvPickUpRecord(self):
        self.common.click_by_name(self.tvPickUpRecord)
    #点击查看购买协议
    def click_tvCheckBuyProtocol(self):
        self.common.click_by_name(self.tvCheckBuyProtocol)
    #点击提货    
    def click_tvOrderPickUp(self):
        self.common.click_by_name(self.tvOrderPickUp)
        
        
        