# 二次封装类，用于获取元素定位的封装
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Base():

    def __init__(self,driver:webdriver.Firefox):
        self.driver=driver
        self.timeout=3
        self.t=1

   #element是元素自身，localor是元素定位
        # 新的定位方法和下面的一样
    def findElementNew(self,locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传入元祖类型：loc=（"id","value1"）')
        else:
            print("正确定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            # 定位到元素，返回元素对象，没有定位到元素，抛出异常
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele

    def findElement(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传入元祖类型：loc=（"id","value1"）')
        else:
            print("正确定位元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1]))
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElements(self,locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传入元祖类型：loc=（"id","value1"）')
        else:
            print("正确定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_elements(*locator))
            return ele

    def send_keys(self,locator,text):
        ele=self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator: object) -> object:
        ele = self.findElement(locator)
        ele.click()

    def submit(self, locator: object) -> object:
        ele = self.findElement(locator)
        ele.submit()


    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        # 判断元素是否被选中，返回bool值
        ele=self.findElement(locator)
        r=ele.is_selected()
        return r

    def isElementExist(self,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self,locator):
        eles=self.findElements(locator)
        n=len(eles)
        if n==0:
            return False
        elif n==1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def is_title(self,_title):
        # 判断定位的元素与期望的结果值是否匹配，返回true false
        try:
           result= WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
           return result
        except:
           return False

    def is_title_contains(self, _title):
        # 判断定位的元素是否包含期望的值，返回true false
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def url_contains2(self,url):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.url_contains(url))
            return result
        except:
            return False


    def is_alert(self):
        # 判断alert是否存在，存在返回alert对象，不存在返回FALSE
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.alert_is_present())
            return result
        except:
            return False


    def is_presence_element_located(self,locator):
        # 判断某个元素是否被加入到了DOM树中
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return result
        except:
            return False

    def is_visibility_element_located(self, locator):
        # 判断某个元素是是否可见，可见代表元素非隐藏，并且元素的宽高都不等于0
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.visibility_of_element_located(locator))
            return result
        except:
            return False

    def is_visibility_of(self, locator):
        # 这个方法与上一个方法相同，区别：上面的方法传入local，这个方法直接传定位到的element
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.visibility_of(locator))
            return result
        except:
            return False

    def is_presence_of_all_elements_located(self, locator):
        # 判断是否有一个元素存在dom中
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.presence_of_all_elements_located(locator))
            return result
        except:
            return False

    def is_text_to_be_present_in_element(self, locator,_text):
        # 判断某个元素中的TEXT是否包含了预期的字符串
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_text_to_be_present_in_element_value(self, locator, _text):
        # 判断某个元素中的TEXT是否包含了预期的字符串
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, _text))
            return result
        except:
            return False



    def is_frame_to_be_ava_and_switch_to_it(self, locator):
        # 判断该frame是否可以switch进去，如果可以的话返回true并switch进去，否则返回false
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.frame_to_be_available_and_switch_to_it(locator))
            return result
        except:
            return False

    def is_invisibility_of_element_located(self, locator):
        # 判断某个元素是否不存在DOM中或者不可见
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.invisibility_of_element_located(locator))
            return result
        except:
            return False

    def is_element_to_be_clickable(self, locator):
        # 判断某个元素中是否可见并且是enable的，这样的话才叫clickable
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.element_to_be_clickable(locator))
            return result
        except:
            return False

    def is_staleness_of(self, locator):
        # 等某个元素是否从dom中移除，返回true false
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.staleness_of(locator))
            return result
        except:
            return False

    def is_element_to_be_selected(self, locator):
        # 判断某个元素是否被选中了，一般用在select下拉框，返回true false
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.element_to_be_selected(locator))
            return result
        except:
            return False

    def is_element_selection_state_to_be(self, locator):
        # 判断某个元素的选中状态是否符合预期
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.element_selection_state_to_be(locator))
            return result
        except:
            return False

            # class element_selection_state_to_be(object):
            #     """ An expectation for checking if the given element is selected.
            #     element is WebElement object
            #     is_selected is a Boolean."
            #     """
            #
            #     def __init__(self, element, is_selected):
            #         self.element = element
            #         self.is_selected = is_selected
            #
            #     def __call__(self, ignored):
            #         return self.element.is_selected() == self.is_selected

    def is_element_located_selection_state_to_be(self, locator):
                # 跟上面的方法一样，区别：上面传入定位到的element，而这个方法传入的是local
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.element_located_selection_state_to_be(locator))
            return result
        except:
            return False



    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele=self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引第几个，从0开始，默认选第一个'''
        element=self.findElement(locator) #定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        element=self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过文本定位'''
        element=self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def js_scroll_end(self,x=0):
        '''滚动到底部'''
        js_heig="window.scrollTo(0,document.body.scrollHeight)"%x
        self.driver.execute_script(js_heig)

    def js_focus(self,loctor):
        '''聚焦元素'''
        target=self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_scroll_top(self):
        '''回到顶部'''
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)

                    # if __name__=="__main__":
#    driver=webdriver.Firefox()
#    driver.get("http://team.zentao.tangyisheng.com.cn")
#    zentao=Base(driver)
#    # locl=(By.ID,"account")
#    # loc2 = (By.NAME, "password")
#    # loc3 = (By.CSS_SELECTOR, "[NAME='PASSWORD']")
#
#    locl = ("id", "account")
#    loc2 = ("css selector", "[name='password']")
#    loc3 = ("id", "submit")
#    zentao.send_keys(locl,"hujiaojiao")
#    zentao.send_keys(loc2,"hujj+0557")
#    zentao.click(loc3,"")