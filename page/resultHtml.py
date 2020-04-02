# coding:utf-8
#from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunnerNew import HTMLTestRunner
import time
import unittest
import os

test_dir = os.path.dirname(os.path.realpath(__file__))
print(test_dir)
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_first.py')
if __name__=="__main__":
    #获取当前时间
    now =time.strftime("%Y-%m-%d %H-%M-%S")
    #定义报告存放路径
    filename=test_dir+ now +'test_result.html'
    fp =open(filename,"wb")
    #以二进制格式打开文件只用于写入，如果文件存在则覆盖，如果文件不存在，创建新文件
    runner =HTMLTestRunner(stream= fp,
                           title=u"自动化测试报告",
                           description=u"测试用例执行情况：")
    runner.run(discover)#运行测试
    fp.close()#关闭报告文件