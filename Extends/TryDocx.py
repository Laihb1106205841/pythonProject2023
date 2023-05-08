import document
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import docx






path = "../Input.docx"  #你的推送文件地址
pathtxt = "666.txt"
#file = docx.getdocumenttext(path)
file2 = docx.opendocx(path)

print(docx.opendocx(path.format()))

obj = open(path, 'rb')
print(obj.read())

obj2 = open(path, 'rb')
print(obj2)

obj3 = open(pathtxt, 'r')

print(obj3)



ojbdocx = docx.opendocx(path)
ojb = docx.opendocx(path.title())
print(ojb)

for p in file2:
    print(p)


