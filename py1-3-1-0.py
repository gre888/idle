##list1 = [10,30,60,20,50,40]
##
##print(list1)
##
##list2 = [10,30,60,20,50,40]
##
##list3=[
##    [10,20,30],
##    [40,50,60]
##    ]
##list1=[10,10,10]
##list2=[
##    ["1","2","3","4","5","6","7","8","9","10"],
##    ["11","12","13","14","15","16","17","18","19","20"],
##    ["21","22","23","24","25","26","27","28","29","30"],
##    ]
##
##print(list2[0][0])
##print(list2[0][1])
##print(list2[2][6])

##
##news_titles = ["台積電股價新高","AI概念股轉強","美股四大指數收紅"]
##news_data=[
##        ["台積電股價新高",15000],
##        ["AI概念股轉強",800],
##        ["美股四大指數收紅",1200]
##    ]
##print("第三則新聞",news_data[2][0])
##click_count=news_data[2][1]
##print(click_count)
##
##single_news={
##    "title":"台積電股價新高",
##    "clicks":1500,
##    "source":"財經日報"
##    }
##
##print("新聞標題",single_news["title"])
##print("新聞來源",single_news["source"])
##print("新聞來源",single_news.get("source"))
##
##
##all_news=[
##    {"title":"台積電","price":800,"rank":1},
##    {"title":"聯發科","price":1000,"rank":2},
##    {"title":"鴻海","price":150,"rank":3}
##    ]
##
####for item in all_news:
####    print("標題",item["title"])
####    print("價格",item["price"])
####    print("排名",item["rank"])
####    print()
##
##print(f'標題\t價格\t排名')    
##for item in all_news:
## print(item["title"],"\t",item["price"],"\t",item["rank"])
##
##
##cart=[
##    {"name":"Python書籍","price":450,"count":1},
##    {"name":"無線滑鼠","price":890,"count":2},
##    {"name":"螢幕支架","price":120,"count":1},
##    ]
##
##total=0
##for item in cart:
##    price=item["price"]
##    count=item["count"]
##    cost=price*count
##    print("小計",cost)
##    total=total+cost
##print(total)

####1-3 隨堂練習
##一, 1.B 2.C 3.B 4.C 5.B
##二, 1.{} 2.stocks[1][1] 3.for 4.key 5.store
##三,實作##########################################
##1.
##site_data={
##    "city":"Taipei",
##    "weather":[{"time":"morning"},{"temp":"night"},{"temp":18}]
##    }
##print(f'{site_data["city"]}晚上的氣溫{site_data["weather"][2]["temp"]}度')
####2.
##my_favorites=[
##    {"title":"a","price":10},
##    {"title":"b","price":20},
##    {"title":"c","price":30}
##    ]
##for book in my_favorites:
##    print(book["title"],end=' ')
#################################################












