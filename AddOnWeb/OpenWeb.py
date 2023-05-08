from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def OnWeb(url,EMailName,Password,driver):
    #driver = webdriver.Chrome()
    driver.get(url)  # 访问
    driver.maximize_window()  # 大屏幕

    time.sleep(1)  # 休息庆祝一下

    login = driver.find_element(By.NAME, 'email').send_keys(EMailName)
    passwordCode = driver.find_element(By.NAME, 'password').send_keys(Password)  # 填写账号密码

    time.sleep(1)
    button = driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div[1]/form/div[4]/button").click()
    # 进入！

    time.sleep(1)
    button2 = driver.find_element(By.XPATH, '//*[@id="tn_xiumi_header_navbar_nav"]/ul/li[1]/a').click()

    time.sleep(1)

    url2 = 'https://xiumi.us/studio/v5#/paper'
    driver.get(url2)

    time.sleep(1)
    # 登录成功！开始作业

def BasicSettings(Head,Summary,Links,Author,driver):
    Heading = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/input').send_keys(
        Head)
    time.sleep(0.2)
    Summaried = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/textarea').send_keys(
        Summary)
    time.sleep(0.2)
    Linked = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[3]/div[1]/div/div[2]/div[2]/input').send_keys(
        Links)
    time.sleep(0.2)
    Authorized = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[3]/div[1]/div/div[2]/div[1]/input').send_keys(
        Author)
    time.sleep(0.2)

def Write(MainPassage,driver):
    zhai = '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/textarea'
    # 为了刷新文本的xpath
    Ma = '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div[3]/div[2]/div[1]/article/section/div[2]/div/div/div/div/div/section/div/div/div/section/div[2]/div[1]/div/div/section/div'
    # 第一次所使用的xpath
    Clickp = '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div[3]/div[2]/div[1]/article/section/div[2]/div/div/div/div/div/section/div/div/div/section/div[2]/div[1]/div/div/section/div/p'
    # 后边所使用的xpath

    driver.find_element(By.XPATH,Ma).click()
    driver.find_element(By.XPATH,Ma).send_keys(MainPassage[5])
    driver.find_element(By.XPATH, zhai).click()

    #
    # MainedB = driver.find_element(By.XPATH,Clickp).click()
    #
    # Mained4 = driver.find_element(By.XPATH,
    #                               '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div/menu[2]/li[21]/div/div/div[2]/button').click()
    #
    # time.sleep(0.5)
    # Pass = driver.find_element(By.XPATH,
    #                            '/html/body/div[1]/div[1]/div[1]/div/div/div/div[3]/div/div[3]/div[2]/div[1]/article/section/div[2]/div/div/div/div/div/section/div/div/div/section/div[2]/div[1]/div/div/section/div').click()
    #
    # pt = driver.find_element(By.XPATH,
    #                          Clickp).send_keys(
    #     MainPassage[5]
    # )



    driver.find_element(By.XPATH,Clickp).click()
    driver.find_element(By.XPATH,Clickp).send_keys(MainPassage[5])
    driver.find_element(By.XPATH, zhai).click()

    for i in range(1, len(MainPassage)):
        driver.find_element(By.XPATH, Clickp).click()
        driver.find_element(By.XPATH, Clickp).send_keys(MainPassage[i])
        driver.find_element(By.XPATH, zhai).click()
        time.sleep(0.1)


    time.sleep(2500)

    Save = driver.find_element(By.XPATH, '/html/body/div[1]/div/header/nav/div/div[1]/div/button[3]').click()

    time.sleep(50)