from selenium import webdriver
import time
from Base.Bases import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from urllib import parse
#url = https://sandbox-cs.lingjm365.com/yishengcaiyun/index?channel=test"
class First(Base):
    fac_name = (By.XPATH, "//*[@id='root']/div[3]/div[2]/div[1]/div[1]/div/input")#姓名输入框
    fac2_man = (By.XPATH, "//*[@id='root']/div[3]/div[2]/div[1]/div[2]/div/div[1]")  # 性别选择男
    fac2_woman = (By.XPATH, "//*[@id='root']/div[3]/div[2]/div[1]/div[2]/div/div[2]")  # 性别选择女
    fac3_brithday = (By.XPATH, "//*[@id='root']/div[3]/div[2]/div[1]/div[3]/div")  # 出生日期
    fac4_count = (By.XPATH, "//*[@id='root']/div[3]/div[2]/div[2]/div")  # 首页立即测算
    comfirm_brithday =(By.XPATH,"/html/body/div[6]/div/span/div/div/div/div")# 出生日期提示语
    agree =(By.XPATH,"//*[@id='root']/div[3]/div[2]/div[3]/div/div[1]")# 用户协议勾选框
    agreement =(By.XPATH, "//*[@id='root']/div[3]/div[2]/div[3]/div/div[2]/a[1]")# 用户协议
    secret =(By.XPATH,"//*[@id='root']/div[3]/div[2]/div[3]/div/div[2]/a[2]")# 隐私协议
    order =(By.XPATH, "//*[@id='root']/div[3]/div[2]/p/a")# 历史订单入口
    order_question =(By.XPATH,"// *[ @ id = 'root'] / div[3] / div[1] / div")# 首页订单咨询
    comlpain =(By.XPATH,"//*[@id='root']/div[5]/span")# 首页投诉入口
    order_bottomquestion =(By.XPATH,"// *[ @ id = 'root'] / div[4] / div / div[2] / a")# 首页底部客服
    bottom_agreement =(By.XPATH,".//*[@id='root']/div[3]/div[6]/div[4]/div/div[2]/a[1]")# 底部用户协议
    bottom_secret =(By.XPATH,"//*[@id='root']/div[3]/div[6]/div[4]/div/div[2]/a[2]")# 底部隐私协议
    hot_sixmeasure =(By.XPATH,"//*[@id='root']/div[3]/div[7]/div[2]/div/div[2]/div[2]")# 首页热门测算第六个
    hot_fifthmeasure =(By.XPATH,"//*[@id='root']/div[3]/div[7]/div[2]/div/div[2]/div[1]")# 首页热门测算第五个
    bottom_count =(By.XPATH,"//*[@id='root']/div[3]/div[5]/div[3]/div")# 首页底部测算按钮
    brithday_choose =(By.XPATH,"/html/body/div[2]/div[3]")# 出生日期选择框
    gregorian_calendar =(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[3]/div/span[1]")# 公历按钮
    lunar_calendar =(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[3]/div/span[2]")# 农历按钮
    cancel =(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[1]")# 取消按钮
    complete =(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[2]")# 完成按钮
    comfirm =(By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[2]/span")# 确认完成按钮
    back_fix =(By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[1]/span")# 返回修改按钮
    #videoes =(By.XPATH,"//*[@id='txplayer_df5ee252dc53dc9eab2d9fa0de208e46']/txpdiv[13]/video")# 视频
    wechat_button =(By.XPATH,"//*[@id='pay2']/div[4]/div[2]/div/div/ul/li[1]/div[2]/div")# 微信支付方式
    alipay_button =(By.XPATH,"//*[@id='pay2']/div[4]/div[2]/div/div/ul/li[2]/div[2]/div")# 支付宝支付方式
    more_pay =(By.XPATH,"//*[@id='pay2']/div[4]/div[2]/div/div/div")# 更多支付方式
    bank_button =(By.XPATH,"//*[@id='pay2']/div[4]/div[2]/div/div/ul/li[3]/div[2]/div")# 银联支付方式
    paypal_button =(By.XPATH,"//*[@id='pay2']/div[4]/div[2]/div/div/ul/li[4]/div[2]/div")# paypal支付方式
    buying =(By.XPATH,"/html/body/div[3]/div")# 支付页立即抢购按钮
    pay_picture =(By.XPATH,".//*[@id='pay2']/div[5]/div[2]")# 支付页立即揭秘图片点击跳转支付
    customer =(By.XPATH,"//*[@id='pay2']/div[4]/div[2]/div/a/span[2]")# 支付页支付遇到问题
    bottom_customer=(By.XPATH,"//*[@id='root']/div[2]/div/div[1]/div/a")# 支付页底部客服链接
    picture =(By.XPATH,"//*[@id='root']/div[2]/div/p/a/img")#底部客服下面图片，用于定位使用
    stay=(By.XPATH,"//*[@id='pay2']/div[1]/div/div[5]")#挽留弹框

    def __init__(self, driver,timeout=30, url='https://sandbox-cs.lingjm365.com/yishengcaiyun/index?channel=test'):
       super().__init__(driver, timeout,url)


    '''
    def __init__(self, browser = 'chrome'):
        #browser='chrome'

       if browser == 'ie' or browser == 'internet explorer':
            driver = webdriver.Ie()


        elif browser == 'firefox' or browser == 'ff':
              driver = webdriver.Firefox()

        elif browser == 'chrome':
        #      driver = webdriver.Chrome()


        try:
              self.driver = webdriver.Chrome()
        except Exception:
              raise NameError('没有找到浏览器，请输入"ie","chrome","ff"')
    '''

    def open(self, url="https://sandbox-cs.lingjm365.com/yishengcaiyun/index?channel=test"):  # 打开一个URL
        self.driver.get(url)

    def sentname(self):
        '''输入姓名'''
        self.find_element(*self.fac_name).clear()
        Base.send_keys(self,self.fac_name,"测试一下下")
        #self.find_element(*self.fac_name).send_keys("测试一下下")
        time.sleep(3)  # 强制等待3s再执行
        #self.driver.find_element_by_xpath("//*[@id='root']/div[3]/div[2]/div[1]/div[1]/div/input").send_keys("测试一下下喜爱")

    def sentother(self):
        '''输入姓名为数字、特殊符号时，点击立即测算'''
        self.find_element(*self.fac_name).clear()
        names=['1','$%','-=']
        for index in range(len(names)):
          self.find_element(*self.fac_name).clear()
          Base.send_keys(self, self.fac_name, names[index])
          print(names[index])
          time.sleep(3)
          self.find_element(*self.fac4_count).click()
          #click =Base.click(self,self.fac4_count)
          message_other = self.find_element(*self.comfirm_brithday).text
          message="姓名只能是中文或者英文"
          if message == message_other:
             print("提示语一致")
          else:
             print("提示语不一致")

    def sentenglish(self):
        '''输入姓名为错误英语，点击立即测算'''
        self.find_element(*self.fac_name).clear()
        Base.send_keys(self, self.fac_name, "g")
        time.sleep(3)
        self.find_element(*self.fac4_count).click()
        message_short = self.find_element(*self.comfirm_brithday).text
        message = "英文姓名最少3个字母"
        if message == message_short:
                print("提示语一致")
        else:
                print("提示语不一致")
        self.find_element(*self.fac_name).clear()
        Base.send_keys(self, self.fac_name, "gdgsdfshsdfhdgh")
        time.sleep(3)
        self.find_element(*self.fac4_count).click()
        message_short = self.find_element(*self.comfirm_brithday).text
        message = "英文姓名不超过10个字母"
        if message == message_short:
            print("提示语一致")
        else:
            print("提示语不一致")

    def sentchinese(self):
        '''输入姓名为错误中文，点击立即测算'''
        self.find_element(*self.fac_name).clear()
        Base.send_keys(self, self.fac_name, "那")
        time.sleep(3)
        self.find_element(*self.fac4_count).click()
        message_short = self.find_element(*self.comfirm_brithday).text
        message = "姓名最少2个字"
        if message == message_short:
            print("提示语一致")
        else:
            print("提示语不一致")
        self.find_element(*self.fac_name).clear()
        Base.send_keys(self, self.fac_name, "的房管还是电饭锅互动分")
        time.sleep(3)
        self.find_element(*self.fac4_count).click()
        message_short = self.find_element(*self.comfirm_brithday).text
        message = "姓名不超过5个字"
        if message == message_short:
            print("提示语一致")
        else:
            print("提示语不一致")

    def shouye_button(self):
        '''点击立即测算'''
        self.find_element(*self.fac4_count).click()
        #self.click(self,self.fac4_count)
        time.sleep(3)

    def if_brithdaymessage(self):
        '''不选择出生日期，点击立即测算'''
        time.sleep(3)
        self.find_element(*self.fac4_count).click()
        message_brithday =self.find_element(*self.comfirm_brithday).text
        message = "请选择出生日期"
        if message == message_brithday:
            print("提示语一致")
        else:
            print("提示语不一致")

    def if_sex(self):
        '''性别男、女切换'''
        time.sleep(3)
        self.find_element(*self.fac2_woman).click()
        time.sleep(3)
        self.find_element(*self.fac2_man).click()
        time.sleep(2)
        self.find_element(*self.fac4_count).click()

    def jump_01(self):
        '''跳转用户协议'''
        self.find_element(*self.agreement).click()
        time.sleep(3)
        current= self.driver.current_url
        agreement_url="https://sandbox-cs.lingjm365.com/activitycollection/userProtocol"
        if current==agreement_url:
            print("用户协议跳转正确")
        else:
            print("用户协议跳转错误")
        self.driver.back()
        time.sleep(3)
        '''定位到特定元素旁边'''
        #target = self.find_element(*self.bottom_count)
        #self.driver.execute_script("arguments[0].scrollIntoView(false);",target)
        '''滑动到底部'''
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)
        self.find_element(*self.bottom_agreement).click()
        time.sleep(3)

    def jump_02(self):
        '''跳转隐私协议'''
        self.find_element(*self.secret).click()
        time.sleep(3)
        current = self.driver.current_url
        secret_url ="https://sandbox-cs.lingjm365.com/activitycollection/individualPrivacy"
        if current == secret_url:
            print("隐私协议跳转正确")
        else:
            print("隐私协议跳转错误")
        self.driver.back()
        '''滑动到底部'''
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)
        self.find_element(*self.bottom_secret).click()
        time.sleep(3)

    def history_order(self):
        '''跳转历史订单'''
        self.find_element(*self.order).click()
        time.sleep(3)
        current = self.driver.current_url
        history_url = "https://sandbox-cs.lingjm365.com/orderquery/index?project=yishengcaiyun"
        if current == history_url:
            print("历史订单跳转正确")
        else:
            print("历史订单跳转错误")
        self.driver.back()

    def question(self):
        '''跳转到客服'''
        self.find_element(*self.order_question).click()
        time.sleep(3)
        current = self.driver.current_url
        question_url = "https://linghit.qiyukf.com/client?k=da58ce0115a1232c79a01c472ae24164&wp=1qtype=13111"
        if current == question_url:
            print("订单咨询跳转正确")
        else:
            print("订单咨询跳转错误")
        self.driver.back()
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)
        self.find_element(*self.order_bottomquestion).click()
        time.sleep(3)
        current_url = self.driver.current_url
        ask_url = "https://kefu.lingjisuanming.cn/"
        if current_url == ask_url:
            print("订单咨询跳转正确")
        else:
            print("订单咨询跳转错误")

    def hot_masure(self):
        '''跳转到热门测算'''
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)
        self.find_element(*self.hot_sixmeasure).click()
        time.sleep(3)
        current = self.driver.current_url
        hot_url = "https://aliyun.ju1tao.cn/ziweicaiyun/index?schannel=syyishengcaiyun&channel=test"
        if current == hot_url:
            print("紫微斗数跳转正确")
        else:
            print("紫微斗数跳转错误")
        time.sleep(1)
        self.driver.back()
        self.driver.back()
        time.sleep(1)
        self.find_element(*self.hot_fifthmeasure).click()
        time.sleep(3)
        current_url = self.driver.current_url
        hots_url = "https://aliyun.ju1tao.cn/mllyuncheng/index?schannel=syyishengcaiyun&channel=test"
        if current_url == hots_url:
            print("麦玲玲跳转正确")
        else:
            print("麦玲玲跳转错误")

    def complain(self):
        '''跳转到投诉'''
        self.find_element(*self.comlpain).click()
        time.sleep(3)
        current = self.driver.current_url
        complain_url = "https://sandbox-cs.lingjm365.com/activitycollection/report?appName=%E4%B8%80%E7%94%9F%E8%B4%A2%E8%BF%902020&id=yi_sheng_cai_yun"
        if current == complain_url:
            print("投诉界面跳转正确")
        else:
            print("投诉界面跳转错误")
        self.driver.back()
    '''
    def video(self):
           播放视频
        js = "var q=document.documentElement.scrollTop=4200"
        self.driver.execute_script(js)
        time.sleep(3)
        video= self.find_element(*self.videoes)
        print(video)
        url =self.driver.execute_script("return arguments[0].currentStr;",video)
        print(url)
        self.driver.execute_script("return arguments[0].paly()",video)
        time.sleep(3)
     '''
    def if_check(self):
        '''不勾选协议，点击立即测算'''
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        time.sleep(3)
        self.find_element(*self.agree).click()
        time.sleep(3)
        self.find_element(*self.fac4_count).click()
        message_check =self.find_element(*self.comfirm_brithday).text
        message = "请同意《用户协议》后，再进行下一步"
        if message == message_check:
            print("提示语一致")
        else:
            print("提示语不一致")
        #jsbottom = "var q=document.documentElement.scrollTop=10000"#滑动到底部
        #self.driver.execute_script(jsbottom)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')#滑动到底部
        time.sleep(3)
        self.find_element(*self.bottom_count).click()
        message_checks = self.find_element(*self.comfirm_brithday).text
        message_bottom = "请同意《用户协议》后，再进行下一步"
        if message_checks == message_bottom:
            print("提示语一致")
        else:
            print("提示语不一致")

    def if_cancel(self):
        '''切换公农历、取消选择日期'''
        time.sleep(3)
        self.find_element(*self.fac3_brithday).click()
        time.sleep(1)
        self.find_element(*self.gregorian_calendar).click()
        time.sleep(1)
        self.find_element(*self.lunar_calendar).click()
        time.sleep(1)
        self.find_element(*self.cancel).click()
        time.sleep(1)
        self.find_element(*self.fac4_count).click()
        time.sleep(3)

    def if_complete(self):
        '''选择日期-返回修改-确定日期-进行测算-确认跳转到支付页'''
        time.sleep(3)
        self.find_element(*self.fac3_brithday).click()
        time.sleep(1)
        self.find_element(*self.gregorian_calendar).click()
        time.sleep(1)
        self.find_element(*self.lunar_calendar).click()
        time.sleep(1)
        self.find_element(*self.complete).click()
        time.sleep(1)
        self.find_element(*self.back_fix).click()
        time.sleep(1)
        self.find_element(*self.complete).click()
        time.sleep(1)
        self.find_element(*self.comfirm).click()
        time.sleep(1)
        self.find_element(*self.fac4_count).click()
        time.sleep(3)
        current_url = self.driver.current_url
        params = parse.parse_qs(parse.urlparse(current_url).query)#获取url的参数与参数值
        #print(params['order_id'])
        order_id ="".join(params['order_id'])#将列表转化为字符串
        pay_url ="https://sandbox-cs.lingjm365.com/yishengcaiyun/pay2?order_id="+order_id
        print(pay_url)
        if current_url == pay_url:
            print("支付页跳转正确")
        else:
            print("支付页跳转错误")

    def pay_customer(self):
        '''选择日期-返回修改-确定日期-进行测算-确认跳转到支付页-跳转到客服界面-跳转到底部客服界面'''
        pay_jump = self.if_complete()
        time.sleep(1)
        self.find_element(*self.customer).click()
        customer_url = self.driver.current_url
        ask_url = "https://linghit.qiyukf.com/client?k=da58ce0115a1232c79a01c472ae24164&wp=1qtype=13111"
        if customer_url == ask_url:
            print("客服界面跳转正确")
        else:
            print("客服界面跳转错误")
        self.driver.back()
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        target = self.find_element(*self.picture)
        self.driver.execute_script("arguments[0].scrollIntoView(false);",target)
        time.sleep(3)
        self.find_element(*self.bottom_customer).click()
        bottomcustomer_url = self.driver.current_url
        question_url = "https://kefu.lingjisuanming.cn/"
        if bottomcustomer_url == question_url:
            print("客服界面跳转正确")
        else:
            print("客服界面跳转错误")
        self.driver.back()

    def pay(self):
        '''选择日期-返回修改-确定日期-进行测算-确认跳转到支付页-跳转微信支付-跳转支付宝支付-跳转银联支付-跳转paypal支付'''
        self.if_complete()
        time.sleep(3)
        self.find_element(*self.wechat_button).click()
        time.sleep(3)
        wechat_url=self.driver.current_url
        print(wechat_url)
        wechat_netloc = parse.urlparse(wechat_url).netloc# 获取url的域名
        print(wechat_netloc)
        wechat_hostname="sandbox-money.dapeiguanli.com"
        if wechat_netloc == wechat_hostname:
            print("微信支付跳转正确")
        else:
            print("微信支付跳转错误")
        self.driver.back()
        time.sleep(3)
        self.find_element(*self.alipay_button).click()
        time.sleep(3)
        alipay_url = self.driver.current_url
        print(alipay_url)
        alipay_netloc = parse.urlparse(alipay_url).netloc  # 获取url的域名
        print(alipay_netloc)
        alipay_hostname = "excashier.alipay.com"
        if alipay_netloc == alipay_hostname:
            print("支付宝支付跳转正确")
        else:
            print("支付宝支付跳转错误")
        self.driver.back()
        time.sleep(3)
        self.find_element(*self.more_pay).click()
        self.find_element(*self.bank_button).click()
        time.sleep(3)
        bank_url = self.driver.current_url
        print(bank_url)
        bank_netloc = parse.urlparse(bank_url).netloc  # 获取url的域名
        print(bank_netloc)
        bank_hostname = "cashier.95516.com"
        if bank_netloc == bank_hostname:
            print("银联支付跳转正确")
        else:
            print("银联支付跳转错误")
        self.driver.back()
        time.sleep(3)
        self.find_element(*self.more_pay).click()
        self.find_element(*self.paypal_button).click()
        time.sleep(4)
        paypal_url = self.driver.current_url
        print(paypal_url)
        paypal_netloc = parse.urlparse(paypal_url).netloc  # 获取url的域名
        print(paypal_netloc)
        paypal_hostname = "www.paypal.com"
        if paypal_netloc == paypal_hostname:
            print("paypal支付跳转正确")
        else:
            print("paypal支付跳转错误")
        self.driver.back()

    def pay_pictures(self):
        '''选择日期-返回修改-确定日期-进行测算-确认跳转到支付页-底部立即购买跳转支付-支付页图片跳转支付-挽留弹框支付跳转'''
        self.if_complete()
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=200000"
        self.driver.execute_script(js)
        target = self.find_element(*self.picture)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", target)
        time.sleep(3)
        self.find_element(*self.buying).click()
        time.sleep(3)
        buying_url = self.driver.current_url
        print(buying_url)
        buying_netloc = parse.urlparse(buying_url).netloc  # 获取url的域名
        print(buying_netloc)
        wechat_hostname = "sandbox-money.dapeiguanli.com"
        if buying_netloc == wechat_hostname:
            print("微信支付跳转正确")
        else:
            print("微信支付跳转错误")
        self.driver.back()
        time.sleep(3)
        js_picture = "var q=document.documentElement.scrollTop=5000"
        self.driver.execute_script(js_picture)
        time.sleep(3)
        self.find_element(*self.pay_picture).click()
        time.sleep(3)
        picture_url = self.driver.current_url
        print(picture_url)
        picture_netloc = parse.urlparse(picture_url).netloc  # 获取url的域名
        print(picture_netloc)
        if picture_netloc == wechat_hostname:
            print("微信支付跳转正确")
        else:
            print("微信支付跳转错误")
        self.driver.back()
        self.driver.back()
        time.sleep(3)
        self.find_element(*self.stay).click()
        time.sleep(3)
        stay_url = self.driver.current_url
        print(stay_url)
        stay_netloc = parse.urlparse(picture_url).netloc  # 获取url的域名
        print(stay_netloc)
        if stay_netloc == wechat_hostname:
            print("微信支付跳转正确")
        else:
            print("微信支付跳转错误")