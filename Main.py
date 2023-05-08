from selenium import webdriver
import LoadText.Loading as Loading
import AddOnWeb.OpenWeb as OpenWeb

url = 'https://xiumi.us/auth#/'
# 秀米的网址

EMailName = "sdc@sustc.edu.cn"
Password = "shudenumber1"


# 树德书院的邮箱和密码

class Txt2Web():
    path = "666.txt"
    # 你的txt文件
    driver = webdriver.Chrome()
    txt = ()


    def OpenTxts(self,path):
        data = Loading.OpenTxt(path)
        return data

    def OnWeb(self, u, E, P, driver=driver):
        Web = OpenWeb.OnWeb(u,E,P,driver)

    def OpenBasic(self, txt, driver=driver):
        Basic = OpenWeb.BasicSettings(txt[0],txt[1],txt[2],txt[3],driver)

    def Write(self, data, driver=driver):
        OpenWeb.Write(data, driver)



if __name__ == '__main__':

    txt1 = Txt2Web()

    data = txt1.OpenTxts(txt1.path)
    txt1.txt = data
    # 导入txt,处理txt

    txt1.OnWeb(url, EMailName, Password)
    txt1.OpenBasic(txt1.txt)
    # 网络基本配置
    txt1.Write(data[-1])