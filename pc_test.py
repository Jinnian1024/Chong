# -*- coding: utf-8 -*-
#!/usr/bin/python
import time
import urllib
import sys
import os
import re
import atx,configparser
from Tkinter import *
from Adbtool import *
import tkMessageBox
import  math
reload(sys)
sys.setdefaultencoding('utf-8')

class game:

 def __init__(self):
    NuseDir =['F:\Download','D:\\']
    self.root = Tk()
    self.root.geometry('+800+400')
    self.root.minsize(800,400)
    self.cnames =StringVar()
    self.tnames =StringVar()
    self.v = IntVar()
    self.frame  = Frame(self.root,bg ='red',width = 20)
    self.frame1  = Frame(self.root,width = 60)
    self.frame.grid(row = 0,column =1)
    self.frame1.grid(row = 3,column =0)
    self.tbutton = Button(self.frame,command = Download,text = '下载安装',width = 20).grid(row = 0,column =0)
    self.l = Listbox(self.root,listvariable = self.cnames,selectmode = BROWSE,width = 80,selectbackground='red')
    self.l1= Listbox(self.frame1,listvariable = self.tnames,selectmode = BROWSE,width = 30,selectbackground='red')
    for i in NuseDir:
        self.l1.insert(0,i)
    self.l.grid(row = 0,column =0)
    self.l1.grid(row = 1,column =0)
    self.gbutton1 = Button(self.frame,command = dev_list,text = 'Get_Dev_List',width = 20).grid(row = 1,column =0)
    self.gbutton2 = Button(self.frame,command = sta_list,text = 'Get_Sta_List',width = 20).grid(row = 2,column =0)
    self.lujin =StringVar()
    self.Kobe = Entry(self.root,width = 80,relief ="sunken",textvariable = self.lujin)
    self.Kobe.grid(row = 1, column = 0)
    self.gbutton3 = Button(self.frame1,command = get_file,text = 'Get_Files',width = 15).grid(row = 0,column =0)
    self.gbutton4 = Button(self.frame1,command = fileapk,text = '安装',width = 15).grid(row = 0,column =1)

def hello(log):
   tkMessageBox.showinfo(message= log)

def get_file():
    if qqgues.lujin.get()=='':
        hello("路径不能为空")
    else:
        qqgues.cnames.set('')
        allfile = os.listdir(qqgues.lujin.get())
        for i in allfile:
            if '.apk' in i:
                qqgues.l.insert(0,i.decode('gbk'))

def getHtml(html):
    reg = r'title="(.*?)">s'

    reg2 =r'href="(.*?)">q'
    APK = re.compile(reg)
    Apklist = re.findall(APK,html)
    for i in Apklist:
        if '.apk' not in i:
            Apklist.remove(i)
    # APK2 = re.compile(reg2)
    # Apklist2 = re.findall(APK2,html)
    # Apklist =Apklist+Apklist2
    return Apklist


def progressbar(num,cur,total):
    percent = '{:.2%}'.format(num*cur*1.0/ total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' % ( '=' * int(math.floor(num*cur * 50 /total)),percent))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')



def dev_list():
    url1 = 'http://10.0.4.14:9257/dev/android_cn/'
    page = urllib.urlopen(url1).read()
    apknameList = getHtml(page)
    qqgues.cnames.set('')
    apknameList.append("网址 ：  "+url1)
    for i in apknameList:
            qqgues.l.insert(0,i)

def sta_list():
    url2 = 'http://10.0.4.14:9257/stable/android_cn/sy/big/'
    page = urllib.urlopen(url2).read()
    apknameList = getHtml(page)
    apknameList.append("网址 ：  "+url2)
    qqgues.cnames.set('')
    for i in apknameList:
            qqgues.l.insert(0,i)

def Download():
    url1 = 'http://10.0.4.14:9257/dev/android_cn/'
    url2 = 'http://10.0.4.14:9257/stable/android_cn/sy/big/'
    index = qqgues.l.curselection()
    local = 'd:\\'
    print qqgues.l.get(index)
    print qqgues.v.get()
    if qqgues.v.get() == 1:
        apkname = qqgues.l.get(index)
        url = url2+apkname
        print "下载的apk路径： "+url
        print "------------------------------downloading----------------------------"
        urllib.urlretrieve(url,local+apkname,progressbar)
    else:
        apkname = qqgues.l.get(index)
        url = url1+apkname
        print "下载的apk路径： "+url
        print "------------------------------downloading----------------------------"
        urllib.urlretrieve(url,local+apkname,progressbar)
    print '\n'
    print "--------------------------Finished--------------------------------"
    print 'Apk download url ：' +local+apkname
    suces = AdbTools()
    suces.install(local+apkname)

def fileapk():
    suces1 = AdbTools()
    index = qqgues.l.curselection()
    Apkurl = qqgues.lujin.get()+'\\'+qqgues.l.get(index)
    print Apkurl
    if '.apk' in Apkurl:
            suces1.install(Apkurl)
    else:
        print u'文件非法'
if __name__ =='__main__':
    qqgues = game()
    qqgues.root.mainloop()