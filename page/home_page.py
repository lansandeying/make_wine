#coding = utf-8
from lib import common
from conf import setting
from lib import log

class Home_page():
    def __init__(self):
        self.log = log.MyLog()
        self.common = common.Common()
        #��ҳ�˵���
        self.home = "com.lihui.winemaking:id/tlIcon"
        #�����н�
        self.share = "com.lihui.winemaking:id/ivInviteReward"
        #��������
        self.download = "com.lihui.winemaking:id/ivOrderGift"
        #��Ʒ
        self.goods = "com.lihui.winemaking:id/ivProduct"

    def click_home(self):
        self.common.click_by_name(self.home)

    def click_share(self):
        self.common.click_by_name(self.share)

    def click_download(self):
        self.common.click_by_name(self.download)

    def click_goods(self):
        self.common.click_by_nams(self.goods)

    