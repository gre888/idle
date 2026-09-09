import xml.etree.ElementTree as ET




xml_string = '''
<news_list>
    <item id="1">
        <title>Python 爬蟲入門</title>
        <author>老師</author>
    </item>
    <item id="2">
        <title>AI 時代來臨</title>
        <author>小助手</author>
    </item>
</news_list>
'''

root = ET.fromstring(xml_string)
print("----新聞列表----")



for news in root.findall("item"):
    print(news.tag, "id=", news.get("id"))
    print("title=",news.find("title").text)
    print("author=",news.find("author").text)


##xml_data = '''
##    <weather_report>
##        <city name="台北">
##            <temp>25</temp>
##            <status></status>
##        </city>
##    </weather_report>    
##'''

    
##item_node = root.find("item")
##print(item_node.tag)
##print(item_node.get("id"))
    

##root = ET.fromstring(xml_data)
##print(root.tag)
##city_node = root.find("city")
##print("都市:",city_node.get("name"))
##
##temp_node = city_node.find("temp")
##print("溫度:",temp_node.text)
