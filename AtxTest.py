#!/usr/bin/Python
# -*- coding: utf-8 -*-

# import  atx
# from Adbtool import *
# from  atx.ext import report
# from  atx.drivers.android import AndroidDevice
# d = AndroidDevice(serialno="")
# rp = report.Report(d, save_dir='report')
#
#
# rp.patch_uiautomator()
# rp.info("Start test")
#
# if d is not None:
#     print "链接成功"
# d.start_app('tv.danmaku.bili')
# name = d.current_app()
# print name
# d.sleep(5.0)
# d.click_exists(text=u'未登录')
# # d.screenshot(filename='D:/denglu.png')
#
# d.click_exists(text =u'点击头像登录')
# # d.screenshot(filename='D:/denglu2.png')
import configparser
config=configparser.ConfigParser()
file1 = config.read('Localurl.ini')
temp = config.sections()
print config.get('global','ip')