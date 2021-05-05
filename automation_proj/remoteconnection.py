#!/usr/bin/python3
from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
from datetime import datetime as t
import subprocess
import argparse
import os
import re
import datetime
import pymysql
import pandas as pd

# def parse_args(fake_args=None):
#     main_parser = argparse.ArgumentParser(prog='remotecheck.py')
#     main_parser.add_argument("-n", "--name", type=str, dest="device_name", required=True, help="inputcasenumber")
#     return main_parser.parse_args()

def get_date(days):
    cur=datetime.date.today()
    delta=datetime.timedelta(days=days)
    return str(cur-delta)

def cur_time():
    x=os.popen('date').read()
    l=[i for i in x if i.isalnum()]
    return "".join(l)

def build_directory(dir_name):
    try:
        os.mkdir(dir_name)
        print(dir_name+" was made at "+cur_time())
    except:print('Directory already existed')
    return

def deploycmd_noshow(box_name,cli_knob):
    if not box_name:
        print("stop here ,please re-run within the correct box name")
        return False
    try:
        ss = StartShell(Device(host=box_name, user='labroot', passwd='lab123'))
        ss.open()
        open=ss.run(cli_knob, this=None, timeout=5)
        ss.close()
        return True
    except:
        print(box_name+" is unreachable")
        return False

def getoutput(box_name,cli_knob,file_name,dir_name):
    if not box_name:
        print("stop here ,please re-run within the correct box name")
        return
    if not file_name:
        print("stop here ,please provide a name for file")
        return
    try:
        ss = StartShell(Device(host=box_name, user='labroot', passwd='lab123'))
        ss.open()
        command = cli_knob
        output = ss.run(command, this=None, timeout=5)
        temp=[]
        if output[0]:temp=output[1].replace("\r","").split("\n")
        else:
            print("nothing here")
            return 
        os.system('date'+' >>'+dir_name+'/'+file_name)
        str2='echo  \"{}\"'.format('#_# '*20)
        for i in temp:
            str1='echo  \"{}\"'.format(i)
            os.system(str1+' >>'+dir_name+'/'+file_name)
        os.system(str2+' >>'+dir_name+'/'+file_name)
        ss.close()
    except:
        print(box_name+" is unreachable")
    return

def record2mysql(sql_insert,values):
    con = pymysql.connect(host='10.85.209.89',
                      user='owencfts',
                      password='222121Wj',
                      db='attlab',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
    try:
        with con.cursor() as cur:
            for i in values:cur.execute(sql_insert,i)
            con.commit()
    finally:
        con.close()



if __name__ == '__main__':
    getoutput("","","","")
