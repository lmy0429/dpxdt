# -*- coding: utf-8 -*-
import base64
import os
import requests
import json
import datetime
import argparse
'''
该脚本使用Python3语法
'''

def put_to_dpxdt(site, filename, base64_data):
    url = "http://127.0.0.1:5000/savefile"
    data = {
        "site": "{}".format(site),
        "filename": "{}".format(filename),
        "base64_data": "{}".format(base64_data)
    }
    response = requests.put(url, data)
    if response.status_code != 200:
        print("{}图片其他异常，请查看当前目录下PicToDpxdt_errolog.txt日志文件了解详细信息！".format(filename))
        with open("PicToDpxdt_errolog.txt", "a") as f:
            f.write("{0}上传图片出错，错误信息({1})：{2}\n".format(filename, datetime.datetime.now(), response.content))
        return False
    else:
        res_data = json.loads(response.content.decode())
        print("{0}:{1}".format(filename, res_data["msg"]))
        return True


def get_picpath_list(filepath):
    files = os.walk(filepath)
    file_path_list = []
    filenamelist = []
    s = 0
    for maindir, subdir, file_name_list in files:
        for fi in file_name_list:
            if fi[-3:] == "png":
                file_path_list.append(os.path.join(maindir, fi))
                filenamelist.append(fi[:-4])
            else:
                s += 1
                print("{0}图片格式不正确，上传dpxdt服务器失败".format(fi))
    return file_path_list, filenamelist, s


ap = argparse.ArgumentParser()
ap.add_argument("-s", "--site", required=True, help="the web name")
ap.add_argument("-p", "--filepath", required=True, help="the picture path")
args = vars(ap.parse_args())
file_path_list, filename, n = get_picpath_list(args["filepath"])
s, m, q = 0, 0, 0
for i in file_path_list:
    with open(i, 'rb') as f:
        base64_data = base64.b64encode(f.read()).decode()
        result = put_to_dpxdt(args["site"], filename[q], base64_data)
    if result is True:
        s += 1
    else:
        m += 1
    q += 1
print("累计上传成功{0}张图片；{1}张上传出错,其中{2}张格式错误".format(s, m + n, n))
