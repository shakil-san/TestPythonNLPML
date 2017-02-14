import urllib.request
import pprint
import nltk
from bs4 import BeautifulSoup

def getAllDoxyDonkeyPosts(url, links):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    soup=BeautifulSoup(response)

    for a in soup.findAll("a"):
        try:
            url=a['href']
            title=a['title']
            if title=="Older Posts":
                #print(url)
                links.append(url)
                getAllDoxyDonkeyPosts(url,links)
        except:
            titl=""

    return

blogUrl="http://doxydonkey.blogspot.in"
links=[]
getAllDoxyDonkeyPosts(blogUrl, links)

def getDoxyDonkeyText(testUrl):
    req = urllib.request.Request(testUrl)
    response = urllib.request.urlopen(req)
    soup = BeautifulSoup(response)
    mydivs =soup.find_all("div",{"class":"post-body"})

    posts=[]
    for div in mydivs:
        posts+= map(lambda p: p.text.encode("ascii", errors="replace").replace(b"?",b" ").decode("utf-8"), div.findAll("li"))
    return posts

doxtDonkeyPosts=[]
for link in links:
    doxtDonkeyPosts+=getDoxyDonkeyText(link)

pp=pprint.PrettyPrinter()
pp.pprint(doxtDonkeyPosts)