# encoding: utf-8
'''
@author: Beck.yang
@contact: wb-ysc255177@alibaba-inc.com
@file: myBase_ini.py
@time: 2019-07-24 09:37
@desc: 
'''

import commands

file_path ='/Users/bjc/.myBase7.ini'

fo = open(file_path,'r+')
flists = fo.readlines()
for flist in flists:
    app = flist.split('=')[0]
    if app == 'App.UserLic.FirstUseOn':
        appname = flist.split('\n')[0]
        cmd = "sed -i \"\" \'/" + appname +"/d\' " + file_path
        print cmd
        ret,out = commands.getstatusoutput(cmd)
        if ret == 0:
            print '文件修改成功'


