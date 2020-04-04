from selenium import webdriver
import unittest
from pages.loginPage import LoginPage,loginUrl
import ddt
import time
'''打开cmd  pip install ddt 先安装再导入'''

'''
数据驱动
1.输入super009,输入admin 点击登录
2.输入hujiaojiao ，输入      点击登录
'''
# 测试数据源
testdates=[
    {"user":"输入super009","psw":"admin","expect":"super009"},
    {"user":"hujiaojiao","psw":"","expect":""}
]

@ddt.ddt
class LoinCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.login=LoginPage(cls.driver)
        cls.driver.get(loginUrl)

    def setUp(self):
        self.login.is_alert_exits()
        self.driver.delete_all_cookies()  # 退出登录
        self.driver.refresh()
        self.driver.get(loginUrl)


    def login_case(self,user,psw,expect):
         self.login.login(user,psw)
         time.sleep(3)
         result = self.login.get_login_name()
         print("获取的测试结果%s"% result)
         # self.assertTrue(result==expect)

    # 输入hujiaojiao, 输入hujj + 0557
    # 点击登录
    '''另外一种写法
  ddt.data(*testdates)
    '''
    @ddt.data({"user":"super009","psw":"admin","expect":"crm"},{"user":"hujiaojiao","psw":"","expect":""},
    )
    def test_01(self,data):
       print("----------开始测试--------------")
       print("测试数据:%s" % data)
       self.login_case(data["user"],data["psw"],data["expect"])
       print("----------结束测试:pass--------------")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
   unittest.main()

