# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android.recorder import *
from airtest.core.android.adb import *
import os

path_log = os.getcwd() + r"\log"


def now_Time(doing):
    print(doing + time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()))


# 脚本初始化
auto_setup(__file__, devices=[
    "android://127.0.0.1:5037/f8f4a508?cap_method=JAVACAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH"],
           logdir=path_log)


def click_by_name(name_value):
    try:
        poco(name=name_value).wait_for_appearance()
    except Exception as msg:
        print("%s" % msg)
    else:
        poco(name=name_value).click()


def click_by_text(text_value):
    try:
        poco(text=text_value).wait_for_appearance()
    except Exception as msg:
        print("%s" % msg)
    else:
        poco(text=text_value).click()


def swipe_by_name_up(name_value):
    try:
        poco(name=name_value).wait_for_appearance()
    except Exception as msg:
        print("%s" % msg)
    else:
        poco(name=name_value).swipe('up')


def swipe_by_name_down(name_value):
    try:
        poco(name=name_value).wait_for_appearance()
    except Exception as msg:
        print("%s" % msg)
    else:
        poco(name=name_value).swipe('down')


def swipe_up():
    poco.swipe([0.5, 0.9], [0.5, 0.1])


def swipe_down():
    poco.swipe([0.5, 0.1], [0.5, 0.9])


def enter_wine():
    # 点击不同意
    #     now_Time("Disagree")
    #     click_by_name("com.lihui.winemaking:id/tvDisagree")
    #     sleep(1.0)
    # 点击关闭应用
    #     now_Time("tvClose")
    #     click_by_name("com.lihui.winemaking:id/tvClose")
    #     sleep(1.0)
    # 重新打开APP
    #     start_app("com.lihui.winemaking")
    # 点击同意
    now_Time("tvAgree")
    click_by_name("com.lihui.winemaking:id/tvAgree")
    sleep(1.0)
    # 获取控件的“text”属性值
    value = poco("com.lihui.winemaking:id/tlText").attr("text")
    assert_equal(value, "首页", "进入首页成功")
    assert_not_equal()


def login():
    # 点击我的
    now_Time("my")
    poco(name="com.lihui.winemaking:id/tlIcon")[1].click()
    sleep(1.0)
    # 点击登录
    now_Time("login")
    click_by_name("com.lihui.winemaking:id/mTvUserName")
    sleep(1.0)
    # 勾选协议
    click_by_name("com.lihui.winemaking:id/mCbAgreement")
    sleep(1.0)
    # 点击账号且输入
    click_by_name("com.lihui.winemaking:id/etPhone")
    text("13510677061")
    sleep(1.0)
    # 点击获取验证码
    click_by_name("com.lihui.winemaking:id/tvGetCode")
    sleep(1.0)
    # 点击验证码且输入
    click_by_name("com.lihui.winemaking:id/etCode")
    text("123456")
    sleep(1.0)
    # 点击登录
    click_by_name("com.lihui.winemaking:id/tvLogin")
    sleep(1.0)


def list_check():
    now_Time("shouye")
    # 点击首页
    poco(name="com.lihui.winemaking:id/tlIcon").click()
    # 点击邀请有奖
    now_Time("ivInviteReward")
    click_by_name("com.lihui.winemaking:id/ivInviteReward")
    sleep(1.0)
    keyevent("BACK")
    # 点击下载有礼
    now_Time("ivOrderGift")
    click_by_name("com.lihui.winemaking:id/ivOrderGift")
    sleep(1.0)
    keyevent("BACK")
    # 向上滑动商品列表
    now_Time("list_refresh_down")
    for i in range(4):
        swipe_up()


def check_goods():
    # 点击首页
    click_by_name("com.lihui.winemaking:id/tlIcon")
    # 回到初始点
    now_Time("list_refresh_up")
    for b in range(4):
        swipe_down()
    sleep(1.0)
    # 循环点击商品名
    now_Time("goods_detail")
    goods = poco(name="com.lihui.winemaking:id/ivProduct")
    for i in range(4):
        goods[i].click()
        keyevent("BACK")


def check_order():
    # 点击我的
    poco("com.lihui.winemaking:id/tlIcon")[1].click()
    # 点击我的订单
    now_Time("order_list")
    click_by_name("com.lihui.winemaking:id/mTvMyOrder")
    # 遍历订单状态
    now_Time("order_status")
    order = poco(name="android.widget.TextView")
    for i in range(5):
        order[i].click()
    # 回到我的
    keyevent("BACK")


def user_message():
    # 点击我的
    poco("com.lihui.winemaking:id/tlIcon")[1].click()
    # 点击提货
    now_Time("pick_list")
    click_by_text("提货")
    sleep(1.0)
    keyevent("BACK")
    # 点击地址管理
    now_Time("address")
    click_by_text("地址管理")
    sleep(1.0)
    keyevent("BACK")
    # 点击银行卡管理
    now_Time("bank_card")
    click_by_text("银行卡管理")
    sleep(1.0)
    keyevent("BACK")
    # 点击常见问题
    now_Time("questions")
    click_by_text("常见问题")
    sleep(1.0)
    keyevent("BACK")


def about_us():
    # 点击我的
    poco("com.lihui.winemaking:id/tlIcon")[1].click()
    # 点击关于我们
    click_by_text("关于我们")
    # 点击全民优酿隐私权协议
    now_Time("secret_company")
    click_by_text("全民优酿隐私权协议")
    sleep(1.0)
    for i in range(5):
        swipe_up()
    keyevent("BACK")
    # 点击全面全民优酿用户协议
    now_Time("secret_user")
    click_by_text("全民优酿用户协议")
    sleep(1.0)
    for i in range(5):
        swipe_up()
    keyevent("BACK")


def check_account():
    # 点击我的
    poco("com.lihui.winemaking:id/tlIcon")[1].click()
    # 点击账户
    now_Time("account")
    click_by_name("com.lihui.winemaking:id/mClMoney")
    sleep(1.0)
    # 点击提示
    click_by_name("com.lihui.winemaking:id/ivTip")
    sleep(1.0)
    keyevent("BACK")
    # 点击提现
    now_Time("drawing")
    click_by_name("com.lihui.winemaking:id/tvWithDraw")
    sleep(1.0)
    keyevent("BACK")
    # 点击账户充值
    now_Time("top_up")
    click_by_name("com.lihui.winemaking:id/tvWithCharge")
    sleep(1.0)
    keyevent("BACK")
    # 点击账户明细
    now_Time("account_log")
    click_by_name("com.lihui.winemaking:id/tvDetailAccount")
    sleep(1.0)
    keyevent("BACK")
    # 点击津贴
    now_Time("jintie")
    click_by_name("com.lihui.winemaking:id/tvDetailSpread")
    sleep(1.0)
    keyevent("BACK")
    # 点击推荐津贴
    now_Time("tuijian_jintie")
    click_by_name("com.lihui.winemaking:id/tvDetailInvite")
    sleep(1.0)
    keyevent("BACK")
    # 点击品鉴奖励
    now_Time("jiangli")
    click_by_name("com.lihui.winemaking:id/tvDetailTicheng")
    sleep(1.0)
    keyevent("BACK")
    # 点击提现记录
    now_Time("drawing_log")
    click_by_name("com.lihui.winemaking:id/tvDetailWithdraw")
    sleep(1.0)
    keyevent("BACK")
    # 返回我的列表
    keyevent("BACK")


try:
    # 初始化Android对应的poco驱动
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    # 开启录屏
    adb = ADB(serialno="f8f4a508")
    recorder = Recorder(adb)
    recorder.start_recording()

    # 重启应用，保证初始化状态一致
    clear_app("com.lihui.winemaking")
    start_app("com.lihui.winemaking")

    # 执行用例
    enter_wine()
    login()
    list_check()
    check_goods()
    check_account()
    check_order()
    user_message()
    about_us()

    # 结束录屏
    recorder.stop_recording(output=path_log + r"\wine.mp4")

finally:
    simple_report(__file__, logpath=path_log, output=path_log + r"\log.html")