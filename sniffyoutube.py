#! /usr/bin/python3

import csv
import datetime
import time

from urllib.request import urlopen
from bs4 import BeautifulSoup



def getPage(channelId):
  rawHtml = ("https://www.youtube.com/"+channelId)
  html = urlopen("https://www.youtube.com/"+channelId)
  bsObj = BeautifulSoup(html, "lxml")
  subscribers = bsObj.find(class_="yt-subscription-button-subscriber-count-branded-horizontal yt-uix-tooltip")
  channelName = bsObj.find(class_='spf-link branded-page-header-title-link yt-uix-sessionlink').get_text()
  print(subscribers.get_text())
  return rawHtml, bsObj, channelName, subscribers


def playListSniff(bsObj):
  vidIdSniff = bsObj.find("", {"id": "pl-video-table"})
  vidId = vidIdSniff.findAll('tr')
  vidIds = []
  for vidId in vidId:
    vidIds.append(vidId.attrs['data-video-id'])
  print(vidIds)
  return vidIds


def getLinks(videoId):
  html = urlopen("https://www.youtube.com/watch?v="+videoId)
  bsObj = BeautifulSoup(html, "lxml")
  title =bsObj.find("", {"id": "eow-title"}).get_text()
  views = bsObj.find("", {"class": "watch-view-count"}).get_text()
  return title, views


def chinaYouku(list):
  t = open(list)
  for line in t:
    html = urlopen(line)
    bsObj = BeautifulSoup(html, 'lxml')
    videoTitles = bsObj.findAll('', {'class':'v_title'})
    videoTitle = []
    for video in videoTitles:
      videoTitle.append(video.get_text())
    videoViews = bsObj.findAll('', {'class':'v_stat'})
    videoView = []
    for video in videoViews:
      videoView.append(video.get_text())
    #channel = bsObj.find('div', {'class':'name'})
    #channel = channel.get_text()
    #channelUrl = bsObj.find('div', {'class':'name'}).a
    #channelUrl = channelUrl.attrs['href']
    #html2 = urlopen(channelUrl)
    #bsObj2 = BeautifulSoup(html2)
    #channelSubs = bsObj2.find('',{'class':'snum'})
    #channelSubs = channelSubs.em.get_text()
    return videoTitle, videoView


def chinaTenCent(line):
  html = urlopen(line)
  bsObj = BeautifulSoup(html, 'lxml')
  title = bsObj.find('',{'class':'mod_player_title'}).get_text()
  views = bsObj.find('',{'class':'played_count'}).find('',{'class':'num'}).get_text()
  return title, views

'''
Currently the Sina Weibo function does not work.

def chinaSina(list):
  t = open(list)
  for line in t:
    html = urlopen(line)
    bsObj = BeautifulSoup(html, 'lxml')
    title =
    views =
    return title, views
'''

def main():
  f = open('playLists.txt')
  #userInput = input("Paste in Channel or Playlist string ->")
  csvFile = open(datetime.datetime.now().strftime('%Y-%m-%d')+"Win10YT.csv", 'wt')
  writer = csv.writer(csvFile)

  for line in f:
    pageUrl = getPage(line)[0] # Should change to just line instead of calling function
    if 'playlist' in pageUrl:
      vidIds = playListSniff(getPage(line)[1])
      writer.writerow((getPage(line)[2], 'Subscribers: '+getPage(line)[3].get_text()))
      for vidId in vidIds:
        writer.writerow((getLinks(vidId)))
  chinaList = 'chinalist.txt'
  chinaTenCents = open('chinaTenCent.txt')
  china1 = chinaYouku(chinaList)[0]
  china2 = chinaYouku(chinaList)[1]

  writer.writerow(('China Youku', ':'))
  counter = 0
  for video in china1:
    writer.writerow((video, china2[counter]))
    counter += 1
  writer.writerow(('China TenCent', ':'))
  for line in chinaTenCents:
    result = chinaTenCent(line)
    writer.writerow((result))
    time.sleep(10)

  csvFile.close()
  chinaTenCents.close()

if __name__ == '__main__':
  main()
