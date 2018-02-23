#!/usr/bin/Python
# -*- coding: utf-8 -*-

import uiautomator2 as ut2
import threading
from time import ctime,sleep
ip_list1 =['10.2.8.138:7912','10.2.8.113:7912','10.2.8.34:7912','10.2.8.148:7912']
ip_list =['10.2.8.113:7912','10.2.8.138:7912']
url = 'http://10.0.4.14:9257/dev/android_cn/'
apkName = 'snqz_banshu_0.0.0.008_1711071629.apk'
dev_packname ='com.snqz.union'
jm_packname='com.jingmo.snqz'
flag = input("dev：1  :  jingmo : 2   \n")
def apk_install(ip):
    u = ut2.connect(ip)
    thread_name = threading.current_thread().getName()
    print  thread_name + "---" + u.device_info['brand'] + "---" +'  starting'
    if flag == 1:
        if u.app_isExist(dev_packname):
            u.app_uninstall(dev_packname)
        u.app_install(url+apkName)
        print 'Brand: '+ u.device_info['brand'] +'--------' + apkName + '\n Install sucess'
        u.app_start(dev_packname)
    else:
        if u.app_isExist(jm_packname):
            u.app_uninstall(jm_packname)
        u.app_install(url+apkName)
        print 'Brand: '+ u.device_info['brand'] +'--------' + apkName + '\n Install sucess'
        u.app_start(jm_packname)

threads = []
files = range(len(ip_list))
for i in files:
    t = threading.Thread(target=apk_install,args=(ip_list[i],))
    threads.append(t)

if __name__ == '__main__':

    for i in files:
        threads[i].start()
    #print threading.enumerate()
for i in files:
    threads[i].join()
print 'end:%s' %ctime()
