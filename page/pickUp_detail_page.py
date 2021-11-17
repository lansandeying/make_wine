# -*- encoding=utf-8 -*-
from airtest.core.api import *
import os
import traceback
from page import pay_page
from page import order_detail_page
import time
from lib import common

path_log = os.getcwd() + r"\log"

class PickUp_detail_page():
    def __init__(self):
        self.common = common.Common()        
        # 返回按钮
        self.mLeftIv = "com.lihui.winemaking:id/mLeftIv"
        # 提货订单状态
        self.tvOrderStatus = "com.lihui.winemaking:id/tvOrderStatus"
        # 收货人姓名
        self.tvRecipient = "com.lihui.winemaking:id/tvRecipient"
        # 收货人手机号
        self.tvPhone = "com.lihui.winemaking:id/tvPhone"
        # 收货人地址
        self.tvAddress = "com.lihui.winemaking:id/tvAddress"
        # 提货商品名称
        self.tvGoodsName = "com.lihui.winemaking:id/tvGoodsName"
        # 商品规格
        self.tvSpecValue = "com.lihui.winemaking:id/tvSpecValue"
        # 订单份数
        self.tvQuantity = "com.lihui.winemaking:id/tvQuantity"
        # 订单金额
        self.tvPrice = "com.lihui.winemaking:id/tvPrice"
        # 提货数量
        self.tvPickQtyValue = "com.lihui.winemaking:id/tvPickQtyValue"
        # 提货订单编号
        self.tvOrderNoValue = "com.lihui.winemaking:id/tvOrderNoValue"
        # 提货单号
        self.tvPickUpNoValue = "com.lihui.winemaking:id/tvPickUpNoValue"
        # 提货时间
        self.tvPickUpTimeValue = "com.lihui.winemaking:id/tvPickUpTimeValue"
        # 取消提货/是否取消提货-返回
        self.tvCancel = "com.lihui.winemaking:id/tvCancel"
        # 是否取消提货-确定
        self.tvConfirm = "com.lihui.winemaking:id/tvConfirm"
        
    def click_mLeftIv(self):
        self.common.click_by_name(self.mLeftIv)
        
    def click_tvCancel(self):
        self.common.click_by_name(self.tvCancel)
        
    def click_tvConfirm(self):
        self.common.click_by_name(self.tvConfirm)
        
        
        
        
        
        
        
        
        