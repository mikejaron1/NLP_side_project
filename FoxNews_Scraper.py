## fox news, meredith
import urllib2
from bs4 import BeautifulSoup
base_url = "http://www.foxnews.com"
politics_url = base_url+ "/politics.html"
page = urllib2.urlopen(politics_url)
# print page.read()
soup = BeautifulSoup(page, "html.parser")
# print soup.prettify()
page_links = []
all_links = soup.find_all('a')
for link in all_links: 
	link = link.get("href")
	print type (link)
	if 'video' not in link and '.html' in link:
		page_links.append(base_url+link)
print len(page_links), " total page links to go through"