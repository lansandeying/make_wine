# -*- encoding=utf-8 -*-
from lib import common
import traceback

class Home_page():
    def __init__(self):
        self.common = common.Common()
        #首页菜单栏
        self.home = "com.lihui.winemaking:id/tlIcon"
        #邀请有奖
        self.share = "com.lihui.winemaking:id/ivInviteReward"
        #下载有礼
        self.download = "com.lihui.winemaking:id/ivOrderGift"
        #商品
        self.goods = "com.lihui.winemaking:id/ivProduct"
        
        #点击购买
        self.buy="com.lihui.winemaking:id/mTvBuyNow"

    def click_home(self):
        self.common.click_by_name(self.home)

    def click_share(self):
        self.common.click_by_name(self.share)

    def click_download(self):
        self.common.click_by_name(self.download)

    def click_goods(self):
        self.common.click_by_nams(self.goods,1)
        
    def click_buyNow(self):
        self.common.click_by_name(self.buyNow)

    #点击进入商品详情
    def enter_goods_detail(self):
        try:
            self.click_home()
            self.click_goods()
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass
    #遍历商品详情
    def check_goods_detail(self):
        try:
            for i in range(2):
                self.common.click_by_nams(self.goods, i)
                self.common.back()
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass

    def assert_goods_detail(self, value2="立即购买"):
        try:
            text_value = self.common.get_attr_text(self.buy)
            self.common.assert_equal(text_value, value2, "进入商品详情成功")
        except Exception as msg:
            traceback.print_exc()
        finally:
            pass


    
