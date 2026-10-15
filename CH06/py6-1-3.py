from urllib.parse import urlparse, parse_qs

full_url = "https://www.google.com/search?q=python%E7%94%B1%E4%BE%86"

parsed_url = urlparse(full_url)
print("Parsed URL",parsed_url)
print(f"路徑: {parsed_url.path}")
print(f"查詢參數: {parsed_url.query}")
print(f"主機: {parsed_url.netloc}")
print(f"協議: {parsed_url.scheme}")
print(f"參數: {parsed_url.params}")
print(f"片段: {parsed_url.fragment}")

query_params = parse_qs(parsed_url.query)
print("Full URL",full_url)
print("Parsed URL:", parsed_url)
print("Query Parameters:", query_params)