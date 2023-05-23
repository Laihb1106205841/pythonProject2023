

def OpenTxt(path):
    f = open(path, "r", encoding='utf-8')
    data2 = f.readline()

    for line in f.readlines():
        line = line.strip('\n')  # 去掉列表中每一个元素的换行符
        print(line)

    print("\n")

    with open(path, "r", encoding='utf-8') as f:  # 打开文件
        try:
            word = f.read()  # 读取文件
            print("读取txt文件成功！文件内容为：")
            # print(word)
        except:
            print("读取txt文件失败！")

    try:
        with open(path, "r", encoding='utf-8') as f:
            data = f.readlines()

            for i in range(len(data)):
                data[i] = data[i].strip('\n')


            print(data)
            Num = LoadInfos(data)
            return Num
    except:
        print("不是成功的")
        return "读取失败"


def LoadInfos(data):
    Head = data[0]
    Summary = data[1]
    Links = "http://baidu.com"
    Author = "树德书院宣传中心"

    Title = data[2]
    MainPassage = data[2]

    tus = []



    for line in data:

        tu = '图'
        if(tu in line):
            tus.append(tu)


    print("标题是：",Head)
    print("推送摘要是:",Summary)

    Num = (Head,Summary,Links,Author,Title,MainPassage,tus,data)
    return Num