# -*- encoding=utf-8 -*-
from airtest.core.api import *
import os
import traceback
from page import pay_page
from page import order_detail_page

path_log = os.getcwd() + r"\log"

class Secret_page(pay_page.Pay_page):
    def __init__(self):
        super().__init__()
        # 输入密码title
        self.mTitleTv = "com.lihui.winemaking:id/mTitleTv"
        # 返回按钮
        self.mLeftIv = "com.lihui.winemaking:id/mLeftIv"
        # 输入密码
        self.psdEditText = "com.lihui.winemaking:id/psdEditText"
        # 忘记密码
        self.mTvForgetPsd = "com.lihui.winemaking:id/mTvForgetPsd"
        # 确定按钮
        self.mTvConfirm = "com.lihui.winemaking:id/mTvConfirm"



    def click_mLeftIv(self):
        self.common.click_by_name(self.mLeftIv)

    def click_psdEditText(self):
        self.common.click_by_name(self.psdEditText)

    def click_mTvForgetPsd(self):
        self.common.click_by_name(self.mTvForgetPsd)

    def click_mTvConfirm(self):
        self.common.click_by_name(self.mTvConfirm)

    # 输入密码
    def set_secret(self,secret_num="190711"):
        try:
            self.click_psdEditText()
            for i in range(6):
                touch(Template(r"tpl1637054447828.png", record_pos=(-0.331, 0.577), resolution=(1080, 2340)))
            self.click_mTvConfirm()
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass


    # 断言进入输入密码页
    def assert_secret_page(self, value2="请输入支付密码"):
        try:
            text_value = self.common.get_attr_text(self.mTitleTv)
            self.common.assert_equal(text_value, value2, "进入输入密码页成功")
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass


if __name__ == "__main__":
    # 脚本初始化
    auto_setup(__file__, devices=[
        "android://127.0.0.1:5037/f8f4a508"],logdir=path_log)
        # "android://127.0.0.1:5037/emulator-5554"], logdir=path_log)
    # g = order_detail_page.Order_detail_page()
    # g.enter_goods_detail()
    # g.assert_goods_detail()
    # g.buy_goods()
    # g.assert_order_detail()
    # g.make_order()
    # g.assert_pay_page()
    #
    # p = Secret_page()
    # p.pay_by_mCbBalance()
    # p.assert_secret_page()
    s=Secret_page()
    s.set_secret()






