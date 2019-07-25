# encoding: utf-8
'''
@author: Beck.yang
@contact: wb-ysc255177@alibaba-inc.com
@file: myBase_ini.py
@time: 2019-07-24 09:37
@desc: 
'''

import commands

#需要读取的文件
file_path ='/Users/bjc/.myBase7.ini'

#open函数读取文件
file_read = open(file_path,'r+')
#读取文件每一行
flists = file_read.readlines()
#for循环读取每一行匹配
for flist in flists:
    app = flist.split('=')[0]
    if app == 'App.UserLic.FirstUseOn':
        appname = flist.split('\n')[0]
        cmd = "sed -i \"\" \'/" + appname +"/d\' " + file_path
        ret,out = commands.getstatusoutput(cmd)
        if ret == 0:
            print '文件修改成功'