#!/usr/bin/Python
# -*- coding: utf-8 -*-


import os
from os import path
GLEX_VERTEX = "#a_Position"
GLEX_NORMAL ="#a_Normal"
GLEX_TEXCOORD = "#a_TexCoord"
GLEX_TEXCOORD1 = "#_glesMultiTexCoord1"


GLEX_VERTEX_PANDA = "#position"
GLEX_NORMAL_PANDA="#normal"
GLEX_TEXCOORD_PANDA = "#texcoord0"
GLEX_TEXCOORD1_PANDA ="#texcoord1"

OBJ_VERTEX= "v"
OBJ_NORMAL ="vn"
OBJ_UV = "vt"
OUTPUT_DIR ="Output"

def OutputObj(srcObjPath,dstObjPath):
    fileNewObj = open (dstObjPath,"w+")
    fileObj = open(srcObjPath,"r")

    for line in fileObj:
        index = line.find(' ')
        beginStr = line[0:index]

        if beginStr == GLEX_VERTEX:
            line = OBJ_VERTEX + line[index:]
        elif beginStr == GLEX_VERTEX_PANDA:
            line = OBJ_VERTEX + line[index:]
        elif beginStr == GLEX_NORMAL:
            line = OBJ_NORMAL + line[index:]
        elif beginStr == GLEX_NORMAL_PANDA:
            line = OBJ_NORMAL + line[index:]
        elif beginStr == GLEX_TEXCOORD:
            line = OBJ_UV + line[index:]
        elif beginStr == GLEX_TEXCOORD1:
            line = OBJ_UV + line[index:]
        elif beginStr == GLEX_TEXCOORD_PANDA:
            line = OBJ_UV + line[index:]
        elif beginStr == GLEX_TEXCOORD1_PANDA:
            line = OBJ_UV + line[index:]
        fileNewObj.write(line)
    fileObj.close()
    fileNewObj.flush()
    fileNewObj.close()
    print  "----------------------" + dstObjPath


def ScanDir (curPath , savePath, isRecursive):
    listFile = os.listdir(curPath)
    for fileName in listFile:
        filePath = path.join(curPath,fileName)
        if isRecursive:
            if path.isdir(filePath) and fileName != OUTPUT_DIR:
                saveDirPath =path.join(savePath,fileName)
                if not path.exists(savePath):
                    os.mkdir(savePath)
                ScanDir(filePath,saveDirPath, isRecursive)



        if path.isfile(filePath) and fileName.lower().endswith("obj"):
            strObjPath = path.join(curPath,fileName)
            dstObjPath = path.join(savePath,fileName)
            OutputObj(strObjPath,dstObjPath)

def SelectMode():
    print "Select Run MOde: \n" \
    "1 Input 1 : Not Recursive\n" \
    "2 Input 2 : Is Recursive\n"

    mode = int(raw_input())
    if mode !=1 and mode !=2:
        print mode
        print "Wrong input Number"
        SelectMode()
    else:
        curdir = os.getcwd()
        outputPath = os.path.join(curdir,OUTPUT_DIR)

        if not os.path.exists(outputPath):
            os.mkdir(outputPath)
            print '------'+outputPath+'--------'
        isRecursive = True
        if mode ==1:
            isRecursive =True
        elif mode ==2:
            isRecursive =False
        ScanDir(curdir,outputPath,isRecursive)

        print '\n All OBJ files Complete'

if __name__ =="__main__":
    SelectMode()


