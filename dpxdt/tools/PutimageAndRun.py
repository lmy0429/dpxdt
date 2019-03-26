# -*- coding: utf-8 -*-
# for python2
import base64
import os
import requests
import json
import datetime
import argparse
import sys
from time import sleep

reload(sys)
sys.setdefaultencoding('utf-8')


# put images to dpxdt
def put_to_dpxdt(site, filename_list, base64_data_list):
    url = "http://127.0.0.1/savefile"
    data = {
        "site": "{}".format(site),
        "filename_list": "{}".format(filename_list),
        "base64_data_list": "{}".format(base64_data_list)
    }
    response = requests.put(url, data)
    return response.content.decode()


def get_picpath_list(filepath):
    files = os.walk(filepath)
    file_path_list = []
    filenamelist = []
    for maindir, subdir, file_name_list in files:
        for fi in file_name_list:
            if fi[-3:] == "png":
                file_path_list.append(os.path.join(maindir, fi))
                filenamelist.append(fi[:-4])
            else:
                print "File Error :"
                print "{0} picture typeerror, put to dpxdt is failed".format(fi)
    return file_path_list, filenamelist


ap = argparse.ArgumentParser()
ap.add_argument("-s", "--site", required=True, help="the web name")
ap.add_argument("-p", "--filepath", required=True, help="the picture path")
args = vars(ap.parse_args())
file_path_list, filename_list = get_picpath_list(args["filepath"])
base64_data_list = []
for i in file_path_list:
    with open(i, 'rb') as f:
        base64_data = base64.b64encode(f.read()).decode()
        base64_data_list.append(base64_data)
result = put_to_dpxdt(args["site"], filename_list, base64_data_list)
print "Response from DPXDT :"
print result

# run dpxdt test
url_run = "http://127.0.0.1/runtest"
data = {
    "site": args["site"]
}
response = requests.post(url_run, data)
print response.content


# get test result
def wait_time():
    pic_num = len(filename_list)
    wait_time = pic_num * 10
    sleep(wait_time)


url_result = "http://127.0.0.1/testresult"
wait_time()
result_rs = requests.post(url_result, data)
print result_rs.content
