#coding = utf-8
from lib import common
from conf import setting
from lib import log

class Alert_page():
    def __init__(self):
        self.log=log.MyLog()
        self.common=common.Common()
        self.app_name=setting.app_name
        #��ͬ�ⰴť
        self.disagree="com.lihui.winemaking:id/tvDisagree"
        #ͬ�ⰴť
        self.agree="com.lihui.winemaking:id/tvAgree"
        #ͬ��ر�
        self.close="com.lihui.winemaking:id/tvClose"

    #�����ͬ��
    def click_disagree(self):
        self.common.click_by_name(self.disagree)

    #���ͬ��
    def click_agree(self):
        self.common.click_by_name(self.agree)

    #����ر�
    def click_close(self):
        self.common.click_by_name(self.close)

    #�״ν���APP��ͬ��Э�����˳�
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

    #������ҳ
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

