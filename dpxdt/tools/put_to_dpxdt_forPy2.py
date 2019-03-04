# -*- coding: utf-8 -*-
# for python2
import base64
import os
import requests
import json
import datetime
import argparse
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def put_to_dpxdt(site, filename, base64_data):
    url = "http://10.110.30.10:5000/savefile"
    data = {
        "site": "{}".format(site),
        "filename": "{}".format(filename),
        "base64_data": "{}".format(base64_data)
    }
    response = requests.put(url, data)
    if response.status_code != 200:
        print "{} picture put error，error messages has been writed in PicToDpxdt_errolog.txt".format(filename)
        with open("PicToDpxdt_errolog.txt", "a") as f:
            f.write("{0} picture put error，error message({1})：{2}\n".format(filename, datetime.datetime.now(),
                                                                            response.content))
        return False
    else:
        res_data = json.loads(response.content.decode())
        print "{0}:{1}".format(filename, res_data["msg"])
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
                print "{0}picture typeerror，put to dpxdt is failed".format(fi)
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
print "Success:{0}; Error:{1},include{2}TypeError ".format(s, m + n, n).encode("utf-8")
