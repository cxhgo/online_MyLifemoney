# coding:utf-8
import logging
import os.path
import time
import inspect


class Log():
    def _init_(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)#log等级总开关

    def console(self,level,message):
        #创建一个handler，用于写入日志文件
        self.rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))[:-4]
        self.log_path = os.path.dirname(os.getcwd())+'/log/logs'
        self.log_name = self.log_path + self.rq + '.log'
        self.logfile =self.log_name
        fh =logging.FileHandler(self.logfile,mode='a',encoding='utf-8')#追加模式 pythom3的
        #fh = logging.FileHandler(self.logname, 'a')  # 追加模式  python2的
        fh.setLevel(logging.DEBUG)#输出到file的log等级的开关
        formatter = logging.Formatter("%(asctime)s -%(filename)s[line:%(lineno)d] -%(levelname)s:%(message)s")#日志输出格式
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        #handler输出控制台
        ch= logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        if level =='info':
            self.logger.info(message)
        elif level =='debug':
            self.logger.debug(message)
        elif level =='warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

    def debug(self, message):
        '''inspect.stack()获取当前运行代码的方法名，和行数'''
        msg = "%s__ %s line%s" % (inspect.stack()[1][3], message, inspect.stack()[1][2])
        self.console('debug', msg)

    def info(self, message):
        msg = "%s__ %s line%s" % (inspect.stack()[1][3], message, inspect.stack()[1][2])
        self.console('info', msg)

    def warning(self, message):
        msg = "%s__ %s line%s" % (inspect.stack()[1][3], message, inspect.stack()[1][2])
        self.console('warning', msg)

    def error(self, message):
        msg = "%s__ %s line%s" % (inspect.stack()[1][3], message, inspect.stack()[1][2])
        self.console('error', msg)
