import time
from common.base import Base
from selenium import webdriver
import  unittest

loginUrl="http://saastys.test.tangyisheng.com.cn/#/login"
class LoginPage(Base):
    # driver=webdriver.Firefox()
    # 定位登录  获取页面上所有的元素
    loc_user = ("xpath", "/html/body/div[1]/div/div/form/div[1]/div/div/input")
    loc_pwd = ("xpath", "/html/body/div[1]/div/div/form/div[2]/div/div/input")
    loc_submit = ("xpath", "/html/body/div[1]/div/div/form/div[3]/button")
    loc_loginUsername=("id","crm")

    # def __init__(self,driver:webdriver.Firefox):
    #     self.driver=driver
    #     loc_user_name=

    def input_user(self,text=""):
        self.send_keys(self.loc_user,text)

    def input_pwd(self,text=""):
        self.send_keys(self.loc_pwd,text)

    def click_login_button(self):
        self.click(self.loc_submit)

    def clear_user(self):
        self.clear(self.loc_user)
        self.clear(self.loc_pwd)

    def get_currentUrl(self):
        url=self.url_contains2("basic1")
        print(url)
        return url
        # currentUrl= driver.current_url
        # print(currentUrl)
        # self.assertTrue(currentUrl=="http://saastys.test.tangyisheng.com.cn/#/basic1")
        # return currentUrl
   # 判断是否登录成功
    def get_login_name(self):
        # locuser= driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div/div[4]/span").text
        user=self.is_title(self.loc_loginUsername)
        print(user)
        return user

        # 判断是否有弹出框
    def is_alert_exits(self):
        try:
            time.sleep(3)
            alert=self.driver.switch_to.alert
            text=alert.text
            alert.accept()
            print(text)
            return text
        except:
            return ""

    def login(self,user,psw):

        time.sleep(3)
        # self.input_user(user)
        # self.input_pwd(psw)
        self.click_login_button()

if __name__=="__main__":
    driver=webdriver.Firefox()
    driver.get(loginUrl)
    loginpage = LoginPage(driver)
    loginpage.input_user("")
    loginpage.input_pwd("")
    loginpage.click_login_button()
    time.sleep(3)
    url=loginpage.get_currentUrl()
    print(url)
    # loginpage.get_login_name()
    # loginpage.is_alert_exits()
    print("2323s")
    # loginpage.login("super009","admin")