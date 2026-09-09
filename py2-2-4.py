import json

raw_data='''
    {
        "status":"success",
        "results":
            [
                {"id":1,
                "info":{
                    "name":"台北",
                    "weather":"雨"
                        }
                },
                {"id":2,
                "info": {
                    "name":"台中",
                    "weather":"晴"
                        }
                 }   
            ]
    }
        '''

try:
    data = json.loads(raw_data)
##    n 用來測試未定義的錯誤
    print("台中天氣:",data["results"][1]["info"]["weather"])
except json.decoder.JSONDecodeError as je:
    print(je)
except NameError as ne:
    print(ne)
except Exception as e: #越上層的類別盡量放後面
    print(e)


    



