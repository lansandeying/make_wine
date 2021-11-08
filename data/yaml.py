# coding:utf-8
import os
from ruamel import yaml
from lib import log

class Yaml():
    def __init__(self):
        self.log = log.MyLog()

    @staticmethod
    def read_yaml(file_name):
        # 获取当前脚本所在文件夹路径
        curPath = os.path.dirname(os.path.realpath(__file__))
        # 获取yaml文件路径
        yamlPath = os.path.join(curPath, file_name)
        # open方法打开直接读出来
        with open(yamlPath, 'r', encoding='utf-8') as f:
            d = yaml.load(f.read(), Loader=yaml.Loader)  # 用load方法转字典
            return d

    @staticmethod
    def write_yaml(file_name, data):
        curpath = os.path.dirname(os.path.realpath(__file__))
        yamlpath = os.path.join(curpath, file_name)

        # 写入到yaml文件
        with open(yamlpath, "w", encoding="utf-8") as f:
            yaml.dump(data, f, Dumper=yaml.RoundTripDumper,allow_unicode=True)

data = [(1, 2), (3, 4), (5, 6)]

dict={"url":"/login.do?phone=18033084759&passwd=123456","headers":{"shopId":"1000"},"data":{"name":"Tom","age":"30"}}
list_suc=[{"phone":"18033084759","passwd":"123456"},{"phone":"13000000010","passwd":"123123"},{"phone":"13000000011","passwd":"123123"}]
list_fail=[{"param":{"phone":"18033080000","passwd":"123456"},"msg":"找不到该用户名","code":"1000"},
            {"param":{"phone":"18033084759","passwd":"888888"},"msg":"密码错误","code":"1006"},
            {"param":{"phone":"00000","passwd":"123456"},"msg":"手机号码有误","code":"1000"},
            {"param":{"phone":"18033080000","passwd":""},"msg":"密码不许为空","code":"1000"}
           ]

dict_login={"url":"/login.do","headers":{"shopId":"1000"},"login_suc":list_suc,"login_fail":list_fail}

# write_yaml('case2.yaml', dict)
if __name__=="__main__":
    # lg =read_yaml("Login.yaml")
    # print(lg["url"])
    # print(lg["headers"])
    # print(lg["login"])
    # ya=Yaml.write_yaml("Login_data.yaml",dict_login)
    # lg = read_yaml("Login_data.yaml")
    # print(lg["login_fail"])
    ya=Yaml.read_yaml("devices")
    print(ya)
