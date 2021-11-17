# -*- encoding=utf-8 -*-

from airtest.core.android.adb import *
from page import order_detail_page,secret_page,pay_success_page
path_log = os.getcwd() + r"\log"

class Case_makeOrder():
    def __init__(self):
        self.order_detail=order_detail_page.Order_detail_page()
        self.secret=secret_page.Secret_page()
        self.pay_success=pay_success_page.Pay_success_page()


    def case_makeOrder_success(self):
        self.order_detail.enter_goods_detail()
        self.order_detail.assert_goods_detail()
        self.order_detail.buy_goods()
        self.order_detail.assert_order_detail()
        self.order_detail.make_order()
        self.secret.pay_by_mCbBalance()
        self.secret.assert_secret_page()
        self.secret.set_secret()
        self.secret.assert_pay_success_page()
        self.pay_success.click_mTvOrderDetail()
        self.pay_success.assert_orderStatus_detail_page()
        self.pay_success.click_mLeftIv()

mo=Case_makeOrder()
mo.case_makeOrder_success()