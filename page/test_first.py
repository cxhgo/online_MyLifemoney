from selenium import webdriver
import unittest
from page.shouye_page import First
from Base.logger import Log
import time
class Yscy_First(unittest.TestCase):

     def setUp(self):
        print("开始测试")
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(chrome_options=option)
        #self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        #self.driver.maximize_window()
        #self.log =Log()
        self.yscy = First(self.driver)
        self.yscy.open()

     def test_01(self):
         #输入姓名，点击立即测算
         self.yscy.sentname()
         self.yscy.shouye_button()

     def test_02(self):
         #不选择和填写，点击立即测算
         self.yscy.if_brithdaymessage()

     def test_03(self):
         #性别切换
         self.yscy.if_sex()

     def test_04(self):
         #跳转到用户协议
         self.yscy.jump_01()

     def test_05(self):
        # 跳转到隐私协议
         self.yscy.jump_02()

     def test_06(self):
         # 跳转到历史订单
         self.yscy.history_order()

     def test_07(self):
         # 跳转到客服咨询
         self.yscy.question()

     def test_08(self):
         # 跳转到热门测算
         self.yscy.hot_masure()

     def test_09(self):
         # 跳转到投诉
         self.yscy.complain()
     '''
     def test_10(self):
        yscy = First(self.driver)
        openfac = yscy.open()
        video = yscy.video()
     '''
     def test_11(self):
         #输入特殊字符是否提示正确
         self.yscy.sentother()

     def test_12(self):
         #输入错误英文是否提示正确
         self.yscy.sentenglish()

     def test_13(self):
         #输入错误中文，是否提示正确
         self.yscy.sentchinese()

     def test_14(self):
         # 不勾选协议，是否提示正确
         self.yscy.if_check()

     def test_15(self):
         #是否取消选出生日期
         self.yscy.if_cancel()

     def test_16(self):
        # 是否确认出生日期，跳转到支付页
         self.yscy.if_complete()

     def test_17(self):
         # 是否正确跳转支付页的客服链接
         self.yscy.pay_customer()

     def test_18(self):
         # 是否正确跳转各支付方式
         self.yscy.pay()

     def test_19(self):
         # 支付页图片跳转支付是否正确
         self.yscy.pay_pictures()

     def tearDown(self):
         self.driver.quit()

