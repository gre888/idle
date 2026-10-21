from bs4 import BeautifulSoup

# html = '<a href="https://example.com" class="link" id="target">點我前往</a>'
# soup = BeautifulSoup(html, 'html.parser')
# a_tag = soup.select_one("#target")

# url_a=a_tag['href']
# print(url_a)

# url_b=a_tag.get('href')
# print(url_b)


html='<a class="link" class="link" id="target">點我前往</a>'
soup = BeautifulSoup(html, 'html.parser')
a_tag = soup.select_one("#target")

# url_c=a_tag['href']
# print(url_c) # key error because the 'href' attribute might not exist

url_d=a_tag.get('href')
print(url_d) # None because the 'href' attribute does not exist


