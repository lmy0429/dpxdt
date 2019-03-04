import requests
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--site", required=True, help="the web name")
args = vars(ap.parse_args())
url = "http://101.207.235.205:5000/run"
data = {
    "site": args["site"]
}
response = requests.post(url,data)
