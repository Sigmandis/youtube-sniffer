from urllib.request import urlopen
from bs4 import BeautifulSoup

def getPage(channelId):
  rawHtml = ("https://www.youtube.com/"+channelId)
  html = urlopen("https://www.youtube.com/"+channelId)
  bsObj = BeautifulSoup(html, "lxml")
  subscribers = bsObj.find(class_="yt-subscription-button-subscriber-count-branded-horizontal yt-uix-tooltip")
  print(subscribers.get_text())
  return rawHtml, bsObj

def playListSniff(bsObj):
  vidIdSniff = bsObj.find("table", {"id": "pl-video-table"})
  vidId = vidIdSniff.findAll('tr')
  vidIds = []
  for vidId in vidId:
    vidIds.append(vidId.attrs['data-video-id'])
  print(vidIds)
  return vidIds

def getLinks(videoId):
  html = urlopen("https://www.youtube.com/watch?v="+videoId)
  bsObj = BeautifulSoup(html, "lxml")
  title =bsObj.find("span", {"id": "eow-title"}).get_text()
  views = bsObj.find("div", {"class": "watch-view-count"}).get_text()
  print(title, views)

userInput = input("Paste in Channel or Playlist string ->")
pageUrl = getPage(userInput)[0]
if 'playlist' in pageUrl:
  vidIds = playListSniff(getPage(userInput)[1])
  for vidId in vidIds:
    getLinks(vidId)
