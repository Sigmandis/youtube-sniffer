import csv

from urllib.request import urlopen
from bs4 import BeautifulSoup

from sniffyoutube import getPage, playListSniff

def prepUrl(urlTxt):
	url = urlopen(urlTxt)
	bsObj = BeautifulSoup(url)
	return bsObj

def metaSniff(vidId):
	url = urlopen("https://www.youtube.com/watch?v="+videoId)
	bsObj = BeautifulSoup(url)
	title = bsObj.find('meta', {'property':'og:title'})
	

def main():
	f = open('metaList.txt')
	for line in f:
		prep = prepUrl(line)
		vidId = playListSniff(prep)
		for ids in vidId:
			metaSniff(ids)


if __name__ == '__main__':
  	main()