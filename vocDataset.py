import xml.etree.ElementTree as ET
import os
import argparse
from pathlib import Path

# file_path = input('.xml資料夾: ')
# p = Path(file_path)
# grep_json =  list(p.glob('*.xml'))

# for _ in grep_json:
#     tree = ET.parse(_, parser = ET.XMLParser(encoding = 'iso-8859-5'))
#     root = tree.getroot()
#     for obj in root.iter("object"):
#         # print(obj.text)
#         if obj[0].text in ['car_CY', 'car_Doll', 'car_Police', 'car_Postal', 'car_Taxi', 'car_Amb']:
#             obj[0].text = 'car'
#         elif obj[0].text in ['truck_CYF', 'truck_CYA', 'truck_Postal', 'truck_ENG']:
#             obj[0].text = 'truck'
#         elif obj[0].text in ['spc_Cement', 'spc_Recycling', 'spc_WaterTruck', 'spc_Garbage', 'spc_hearse', 'spc_TankTruck']:
#             obj[0].text = 'spc'
#         else:
#             obj[0].text = obj[0].text
    
#     tree = ET.ElementTree(root)
#     tree.write(_)
def checkargs(args):
    if not os.path.exists(args.xmlPath):
        raise FileNotFoundError("xmlPath not found")
    if  not os.path.isdir(args.xmlPath):
        raise Exception("xmlPath not folder")

def readXML(filePath):
    pass
    
def readLabel(file):
    className = []
    with open(file, 'r') as f:
        for label in enumerate(f.read().split('\n')):
            className.append(label)
    return className


def main(args):
    checkargs(args)
    print(args.replace)
    # p = Path(args.xmlPath)
    # grepXML =  list(p.glob('*.xml'))
    # for filePath in grepXML:
    #     readXML(filePath)
#     tree = ET.parse(_, parser = ET.XMLParser(encoding = 'iso-8859-5'))
#     root = tree.getroot()
#     for obj in root.iter("object"):
    # else:
    #     print(False)
    # grep_json =  list(p.glob('*.xml'))
    # print(grep_json)
# def readXML(args):
#     p = Path(args.xmlPath)
#     grep_json =  list(p.glob('*.xml'))
    # clas = {}

# for _ in grep_json:
#     tree = ET.parse(_, parser = ET.XMLParser(encoding = 'iso-8859-5'))
#     root = tree.getroot()
#     for obj in root.iter("object"):
#         # print(obj.text)
#         if obj[0].text in ['car_CY', 'car_Doll', 'car_Police', 'car_Postal', 'car_Taxi', 'car_Amb']:
#             obj[0].text = 'car'
#         elif obj[0].text in ['truck_CYF', 'truck_CYA', 'truck_Postal', 'truck_ENG']:
#             obj[0].text = 'truck'
#         elif obj[0].text in ['spc_Cement', 'spc_Recycling', 'spc_WaterTruck', 'spc_Garbage', 'spc_hearse', 'spc_TankTruck']:
#             obj[0].text = 'spc'
#         else:
#             obj[0].text = obj[0].text
    
#     tree = ET.ElementTree(root)
#     tree.write(_)
# 自定義解析函數，解析 value:value 格式的參數



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--xmlPath', type=str, required=True, help='xml folder Path')
    parser.add_argument('--originalClass', type=str, help='original className file')
    parser.add_argument('--newClass', type=str, help='new className file')
    parser.add_argument('--delete', type=str, help='new className file')
    args = parser.parse_args()
    
    
    if args.newClass is not None and args.originalClass is None:
        parser.error("--newClass 选用时 --originalClass 参数也必须使用")
    
