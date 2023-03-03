
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import docx

path = "D:\Python\pythonProject2023\Input.docx"

url = 'https://xiumi.us/auth#/'
#秀米的网址

EMailName = "sdc@sustc.edu.cn"
Password  = "shudenumber1"
#树德书院的邮箱和密码

driver = webdriver.Chrome()

driver.get(url)#访问
driver.maximize_window()#大屏幕

time.sleep(0.5)#休息庆祝一下

login = driver.find_element(By.NAME, 'email').send_keys(EMailName)
passwordCode = driver.find_element(By.NAME, 'password').send_keys(Password)#填写账号密码

time.sleep(0.5)
button = driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/form/div[4]/button").click()
#进入！


time.sleep(0.5)
button2 = driver.find_element(By.XPATH, '//*[@id="tn_xiumi_header_navbar_nav"]/ul/li[1]/a').click()

time.sleep(0.5)

url2 = 'https://xiumi.us/studio/v5#/paper'
driver.get(url2)

time.sleep(1)



#file = docx.getdocumenttext(path)
file2 = docx.opendocx(path)


for p in file2:
    print(p)

input()
