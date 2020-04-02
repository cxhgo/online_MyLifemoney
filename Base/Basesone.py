from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os,configparser
from selenium.webdriver.common.by import By

class Base():
    '''
    path =os.path.dirname(os.path.abspath("."))#找到代码存放路径
    cfpath = os.path.join(path,'F:\MyLifemoney\config\config.ini')#获取配置文件路径
    conf =configparser.ConfigParser()
    conf.read(cfpath)
    url =conf.get('base','url')
    '''
    # def __init__(self, driver,timeout,url):
    #     self.driver = driver
    #     self.url = url
    #     self.timeout =timeout

    def __init__(self, driver,timeout):
       # self.url = url
        self.timeout = timeout
        self.driver=driver


    def open(self,url):
        self.driver.get(url)
        time.sleep(3)
        return self.driver.current_url == url

    # def open(self):
    #     self.driver.get(self.url)

    def find_element(self,*loc):
        #传入参数为元组需要加*，本身就是元组的不需要

        try:
           #判断是否定位到元素，是返回元素，否，报错+等待
           WebDriverWait(self.driver,self.timeout,0.5).until(EC.visibility_of_element_located(loc))
           return self.driver.find_element(*loc)
        except:
            print('页面未找到元素')

    def find_elements(self,*loc):
        #复数的时候，多个相同
        return self.driver.find_elements(*loc)


    def send_keys(self,loc,value):
        #输入传值
        self.find_element(*loc).send_keys(value)
    def click(self,loc):
        #点击按钮
        self.find_element(*loc).click()
    def clear(self,loc):
        #清除
        self.find_element(*loc).clear()

    def bottom_skip(self,height):

        js = "var q=document.documentElement.scrollTop="+height
        self.driver.execute_script(js)
        #self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    def if_tip(self,message,loc):
        mes=self.find_element(*loc).text
        if message == mes:
            print("提示正确")
        else:
            print("提示错误")

    def find_currenturl(self):
        return self.driver.current_url



