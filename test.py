import lxml
from bs4 import BeautifulSoup

aa = '<a href="/picture/article/77/3c/6c/7c0bbe5e4cc9ad4026c297054e10/31ec9080-7f69-460a-919c-e562ce888784.pdf">'
soup = BeautifulSoup(aa, 'lxml')

print(soup.a.get_text())