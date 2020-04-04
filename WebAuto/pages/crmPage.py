import time
from common.base import Base
from selenium import webdriver
from pages.loginPage import LoginPage,loginUrl

class CrmPage(Base):
    # 定位元素
    loc_new = ("xpath", "/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/a/button")
    loc_username=("xpath","/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div/div/form/div/div[1]/div/div/div/input")
    loc_phone=("xpath","/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div/div/form/div/div[2]/div/div/div/input")
    loc_ages=("xpath","/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div/div/form/div/div[6]/div/div/div/input")
    loc_khqd=("xpath","/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div/div/form/div/div[7]/div/div/div/div[1]/span/span/i")
    loc_save=("xpath","/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div/div/form/div/div[31]/div/div/button[1]/span")
    loc_khqd2=("xpath","/html/body/div[2]/div[1]/div[1]/ul/li[1]/span")


    def click_new(self):
        self.click(self.loc_new)

    def input_user(self, text="胡密码"):
        self.send_keys(self.loc_username, text)

    def input_phone(self, text="18067554323"):
        self.send_keys(self.loc_phone, text)

    def input_ages(self, text="11"):
        self.send_keys(self.loc_ages, text)

    def click_khqd(self):
        self.click(self.loc_khqd)
        self.click(self.loc_khqd2)

    def click_save(self):
        self.click(self.loc_save)

    def new_crm(self,username,phone,ages):
        # driver = webdriver.Firefox()
        self.driver.get(loginUrl)
        login = LoginPage(self.driver)
        login.login("", "")
        time.sleep(5)
        crm = CrmPage(self.driver)

        self.click_new()
        self.input_user(username)
        self.input_phone(phone)
        self.input_ages(ages)
        self.click_khqd()
        self.click_save()


if __name__=="__main__":
   driver=webdriver.Firefox()
   driver.get(loginUrl)
   login=LoginPage(driver)
   login.login("","")
   time.sleep(5)
   crm=CrmPage(driver)
   crm.click_new()
   crm.input_user("漂亮")
   crm.input_phone("17867667877")
   crm.input_ages("33")
   crm.click_khqd()
   crm.click_save()

