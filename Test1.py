#!/usr/bin/Python
# -*- coding: utf-8 -*-
import uiautomator2 as ut2
ip_list =['10.2.8.138:7912','10.2.8.113:7912','10.2.8.34:7912']
url = 'http://10.0.4.14:9257/dev/android_cn/'
#apkName = 'snqz_banshu_0.0.0.008_1711071629.apk'
apkName ='snqz_test_0.0.0.013_1801241755.apk'
pack_name = ['com.jingmo.snqz','com.snqz.union']
dev_packname ='com.snqz.union'
jm_packname='com.jingmo.snqz'
#flag = raw_input("dev：1  :  jingmo : 2   \n")
def apk_install(ip):
    u = ut2.connect(ip)
    print u.device_info
    print u.info
    print u.info.get('screenOn')
    #u.unlock()
    #u._default_session.screen_on()
    u.app_install(url+apkName)
    #u.push_url(url+apkName,'./storage/sdcard0/')
    # if flag == 1:
    #     if u.app_isExist(dev_packname):
    #         u.app_uninstall(dev_packname)
    #     else:
    #         u.app_install(url+apkName)
    #         u.app_start(dev_packname)
    # else:
    #     if u.app_isExist(jm_packname):
    #         u.app_uninstall(jm_packname)
    #     else:
    #         u.app_install(url+apkName)
    #         u.app_start(jm_packname)
#apk_install('10.2.8.148:7912')
apk_install('10.2.8.138:7912')