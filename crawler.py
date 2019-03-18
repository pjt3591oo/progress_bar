import requests
from bs4 import BeautifulSoup
from progress_bar import progress_bar


KEYWORD = "화재"
PAGE = 0
MAX_PAGE = 5
URL = "https://search.naver.com/search.naver?&where=news&query=%s&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:dd,p:all,a:all&mynews=0&start=%s"


if __name__ == "__main__":
  
  while True:
    print('=========================%d PAGE crawler========================='%(PAGE+1))
    if PAGE >= MAX_PAGE : break

    start = PAGE * 10 + 1

    res = requests.get(URL%(KEYWORD, start))
    soup = BeautifulSoup(res.content, 'lxml')

    p = soup.select('#main_pack .news ul.type01 li')

    for i in p:
      item = i.select('dl dt a')[0]

      text = item.text
      href = item.get('href')

      print(text, href)

    PAGE += 1
  
    progress_bar()
    