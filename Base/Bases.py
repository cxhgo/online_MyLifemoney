from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os,configparser
class Base():
    '''用于首页和支付页使用'''
    '''
    path =os.path.dirname(os.path.abspath("."))#找到代码存放路径
    cfpath = os.path.join(path,'F:\MyLifemoney\config\config.ini')#获取配置文件路径
    conf =configparser.ConfigParser()
    conf.read(cfpath)
    url =conf.get('base','url')
    '''
    def __init__(self, driver,timeout,url):
         self.driver = driver
         self.url = url
         self.timeout =timeout

    # def __init__(self, timeout, url):
    #     self.url = url
    #     self.timeout = timeout

    '''
    def open(self,url):
        self.driver.get(self.url)
        time.sleep(3)
        return self.driver.current_url == url
    '''
    def open(self):
        self.driver.get(self.url)

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