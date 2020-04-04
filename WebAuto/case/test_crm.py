from selenium import webdriver
import unittest
from pages.crmPage import CrmPage
import ddt
import time
from pages.loginPage import LoginPage,loginUrl
'''
数据驱动
1.输入漂亮2,输入17899009899，输入23  选择客户渠道 点击保存
2.
'''
# 测试数据源
testdates=[
    {"username":"漂亮2","phone":"17899009899","ages":"23"}
]
@ddt.ddt
class CrmCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        # cls.login=LoginPage(cls.driver)
        # cls.driver.get(loginUrl)
        # cls.login.login("", "")
        cls.crm=CrmPage(cls.driver)


    def setUp(self):
        # self.login.is_alert_exits()
        self.driver.delete_all_cookies()  # 退出登录
        self.driver.refresh()
        # self.driver.get(loginUrl)


   # 新增crm信息
    def add_crm_case(self,username,phone,ages):
         self.crm.new_crm(username,phone,ages)
         print("添加成功")

    # 输入hujiaojiao, 输入hujj + 0557
    # 点击登录
    '''另外一种写法
  ddt.data(*testdates)
    '''
    @ddt.data({"username":"嘟嘟陈","phone":"17898996543","ages":"45"}
    )
    def test_01(self,data):
       print("----------开始测试--------------")
       print("测试数据:%s" % data)
       self.add_crm_case(data["username"],data["phone"],data["ages"])
       print("----------结束测试:pass--------------")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()


