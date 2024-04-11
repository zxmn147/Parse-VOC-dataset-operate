import xml.etree.ElementTree as ET
import os
import argparse
from pathlib import Path

def checkargs(args):
    # check xml
    if not os.path.exists(args.xmlPath):
        raise FileNotFoundError("xmlPath not found")
    if  not os.path.isdir(args.xmlPath):
        raise Exception("xmlPath not folder")
    # check class.txt
    if not os.path.exists(args.originalClass):
        raise FileNotFoundError("originalClass label file not found")
    if not os.path.exists(args.newClass):
        raise FileNotFoundError("newClass label file not found")
    

def readLabel(file):
    className = []
    with open(file, 'r') as f:
        className = [i.strip() for i in f.readlines()]
    
    while className[-1] == "":
        className.pop()
        
    return className

def main(args):
    oLabel = readLabel(args.originalClass)
    nLabel = readLabel(args.newClass)
   
    if len(nLabel) > len(oLabel):
        raise FileNotFoundError("nLabel number more than oLabel number")
    elif len(oLabel) != len(nLabel):
        nLabel += ["" for i in range(len(oLabel) - len(nLabel))]
    
    mappingLabel = {k: v for k, v in zip(oLabel, nLabel)}

    p = Path(args.xmlPath)
    grepXML =  list(p.glob('*.xml'))
    for filePath in grepXML:
        tree = ET.parse(filePath, parser = ET.XMLParser(encoding = 'iso-8859-5'))
        root = tree.getroot()
        for obj in root.findall("object"):
            if obj[0].text != mappingLabel[obj[0].text]:
                if mappingLabel[obj[0].text] == "":
                    # print(f'remove: {obj[0].text}')
                    root.remove(obj)
                else:
                    # print(f'replcae: {obj[0].text} to {mappingLabel[obj[0].text]}')
                    obj[0].text = mappingLabel[obj[0].text]

        tree.write(filePath)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--xmlPath', type=str, required=True, help='xml folder Path')
    parser.add_argument('--originalClass', type=str, default='original.txt', required=True, help='original className file')
    parser.add_argument('--newClass', type=str, required=True, help='new className file')
    args = parser.parse_args()
    checkargs(args)
    main(args)
    

    
