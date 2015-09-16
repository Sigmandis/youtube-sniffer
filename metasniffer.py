import csv

from urllib.request import urlopen
from bs4 import BeautifulSoup

from sniffyoutube import playListSniff

def prepUrl(urlTxt):
	url = urlopen(urlTxt)
	bsObj = BeautifulSoup(url)
	return bsObj

def metaSniff(vidId):
	url = urlopen('https://www.youtube.com/watch?v='+vidId)
	bsObj = BeautifulSoup(url)
	title = bsObj.find('meta', {'property':'og:title'}).attrs['content']
	description = bsObj.find('meta', {'property':'og:description'}).attrs['content']
	keywords = bsObj.findAll('meta', {'property':'og:video:tag'})
	keys = []
	for keyword in keywords:
		key = keyword.attrs['content']
		keys.append(key)
	return title, description, keys


def main():
	f = open('metaList.txt')
	with open('metaSniff.csv', 'wt') as csvfile:
		for line in f:
			writer = csv.writer(csvfile, delimiter=',')
			prep = prepUrl(line)
			vidId = playListSniff(prep)
			for ids in vidId:
				writer.writerow(metaSniff(ids))


if __name__ == '__main__':
  	main()
