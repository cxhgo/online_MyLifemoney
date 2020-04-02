import time
from Base.Basesone import Base
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from urllib import parse
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Last(Base):
    free_question = (By.XPATH, "/html/body/div[4]/ul/li[1]")  # 免费追问
    kefu =(By.XPATH,"html/body/div[4]/ul/li[2]")#客服
    hotguess=(By.XPATH,"/html/body/div[4]/ul/li[3]")#热门测算
    mailbox=(By.XPATH,"//*[@id='email']/div[2]/div/div[1]/div[2]/input")#邮箱输入框
    phone =(By.XPATH,"//*[@id='email']/div[2]/div/div[2]/div[2]/input")#手机输入框
    push_button=(By.XPATH,"//*[@id='email']/div[2]/div/div[3]")#发送按钮
    secret_document=(By.XPATH,"//*[@id='email']/div[2]/div/div[4]/span[2]/a")#服务条款
    checkbox=(By.XPATH,"//*[@id='email']/div[2]/div/div[4]/span[1]")#协议勾选框
    namebox=(By.XPATH,"//*[@id='root']/div[1]/section[2]/div[2]/div/section/div/input")#姓名输入框
    commit_button=(By.XPATH,"//*[@id='root']/div[1]/section[2]/div[2]/div/section/div/div")#姓名提交按钮
    praise_button=(By.XPATH,"//*[@id='tab_scroll_0']/div[5]/div/div[1]")#点赞按钮
    nopraise_button=(By.XPATH,"//*[@id='tab_scroll_0']/div[5]/div/div[2]")#不准按钮
    nopraise_buttonone=(By.XPATH,"//*[@id='tab_scroll_1']/div[5]/div/div[2]")#未点击过的不准按钮
    back_to_top=(By.XPATH,"/html/body/div[2]/div")#返回顶部按钮
    bottom_hotguess=(By.XPATH,"//*[@id='root']/div[1]/div[17]/div[2]/div[1]/div[3]")#底部热门测算其中一个
    good_picture=(By.XPATH,".//*[@id='root']/div[1]/div[12]/div[2]/div/div/div/img")  # 商城图片
    fine_guess=(By.XPATH,"/html/body/div[1]/div[1]/div[13]/div[2]/div[9]/div[1]/div[1]")#精品测算其中一个
    changing=(By.XPATH,".//*[@id='root']/div[1]/div[14]/div/div[2]/div")#换一批
    change_url=(By.XPATH,".//*[@id='root']/div[1]/div[14]/div/ul/li[2]/div[1]")#换一批的链接
    lists=(By.XPATH,"/html/body/div[1]/div[1]/div[16]/div/div")#目录按钮
    list_one=(By.XPATH,"/html/body/div[1]/div[1]/div[16]/div/div[2]/div[7]")#目录其中一个
    close_list=(By.XPATH,"/html/body/div[1]/div[1]/div[16]/div/div[1]/img")#关闭目录列表
    tickling_commit=(By.XPATH,"//*[@id='tab_scroll_1']/div[5]/div[2]/div[2]/div[2]/div[3]")#反馈提交按钮
    close_ticklingbox=(By.XPATH,"//*[@id='tab_scroll_1']/div[5]/div[2]/div[2]/div[1]/img")#关闭反馈弹框按钮
    goodbox_buy=(By.XPATH,"/html/body/div[1]/div[1]/div[12]/div[2]/section/div/div/div[4]/div[2]")#点击请购
    goodbox_cancel=(By.XPATH,"//*[@id='root']/div[1]/div[12]/div[2]/section/div/div/div[4]/div[1]")#取消商城弹框
    stay_buy=(By.XPATH,"//*[@id='root']/div[1]/div[12]/div[2]/section/div[2]/div/div/div/div[2]")#挽留弹框中的点击请购
    stay_cancel=(By.XPATH,"//*[@id='root']/div[1]/div[12]/div[2]/section/div[2]/div/div/div/div[1]")#挽留的去意已决按钮
    goodname_input=(By.XPATH,"/html/body/div[1]/div[1]/div[12]/div[2]/section/div/div/div[3]/ul/li[1]/div[2]/input")#商品姓名输入框
    goodphone_input=(By.XPATH,"/html/body/div[1]/div[1]/div[12]/div[2]/section/div/div/div[3]/ul/li[2]/div[2]/input")#商品电话输入框
    goodadress_input=(By.XPATH,"/html/body/div[1]/div[1]/div[12]/div[2]/section/div/div/div[3]/ul/li[4]/div[2]/div/div/p")#商品地址选择
    goodadress_cancel=(By.XPATH,"/html/body/div[5]/div/div[2]/div/div/div/div/div[1]/div[1]")#省市区取消按钮
    goodadress_check=(By.XPATH,"/html/body/div[5]/div/div[2]/div/div/div/div/div[1]/div[3]")#省市区确定按钮
    goodadress_beijing=(By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]")#北京
    goodadress_neimenggu=(By.XPATH,"/html/body/div[6]/div/div[2]/div/div/div/div/div[2]/div[1]/div[2]")#内蒙古
    gooddetailadress_input=(By.XPATH,"/html/body/div[1]/div[1]/div[12]/div[2]/section/div/div/div[3]/ul/li[5]/div[2]/textarea")#商品详细地址输入框
    goodnumber_cut=(By.XPATH,"/html/body/div[1]/div[1]/div[12]/div[2]/section/div/div/div[1]/div/div[2]/div[2]/ul/li[1]")#商品数量选择减少-
    goodnumber_add=(By.XPATH,"/html/body/div[1]/div[1]/div[12]/div[2]/section/div/div/div[1]/div/div[2]/div[2]/ul/li[3]")#商品数量选择增加+
    phonebox=(By.XPATH,"//*[@id='root']/div[1]/section[1]/div/div[2]/div/div[2]/div[1]/div[2]/input")#电话号码输入框
    mailbox_url=(By.XPATH,"//*[@id='root']/div[1]/section[1]/div/div[2]/div/div[2]/div[2]/span")#邮箱出现链接
    box_mailbox=(By.XPATH,"//*[@id='root']/div[1]/section[1]/div/div[2]/div/div[2]/div[2]/div[2]/input")#邮箱输入框
    box_input=(By.XPATH,"//*[@id='root']/div[1]/section[1]/div/div[2]/div/div[3]/div/div")#保存提交按钮
    box_check=(By.XPATH,".//*[@id='root']/div[1]/section[1]/div/div[2]/div/div[4]")#勾选协议按钮
    box_pass=(By.XPATH,"//*[@id='root']/div[1]/section[1]/div/div[2]/div/div[5]/span")#跳过保存
    no_lose=(By.XPATH,"//*[@id='root']/div[1]/section[1]/div/div[2]/div/div[2]/div[1]")#不怕丢失按钮
    box_keep=(By.XPATH,"//*[@id='root']/div[1]/section[1]/div/div[2]/div/div[2]/div[2]")#我要保存返回按钮
    box_tip=(By.XPATH,"html/body/div[5]/div/span/div/div/div")#提示框
    tickings_tip=(By.XPATH,"html/body/div[3]/div/span/div/div/div")#反馈语提示框
    download_close=(By.XPATH," html/body/div[3]/div/div/div[1]/div")#下载引导框关闭按钮

    def __init__(self,driver,timeout=30):
        Base.__init__(self,driver,timeout)

    def open(self, url="https://sandbox-cs.lingjm365.com/yishengcaiyun/result?order_id=YSCY158406802109500000"):
        return super().open(url)

    def bottom_kefu(self):
        time.sleep(1)
        self.find_element(*self.kefu).click()
        time.sleep(3)
        return Base.find_currenturl(self)

    def bottom_freequestion(self):
        time.sleep(1)
        self.find_element(*self.free_question).click()
        time.sleep(3)
        return Base.find_currenturl(self)

    def bottom_hotskip(self):
        time.sleep(1)
        self.find_element(*self.hotguess).click()
        time.sleep(3)
        return Base.find_currenturl(self)

    def one_box_disappear(self):
        time.sleep(1)
        self.find_element(*self.box_pass).click()
        self.find_element(*self.no_lose).click()
        time.sleep(3)

    def top_secret_document(self):
        Last.one_box_disappear(self)
        self.find_element(*self.secret_document).click()
        time.sleep(3)
        return Base.find_currenturl(self)

    def one_box(self):
        time.sleep(2)
        self.find_element(*self.box_input).click()
        Base.if_tip(self,"邮箱或手机号至少填写一项！",self.box_tip)
        time.sleep(1)


    def one_box_check(self):
        time.sleep(2)
        self.find_element(*self.box_check).click()
        self.find_element(*self.box_input).click()
        Base.if_tip(self,"请先同意个人隐私协议",self.box_tip)
        time.sleep(1)

    def one_box_mail(self):
        time.sleep(2)
        Base.send_keys(self, self.phonebox, "测试一下下")
        self.find_element(*self.box_input).click()
        Base.if_tip(self,"手机号码格式不正确！",self.box_tip)
        time.sleep(1)
        self.find_element(*self.phonebox).clear()
        self.driver.refresh()
        Base.send_keys(self, self.phonebox, "1549286954665867")
        self.find_element(*self.box_input).click()
        Base.if_tip(self,"手机号码格式不正确！",self.box_tip)
        time.sleep(1)
        self.find_element(*self.phonebox).clear()
        self.driver.refresh()
        self.find_element(*self.mailbox_url).click()
        Base.send_keys(self, self.box_mailbox, "18826426272")
        self.find_element(*self.box_input).click()
        Base.if_tip(self,"邮箱格式不正确！",self.box_tip)
        # other_mail=(By.CSS_SELECTOR,".am-toast am-toast-mask")#获取css取样器元素
        # WebDriverWait(self.driver, 120).until(EC.invisibility_of_element_located(other_mail))#断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
        # WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable(self.mailbox_url))#判断某个元素中是否可见并且是enable的

    def sent_check(self):
        time.sleep(1)
        Last.one_box_disappear(self)
        self.find_element(*self.push_button).click()
        Base.if_tip(self,"邮箱或手机号至少填写一项！",self.box_tip)
        time.sleep(3)
        self.find_element(*self.checkbox).click()
        self.find_element(*self.push_button).click()
        Base.if_tip(self,"请先阅读服务条款和隐私政策",self.box_tip)
        time.sleep(3)
        self.find_element(*self.checkbox).click()
        Base.send_keys(self, self.phone, "ggfkdfjhkhsk")
        self.find_element(*self.push_button).click()
        Base.if_tip(self,"手机号码格式不正确！",self.box_tip)
        time.sleep(1)
        self.find_element(*self.phone).clear()
        Base.send_keys(self, self.phone, "15004690")
        time.sleep(3)
        self.find_element(*self.push_button).click()
        Base.if_tip(self,"手机号码格式不正确！",self.box_tip)
        time.sleep(2)
        self.find_element(*self.phone).clear()
        Base.send_keys(self, self.mailbox, "15004690")
        time.sleep(3)
        self.find_element(*self.push_button).click()
        Base.if_tip(self,"邮箱格式不正确！",self.box_tip)
        time.sleep(3)

    def sent_name(self):
        time.sleep(1)
        Last.one_box_disappear(self)
        self.find_element(*self.commit_button).click()
        Base.if_tip(self,"请填写您的姓名",self.box_tip)
        time.sleep(2)
        Base.send_keys(self, self.namebox, "sdhlfjhjfldh")
        self.find_element(*self.commit_button).click()
        Base.if_tip(self,"英文姓名不超过10个字母",self.box_tip)
        time.sleep(2)
        self.find_element(*self.namebox).clear()
        Base.send_keys(self, self.namebox, "s")
        self.find_element(*self.commit_button).click()
        Base.if_tip(self,"英文姓名最少3个字母",self.box_tip)
        time.sleep(2)
        self.find_element(*self.namebox).clear()
        Base.send_keys(self, self.namebox, "￥……#……%￥")
        self.find_element(*self.commit_button).click()
        Base.if_tip(self,"姓名只能是中文或者英文",self.box_tip)
        time.sleep(2)
        self.find_element(*self.namebox).clear()
        Base.send_keys(self, self.namebox, "饿")
        self.find_element(*self.commit_button).click()
        Base.if_tip(self,"姓名最少2个字",self.box_tip)
        time.sleep(2)
        self.find_element(*self.namebox).clear()
        Base.send_keys(self, self.namebox, "饿法国队更健康的发生过")
        self.find_element(*self.commit_button).click()
        Base.if_tip(self,"姓名不超过5个字",self.box_tip)
        time.sleep(2)

    def praise_orno(self):
        #点赞-反馈-反馈校验-关闭弹框-返回顶部-查看目录-跳转对应目录-关闭目录
        time.sleep(1)
        Last.one_box_disappear(self)
        Base.bottom_skip(self,"1000")
        self.find_element(*self.praise_button).click()
        Base.if_tip(self,"您已经评价过了",self.box_tip)
        time.sleep(2)
        self.find_element(*self.nopraise_button).click()
        Base.if_tip(self,"您已经评价过了",self.box_tip)
        time.sleep(2)
        Base.bottom_skip(self,"2000")
        self.find_element(*self.nopraise_buttonone).click()
        self.find_element(*self.tickling_commit).click()
        Base.if_tip(self,"请填写评论",self.tickings_tip)
        time.sleep(2)
        self.find_element(*self.close_ticklingbox).click()
        self.find_element(*self.back_to_top).click()
        time.sleep(2)
        self.find_element(*self.lists).click()
        self.find_element(*self.list_one).click()
        time.sleep(2)
        self.find_element(*self.close_list).click()
        time.sleep(2)

    def change(self):
        Last.one_box_disappear(self)
        Base.bottom_skip(self,"15500")
        time.sleep(4)
        self.find_element(*self.changing).click()
        time.sleep(1)
        self.find_element(*self.change_url).click()
        time.sleep(3)
        return Base.find_currenturl(self)

    def guess(self):
        Last.one_box_disappear(self)
        Base.bottom_skip(self,"20000")
        time.sleep(2)
        self.find_element(*self.download_close).click()
        self.find_element(*self.bottom_hotguess).click()
        time.sleep(2)
        return Base.find_currenturl(self)

    def fineguess(self):
        Last.one_box_disappear(self)
        Base.bottom_skip(self,"14000")
        time.sleep(4)
        self.find_element(*self.fine_guess).click()
        time.sleep(2)
        #return Base.find_currenturl(self)
        current_url = self.driver.current_url
        params = parse.urlparse(current_url).path#获取url的参数与参数值
        return params
        # shopping_id ="".join(params['id'])#将列表转化为字符串
        # shopping_url="https://shop.zelingyu.cn/index.php?s=shop&c=order&a=checkout&id="+ shopping_id +"&channel=test"

    def shopping(self):
        Last.one_box_disappear(self)
        Base.bottom_skip(self,"12000")
        time.sleep(2)
        self.find_element(*self.good_picture).click()
        time.sleep(2)
        self.find_element(*self.goodbox_cancel).click()
        time.sleep(2)
        self.find_element(*self.stay_buy).click()
        self.find_element(*self.goodbox_cancel).click()
        time.sleep(2)
        self.find_element(*self.stay_cancel).click()
        time.sleep(2)
        self.find_element(*self.good_picture).click()
        time.sleep(2)
        self.find_element(*self.goodbox_buy).click()
        Base.if_tip(self,"姓名不能为空！",self.box_tip)
        time.sleep(1)
        Base.send_keys(self, self.goodname_input, "测试")
        self.find_element(*self.goodbox_buy).click()
        Base.if_tip(self,"联系电话不能为空！",self.box_tip)
        time.sleep(1)
        Base.send_keys(self, self.goodphone_input, "测试")
        self.find_element(*self.goodbox_buy).click()
        Base.if_tip(self,"联系电话格式不正确！",self.box_tip)
        time.sleep(1)
        self.find_element(*self.goodphone_input).clear()
        Base.send_keys(self, self.goodphone_input, "5326")
        self.find_element(*self.goodbox_buy).click()
        Base.if_tip(self,"联系电话格式不正确！",self.box_tip)
        time.sleep(1)
        self.find_element(*self.goodphone_input).clear()
        Base.send_keys(self, self.goodphone_input, "123456")
        self.find_element(*self.goodbox_buy).click()
        Base.if_tip(self,"省市区选择不能为空",self.box_tip)
        time.sleep(1)
        self.find_element(*self.goodnumber_add).click()
        time.sleep(1)
        self.find_element(*self.goodnumber_cut).click()
        time.sleep(1)
        self.find_element(*self.goodadress_input).click()
        time.sleep(1)
        self.find_element(*self.goodadress_cancel).click()
        time.sleep(1)
        self.find_element(*self.goodadress_input).click()
        self.find_element(*self.goodadress_check).click()
        self.find_element(*self.goodbox_buy).click()
        Base.if_tip(self,"详细地址不能为空！",self.box_tip)
        time.sleep(1)
        Base.send_keys(self, self.gooddetailadress_input, "测试")
        self.find_element(*self.goodbox_buy).click()
        self.driver.back()
        time.sleep(2)
        #action=ActionChains(self.driver)
        #action.drag_and_drop(self.adress_beijing,self.adress_neimenggu).perform()鼠标拖动地区
        current_url = self.driver.current_url
        params = parse.parse_qs(parse.urlparse(current_url).query)#获取url的参数与参数值
        shopping_id ="".join(params['id'])#将列表转化为字符串
        shopping_url="https://shop.zelingyu.cn/index.php?s=shop&c=order&a=checkout&id="+ shopping_id +"&channel=test"
        if current_url == shopping_url:
            print("跳转正确")
        else:
            print("跳转错误")
        time.sleep(1)
        self.driver.back()
        time.sleep(2)

