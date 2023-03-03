import document
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import docx

path = "Input.docx"#你的推送文件地址


#############################################确定输入网址与登录账号、密码
url = 'https://xiumi.us/auth#/'
#秀米的网址

EMailName = "sdc@sustc.edu.cn"
Password  = "shudenumber1"
#树德书院的邮箱和密码



#############################################登录秀米，开始作业
driver = webdriver.Chrome()

driver.get(url)#访问
driver.maximize_window()#大屏幕

time.sleep(1)#休息庆祝一下

login = driver.find_element(By.NAME, 'email').send_keys(EMailName)
passwordCode = driver.find_element(By.NAME, 'password').send_keys(Password)#填写账号密码

time.sleep(1)
button = driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/form/div[4]/button").click()
#进入！


time.sleep(1)
button2 = driver.find_element(By.XPATH, '//*[@id="tn_xiumi_header_navbar_nav"]/ul/li[1]/a').click()

time.sleep(1)

url2 = 'https://xiumi.us/studio/v5#/paper'
driver.get(url2)

time.sleep(1)
#登录成功！开始作业

##################################开始输入文字

Head ="树德书院推送标题"
Summary ="推送摘要"
Links = "http://baidu.com"
Author ="树德书院宣传中心"

Title = "这是一个标题"
MainPassage ="这是正文，如果它保留下来了，那就是最好的"


##################基础配置

Heading = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/input').send_keys(Head)
Summaried =driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/textarea').send_keys(Summary)
Linked =driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[3]/div[1]/div/div[2]/div[2]/input').send_keys(Links)
Authorized =driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[3]/div[1]/div/div[2]/div[1]/input').send_keys(Author)


##################文章内容设置

#Title1 =driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/ul/li[1]/ul/li[1]/a').click()
#Title12=driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[3]/div/div[2]/div[3]/ul/li[1]').click()
#time.sleep(5)

Mained = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div[3]/div[2]/div[1]/article/section/div[2]/div/div/div/div/div/section/div/div/div/section/div[2]/div[1]/div/div/section/div').click()
Mained2 =driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div[3]/div[2]/div[1]/article/section/div[2]/div/div/div/div/div/section/div/div/div/section/div[2]/div[1]/div/div/section/div').send_keys(MainPassage)


time.sleep(50)