# coding:utf-8
#from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunnerNew import HTMLTestRunner
import time
import unittest
import os
from page.test_order import Yscy_Order
from page.test_last import Yscy_Last
from page.send_report import unittest_smtp

def creat_report():
    test_dir = os.path.dirname(os.path.realpath(__file__))#获取脚本的父级相对路径，不包含脚本名
    #test_dir = os.path.dirname(os.path.abspath(__file__))#获取脚本的父级绝对路径，不包含脚本名
    #test_dir = os.path.abspath(__file__)获取脚本的绝对路径
    #test_dir = os.getcwd()#返回当前工作目录
    print(test_dir)
    #testunit = unittest.defaultTestLoader.discover(test_dir,pattern='test_first.py')#执行单个脚本生成报告
    #testunit = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')#执行路径下所有test开头的脚本生成报告
    testunit=unittest.TestSuite()#构建测试集
    testunit.addTest(unittest.makeSuite(Yscy_Order))#将多个脚本存放在一起后执行生成报告
    #testunit.addTest(unittest.makeSuite(Yscy_Last))
    now =time.strftime("%Y-%m-%d %H-%M-%S")#获取以可读字符串表示的当地时间
    filename=test_dir+ now +'test_result.html'#定义报告存放路径
    fp =open(filename,"wb")#以二进制格式打开文件只用于写入，如果文件存在则覆盖，如果文件不存在，创建新文件
    runner =HTMLTestRunner(stream= fp,
                           title=u"自动化测试报告",
                           description=u"测试用例执行情况：")#定义测试报告文件，文件标题、文件描述
    runner.run(testunit)#运行测试
    fp.close()#关闭报告文件
    unittest_smtp(filename)#发送邮件

if __name__=="__main__":
    creat_report()