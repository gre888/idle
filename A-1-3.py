def check_relevance(title, content, keyword):
    """檢查標題或內容中是否真的包含關鍵字"""
    if keyword in title or keyword in content:
        return True
    return False

# 測試
test_title = "最新科技趨勢：積層製造技術解析"
test_keyword = "3D列印"

if check_relevance(test_title, "", test_keyword):
    print("符合需求，存入資料庫。")
else:
    print("相關度過低，略過。")
