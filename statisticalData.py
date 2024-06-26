import xml.etree.ElementTree as ET
import os
import argparse
from pathlib import Path
import matplotlib.pyplot as plt

def checkargs(args):
    if not os.path.exists(args.xmlPath):
        raise FileNotFoundError("xmlPath not found")
    if  not os.path.isdir(args.xmlPath):
        raise Exception("xmlPath not folder")

def saveLabelFile(clas):
    with open('original.txt', 'w') as f:
        for i, label in enumerate(clas.keys()):
            if i != len(clas.keys())-1:
                f.writelines(label+'\n')
            else:
                f.writelines(label)

def drawHistogram(clas, args):
    # 資料
    # x, y
    categories = list(clas.keys()) 
    values = list(clas.values())  
    # 根據值的大小排序
    sortedData = sorted(zip(categories, values), key=lambda x: x[1], reverse=True)    # 繪製長條圖
    
    # 分離排序後的類別和值
    sortedCategories = [x[0] for x in sortedData]
    sortedValues = [x[1] for x in sortedData]

    plt.bar(sortedCategories, sortedValues)  
    # 在每個長條上加上值標籤
    for i in range(len(sortedCategories)):
        plt.text(i, sortedValues[i]+0.1, str(sortedValues[i]), ha='center')

    # 設定標題與標籤
    plt.title('Histogram of Data Distribution')
    plt.xticks(rotation=-20)

    if args.save:
        plt.savefig('Distribution.png')
        
    plt.show()
    
def statisticalData(args):
    p = Path(args.xmlPath)
    grep_json =  list(p.glob('*.xml'))
    clas = {}
    count = 0
    for _ in grep_json:
        tree = ET.parse(_, parser = ET.XMLParser(encoding = 'iso-8859-5'))
        root = tree.getroot()
        count +=1
        for obj in root.iter("object"):
            if obj[0].text in clas:
                clas[obj[0].text] = clas[obj[0].text] + 1
            else:
                clas[obj[0].text] = 1
    print(f'clas: {clas}')
    saveLabelFile(clas)
    drawHistogram(clas, args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--xmlPath', type=str, required=True, help='xml folder Path')
    parser.add_argument('--save', type=bool, default=True, help='save the Histogram img')
    args = parser.parse_args()
    checkargs(args)
    statisticalData(args)
