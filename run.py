import bs4 as bs
import re
import urllib.request

url = input('Enter thread url: ')
fetch = urllib.request.urlopen(url)
print('Status Code:', fetch.getcode())
html = fetch.read()
soup = bs.BeautifulSoup(html, 'html.parser')
ls = soup.find_all('a', class_ = 'fileThumb') # list contains 'tag' class

filepath = input("insert path: ")

for i in range(len(ls)):
    print(ls[i]['href'])
    video_link = ls[i]['href']
    stringsearch = re.search(r'[\/](\d*)([.].*$)', video_link)
    filename = stringsearch.group(1)
    formatname = stringsearch.group(2)
    fullpath = filepath + filename + formatname
    urllib.request.urlretrieve('https:'+video_link, fullpath)
    print('completed...', i)
