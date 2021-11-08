#coding = utf-8
from lib import common
from conf import setting
from lib import log

class Alert_page():
    def __init__(self):
        self.log=log.MyLog()
        self.common=common.Common()
        self.app_name=setting.app_name
        #不同意按钮
        self.disagree="com.lihui.winemaking:id/tvDisagree"
        #同意按钮
        self.agree="com.lihui.winemaking:id/tvAgree"
        #同意关闭
        self.close="com.lihui.winemaking:id/tvClose"

    #点击不同意
    def click_disagree(self):
        self.common.click_by_name(self.disagree)

    #点击同意
    def click_agree(self):
        self.common.click_by_name(self.agree)

    #点击关闭
    def click_close(self):
        self.common.click_by_name(self.close)

    #首次进入APP不同意协议点击退出
    def close_app(self):
        try:
            self.common.clear_app(self.app_name)
            self.common.star_app(self.app_name)
            self.click_disagree()
            self.click_close()
        except Exception as msg:
            self.log.error("s%"%msg)
        finally:
            pass

    #进入首页
    def enter_home(self):
        try:
            self.common.clear_app(self.app_name)
            self.common.star_app(self.app_name)
            self.click_agree()
        except Exception as msg:
            self.log.error("s%" % msg)
        finally:
            pass


if __name__=="__main__":
    pass

