from bs4 import BeautifulSoup

html_with_links = """
<div class="menu">
  <a href="/news">新聞</a>
  <a href="/all/news">新聞2</a>
  <a href="/news/new3">新聞3</a>    
  <a href="https://google.com" target="_blank">Google</a>
  <a href="https://microsoft.com" target="_blank">Microsoft</a> 
  <a href="http://apple.com" target="_blank">Apple</a>
  <a href="/about">關於</a>
</div>

"""
soup=BeautifulSoup(html_with_links, 'html.parser')

external=soup.select("a[target]")
print(external)
for a in external:
  print(a.text)
  print(a['href'])
  
  print("-----")
  news=soup.select("a[href^='/news']")
  for a in news:
    print(a.text)
    print(a['href'])
    
  print("-----")

  news=soup.select("a[href='/news']")
  for a in news:
    print(a.text)
    print(a['href'])

