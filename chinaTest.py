import time

import requests
from bs4 import BeautifulSoup

china = open('chinaTenCent.txt')

def chinaTenCent(line):
  session = requests.Session()
  headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
  url = line
  req = session.get(url, headers=headers)
  bsObj = BeautifulSoup(req.text)
  title = bsObj.find('',{'class':'mod_player_title'}).get_text()
  views = bsObj.find('',{'class':'played_count'}).find('',{'class':'num'}).get_text()
  return title, views

for line in china:
  print(chinaTenCent(line))
  time.sleep(5)

china.close()
