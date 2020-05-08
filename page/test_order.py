from selenium import webdriver
import unittest
from page.Order_page import Order
from selenium import webdriver
from Base.logger import Log
from selenium.webdriver.chrome.options import Options
class Yscy_Order(unittest.TestCase):


   def setUp(self,browser='chrome'):

       print("开始测试")
       try:
          if browser == 'ie' or browser == 'internet explorer':
             self.driver = webdriver.Ie()
             print(self.driver)

          elif browser == 'firefox' or browser == 'ff':
             self.driver = webdriver.Firefox()
             print(self.driver)

          elif browser == 'chrome':
             # option = webdriver.ChromeOptions()
             # option.add_argument('--user-agent=iphone')
             mobile_emulation = {"deviceName": "Galaxy S5"}  # 设置浏览器内支持的设备
             options = webdriver.ChromeOptions()
             options.add_experimental_option("mobileEmulation", mobile_emulation)
             self.driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=options)  # 打开网页，将网页调整为手机模式
             #self.driver = webdriver.Chrome()
             #self.driver.maximize_window()
             print(self.driver)
       except Exception:
             raise NameError('没有找到浏览器，请输入"ie","chrome","ff"')
       self.log = Log()
       self.order = Order(self.driver)
       self.order.open()

   def test_01(self):
       #是否跳转到历史订单
       order=self.order.if_jump()
       orderurl="/orderquery/index"
       self.assertEqual(order, orderurl)

   def test_02(self):
       #不输入订单或者输入错误是否有提示
       self.order.order_tip()

   def test_03(self):
       #是否正确选择订单跳转到支付页
       order=self.order.click_look()
       orderurl="/yishengcaiyun/pay2"
       self.assertEqual(order, orderurl)


   def test_04(self):
       #删除订单是否有提示
       self.order.check_delete()

   def test_05(self):
       #切换手机查找订单各个校验
       self.order.phone_find()

   def test_06(self):
       #切换手机查找订单各个校验
       question= self.order.question()
       questionurl="https://kefu.lingjisuanming.cn/"
       self.assertEqual(question, questionurl)


   def tearDown(self):
       print("测试结束")
       self.driver.quit()