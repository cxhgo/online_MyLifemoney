from selenium import webdriver
import unittest
from page.Last_page import Last
from selenium import webdriver
from Base.logger import Log
class Yscy_Last(unittest.TestCase):


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
             self.driver = webdriver.Chrome()
             #self.driver.maximize_window()
             print(self.driver)
       except Exception:
             raise NameError('没有找到浏览器，请输入"ie","chrome","ff"')
       self.log = Log()
       self.last = Last(self.driver)
       self.last.open()

   def test_01(self):
       #手机邮箱弹框是否勾选协议校验
       self.last.one_box_check()

   def test_02(self):
       #手机邮箱弹框输入为空的点击
       self.last.one_box()

   def test_03(self):
      #手机邮箱弹框输入错误提示校验
       self.last.one_box_mail()

   def test_04(self):
      #客服链接跳转校验
       bottom_kefu=self.last.bottom_kefu()
       free_url = "https://linghit.qiyukf.com/client?k=da58ce0115a1232c79a01c472ae24164&wp=1qtype=13111&channel=test&combo_goods_id=13"
       self.assertEqual(bottom_kefu,free_url)

   def test_05(self):
       # 免费追问链接跳转校验
       bottom_free = self.last.bottom_freequestion()
       free_url = "https://sandbox-cs.lingjm365.com/zwquestion/newguide?channel=test&combo_goods_id=13&source_id=YSCY158406802109500000&source_key=yi_sheng_cai_yun"
       self.assertEqual(bottom_free, free_url)

   def test_06(self):
      # 热门测算链接跳转校验
       bottom_hot =self.last.bottom_hotskip()
       free_url = "https://zx.xhrlzab.cn/cesuandaquan/shopsite?schannel=jieguoyewl&channel=test&combo_goods_id=13"
       self.assertEqual(bottom_hot, free_url)

   def test_07(self):
      # 服务条款链接跳转校验
       top_secret = self.last.top_secret_document()
       assert_url = "https://sandbox-cs.lingjm365.com/activitycollection/individualPrivacy"
       self.assertEqual(top_secret, assert_url)

   def test_08(self):
       # 手机邮箱输入校验校验
       self.last.sent_check()

   def test_09(self):
       # 姓名输入校验校验
       self.last.sent_name()

   def test_10(self):
       # 点赞-反馈-返回顶部-查看目录
       self.last.praise_orno()


   def test_11(self):
       #换一批跳转
       changing=self.last.change()
       changurl="https://m.linghit666.com/live/download?channel=lingji_calendar"
       self.assertEqual(changing, changurl)

   def test_12(self):
       #精品测算的跳转
       guessing=self.last.fineguess()
       #guessurl="https://afb.hedebt.cn/zwzjingpi/index?channel=test&schannel=jgyzywyishengcaiyun"
       guessurl="/zwzjingpi/index"
       self.assertEqual(guessing, guessurl)

   def test_13(self):
       #热门测算跳转
       guessing=self.last.guess()
       guessurl="https://afb.hedebt.cn/qianshiyinyuan/index?schannel=jgyyishengcaiyun&channel=test"
       self.assertEqual(guessing, guessurl)


   def test_14(self):
       #商城弹框各个校验
       self.last.shopping()


   def tearDown(self):
       print("测试结束")
       self.driver.quit()