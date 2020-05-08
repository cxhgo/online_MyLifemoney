from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib

def _format_address(text):
      name,address=parseaddr(text)#解析邮件地址的函数,返回一个tuple
      return formataddr((Header(name,"utf-8").encode(),address))#构建邮件地址的，传入一个tuple，返回str

def unittest_smtp(filename):
      from_address="chenxiaohuan@linghit.com"#发送人邮箱
      password="Xh940107"#授权密码，有的邮箱是登录密码
      to_address=["chenxiaohuan@linghit.com",";","857227598@qq.com"]#收件人邮箱，可添加多个，有坑，没有标点符号可以隔开邮箱显示
      smtp_server="smtp.exmail.qq.com"#发送邮箱服务器地址
      message=MIMEMultipart()#定义整个邮件体
      message["From"]=_format_address("自动化测试报告<%s>"%from_address)#发送人邮箱
      #message["To"]=_format_address("陈晓欢<%s>"%to_address)#收件人地址，不适合多人
      message["To"]="".join(to_address)#多个收件人需要转化为字符串才能显示在收件人那栏
      message["Subject"]=Header("自动化测试报告","utf-8").encode()#邮件标题
      message.attach(MIMEText("发送测试报告","plain","utf-8"))#邮件正文内容、正文类型（如text/plain、text/html）、正文编码
      #att1=MIMEText(open("F:\\MyLifemoney\\page2020-05-07 18-12-38test_result.html","rb").read(),"base64","utf-8")#打开报告的地址
      att1=MIMEText(open(filename,"rb").read(),"base64","utf-8")#读取对应路径文件作为附件
      att1["Content-Type"]="application/octet-stream"#附件内容类型
      att1["Content-Disposition"]='attachment; filename=test_result.html'#附件名称
      message.attach(att1)
      try:
         server=smtplib.SMTP(smtp_server)#发件人邮箱中的SMTP服务器，端口
         server.set_debuglevel(1)#打开debug输出模式
         server.login(from_address,password)#登录smtp服务器， 发件人邮箱账号、邮箱授权码
         server.sendmail(from_address,to_address,message.as_string())#发送邮件,as_string()是将邮件体对象转化为str
         server.quit()
      except smtplib.SMTPException as e:
         print("Error:无法发送邮件",e)#打印报错信息
