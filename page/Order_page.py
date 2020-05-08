from urllib import parse
from page.shouye_page import First
import time
from Base.Basesone import Base
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Order(Base):
    order_jump = (By.XPATH,"/html/body/div[1]/div[3]/div[2]/p/a")#历史订单跳转
    order_input =(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/section/div/div/input")#历史订单输入框
    order_query =(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/section/button")#历史订单查询按钮
    order_find=(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/ul/li[1]/div[4]")#历史订单记录查询
    order_delete=(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/ul/li[1]/div[5]")#删除订单
    order_cancel=(By.CLASS_NAME,"am-modal-button")#删除订单取消按钮
    order_phone=(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/section/span")#切换手机查找订单
    order_phoneinput=(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/section/div/div[1]/input")#手机输入框
    order_year=(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/section/div/div[2]/div/input")#年份选择
    order_yearcancel=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div[1]")#年份取消
    order_yearcheck=(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div[3]")#年份确定
    order_codeinput=(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/section/div/div[3]/input")#验证码输入框
    order_getcode=(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/section/div/div[3]/span[2]")#获取验证码按钮
    order_question=(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[2]/div/div[1]/div/a")#客服
    order_tips=(By.XPATH,"/html/body/div[2]/div/span/div/div/div")#提示语
    order_id=(By.XPATH,"/html/body/div[1]/div/section/div[1]/div[1]/ul/li[1]/div[2]/div[2]")#订单号
    check_find= (By.XPATH,".//*[@id='orderList']/li[1]/div[5]")#手机查询点击查看
    phone_orderid=(By.XPATH,".//*[@id='orderList']/li[1]/div[3]/div[2]")#手机查询订单号
    def __init__(self,driver,timeout=30):
        '''初始化'''
        Base.__init__(self,driver,timeout)

    def open(self, url="https://sandbox-cs.lingjm365.com/yishengcaiyun/index?channel=test"):
        '''打开界面'''
        return super().open(url)

    def if_jump(self):
        '''调用首页跳转支付页-从支付页返回-进入历史订单'''
        first = First(self.driver)
        first.if_complete()
        self.driver.back()
        self.driver.back()
        time.sleep(1)
        self.find_element(*self.order_jump).click()
        time.sleep(3)
        return Base.find_currenturl(self,1)

    def order_tip(self):
        '''进入历史订单-订单号为空提示-输入错误订单号提示'''
        self.find_element(*self.order_jump).click()
        time.sleep(2)
        self.find_element(*self.order_query).click()
        time.sleep(1)
        Base.if_tip(self,"订单号不能为空或格式不正确",self.order_tips)
        time.sleep(2)
        Base.send_keys(self, self.order_input, "BZJP15880470860950006")
        self.find_element(*self.order_query).click()
        Base.if_tip(self,"资源不存在",self.order_tips)
        time.sleep(1)

    def click_look(self):
        '''调用进入支付页再进入历史订单生成订单数据-选择一个订单点击查看-进入支付'''
        Order.if_jump(self)
        time.sleep(2)
        mes=self.find_element(*self.order_id).text
        print(mes)
        self.find_element(*self.order_find).click()
        time.sleep(1)
        params= Base.find_currenturl(self,2)
        print (params)
        orderid ="".join(params['order_id'])#将列表值提取并转化为字符串
        if orderid== mes:
            print("跳转正确")
        else:
            print("跳转错误")
        return Base.find_currenturl(self,1)

    def check_delete(self):
        '''调用进入支付页再进入历史订单生成订单数据-选择一个订单点击删除-点击取消删除'''
        Order.if_jump(self)
        time.sleep(2)
        self.find_element(*self.order_delete).click()
        time.sleep(1)
        self.find_element(*self.order_cancel).click()
        time.sleep(3)

    def phone_find(self):
        '''切换到手机查找方式-不输入各种校验-输入错误各种校验-查找出订单-选择订单进行跳转'''
        self.find_element(*self.order_jump).click()
        time.sleep(2)
        self.find_element(*self.order_phone).click()
        time.sleep(1)
        self.find_element(*self.order_query).click()
        Base.if_tip(self,"手机号码不能为空",self.order_tips)
        time.sleep(4)
        self.find_element(*self.order_getcode).click()
        Base.if_tip(self,"手机号码不能为空",self.order_tips)
        time.sleep(1)
        self.find_element(*self.order_phoneinput).clear()
        phones=['1gafdg解决','188264262722','12483585']
        for index in range(len(phones)):
          self.find_element(*self.order_phoneinput).clear()
          Base.send_keys(self, self.order_phoneinput, phones[index])
          time.sleep(1)
          self.find_element(*self.order_query).click()
          time.sleep(1)
          Base.if_tip(self,"手机号码格式不正确！",self.order_tips)
          time.sleep(4)
          self.find_element(*self.order_getcode).click()
          Base.if_tip(self,"手机号码格式不正确！",self.order_tips)
          time.sleep(1)
        time.sleep(2)
        self.find_element(*self.order_phoneinput).clear()
        Base.send_keys(self, self.order_input, "18826426272")
        self.find_element(*self.order_query).click()
        time.sleep(1)
        Base.if_tip(self,"请选择年份",self.order_tips)
        time.sleep(1)
        self.find_element(*self.order_year).click()
        time.sleep(2)
        self.find_element(*self.order_yearcancel).click()
        time.sleep(2)
        self.find_element(*self.order_year).click()
        time.sleep(1)
        self.find_element(*self.order_yearcheck).click()
        time.sleep(2)
        self.find_element(*self.order_query).click()
        time.sleep(2)
        Base.if_tip(self,"验证码不能为空",self.order_tips)
        time.sleep(1)
        Base.send_keys(self, self.order_codeinput, "45894")#测服去掉验证码校验
        self.find_element(*self.order_query).click()
        time.sleep(5)
        self.find_element(*self.order_query).click()
        Base.if_tip(self,"请勿重复点击",self.order_tips)
        time.sleep(3)
        mes=self.find_element(*self.phone_orderid).text
        print(mes)
        self.find_element(*self.check_find).click()
        time.sleep(1)
        params= Base.find_currenturl(self,2)
        print (params)
        orderid ="".join(params['order_id'])#将列表值提取并转化为字符串
        if orderid == mes:
            print("跳转正确")
        else:
            print("跳转错误")


    def question(self):
        '''进入历史订单-跳转底部客服'''
        self.find_element(*self.order_jump).click()
        time.sleep(2)
        self.find_element(*self.order_question).click()
        return Base.find_currenturl(self,0)



















