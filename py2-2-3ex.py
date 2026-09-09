import json
import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

##data=[
##  {
##    "機構名稱": "森美牙醫診所",
##    "縣市別代碼": "10018",
##    "行政區域代碼": "10018020",
##    "街道項弄號": "大同里中正路111號1樓、2樓",
##    "負責人": "李森孟",
##    "電話": "(03)5260203"
##  },
##  {
##    "機構名稱": "黃啟祥牙醫診所",
##    "縣市別代碼": "10018",
##    "行政區域代碼": "10018020",
##    "街道項弄號": "和福街105號",
##    "負責人": "黃啟祥",
##    "電話": "(03)5269095"
##  },
##  {
##    "機構名稱": "福華牙醫診所",
##    "縣市別代碼": "10018",
##    "行政區域代碼": "10018020",
##    "街道項弄號": "育英里四維路54號1樓",
##    "負責人": "吳英法",
##    "電話": "(03)5262345"
##  },
##  {
##    "機構名稱": "親民牙醫診所",
##    "縣市別代碼": "10018",
##    "行政區域代碼": "10018020",
##    "街道項弄號": "竹光路２１號",
##    "負責人": "黃宏正",
##    "電話": "(03)5427027"
##  },
##  {
##    "機構名稱": "如意牙醫診所",
##    "縣市別代碼": "10018",
##    "行政區域代碼": "10018020",
##    "街道項弄號": "光田里水田街131號",
##    "負責人": "呂正德",
##    "電話": "(03)5422765"
##  }
##  ]

url = "https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/106/94b0e54b-ad45-4222-b26c-648773794ded.json"

##data = requests.get(url, verify=False).json()

##response = requests.get(url, timeout=20, verify=False)
##response.raise_for_status()
##data =  response.json()
try:
    response = requests.get(url, timeout=20, verify=False)
    response.raise_for_status()
    data =  response.json()
except requests.exceptions.SSLError as e:
    print("requests.exceptions.SSLError例外,SSLCerVerificationError")
    print(e)
    

with open("dental_clinics.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False,indent=4)
with open("dental_clinics.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    for clinic in loaded_data:
##        print(clinic)
##        for field in clinic:
##          print(clinic[field])
            print(clinic["機構名稱"],clinic["電話"])
            print()    





    


