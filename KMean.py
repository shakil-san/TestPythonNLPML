import urllib.request
import pprint
import nltk
from bs4 import BeautifulSoup


def getAllDoxyDonkeyPosts(url, links):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    soup = BeautifulSoup(response)

    for a in soup.findAll("a"):
        try:
            url = a['href']
            title = a['title']
            if title == "Older Posts":
                print(url)
                links.append(url)
                getAllDoxyDonkeyPosts(url, links)
        except:
            titl = ""

    return


blogUrl = "http://doxydonkey.blogspot.in"
links = []
getAllDoxyDonkeyPosts(blogUrl, links)


def getDoxyDonkeyText(testUrl):
    req = urllib.request.Request(testUrl)
    response = urllib.request.urlopen(req)
    soup = BeautifulSoup(response)
    mydivs = soup.find_all("div", {"class": "post-body"})

    posts = []
    for div in mydivs:
        posts += map(lambda p: p.text.encode("ascii", errors="replace").replace(b"?", b" ").decode("utf-8"),
                     div.findAll("li"))
    return posts


doxtDonkeyPosts = []
for link in links:
    doxtDonkeyPosts += getDoxyDonkeyText(link)

pp=pprint.PrettyPrinter()
pp.pprint(doxtDonkeyPosts)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer=TfidfVectorizer(max_df=0.5, min_df=2, stop_words="english")

x= vectorizer.fit_transform(doxtDonkeyPosts)
x

print(x[0])

from sklearn.cluster import KMeans
km=KMeans(n_clusters=3, init="k-means++", max_iter=100, n_init=1, verbose=True)

km.fit(x)

import numpy as np
np.unique(km.labels_, return_counts=True)

text={}
for i, cluster in enumerate (km.labels_):
    oneDocument=doxtDonkeyPosts[i]
    if cluster not in text.keys():
        text[cluster]=oneDocument
    else:
        text[cluster]+=oneDocument

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import nltk

_stopwords=set(stopwords.words("english") + list(punctuation))

keywords={}
counts={}
for cluster in range(3):
    word_sent=word_tokenize(text[cluster].lower())
    word_sent=[word for word in word_sent if word not in _stopwords]
    freq=FreqDist(word_sent)
    keywords[cluster]=nlargest(100, freq, key=freq.get)
    counts[cluster]=freq

unique_keys={}
for cluster in range(3):
    other_clusters=list(set(range(3))-set([cluster]))
    keys_other_clusters=set(keywords[other_clusters[0]]).union(set(keywords[other_clusters[1]]))
    unique=set(keywords[cluster])-keys_other_clusters
    unique_keys[cluster]=nlargest(10, unique, key=counts[cluster].get)

print(unique_keys)

pp.pprint(unique_keys)

article='Twitter Inc posted the slowest revenue growth since it went public four years ago, sending shares down more than 10 percent on Thursday on fears that rivals Snapchat and Facebook Inc(FB.O) were winning the war for advertising. Revenue from advertising fell from a year ago and a 4.0 percent year-on-year rise in users to 319 million fell short of Wall Street forecasts as well. Total revenue grew 1.0 percent to $717.2 million. The election of prolific tweeter Donald Trump as U.S. president failed to produce a Trump Bump in Twitters results, and Twitter declined to give guidance on future revenue with Chief Executive Jack Dorsey asking for patience. The microblogging service has struggled to find a formula that will attract a new crop of users or advertisers even as rivals have ridden a wave of rising investment in internet advertising. The lack of revenue growth has raised questions about Dorsey s leadership and whether the company would be bought by a bigger media firm. Financial markets speculated about a sale of Twitter last year, but no concrete bids were forthcoming. Dorsey also faced concerns about his dual role as the chief executive of both Twitter and Square Inc. "Running two companies is not the best idea," Steve Ballmer, a Twitter investor and a former Microsoft Corp (MSFT.O) chief executive, told CNBC. Twitter was also hit by a string of executive departures in 2016, including in its products team, which had three heads in less than a year. In October, the company said it would cut 9.0 percent of its global workforce as part of a broader restructuring. Twitter s net loss widened to $167.1 million, or 23 cents per share, in the fourth quarter ended Dec. 31, from $90.24 million, or 13 cents per share, a year earlier.'

from sklearn.neighbors import KNeighborsClassifier

classifier=KNeighborsClassifier(n_neighbors=10)
classifier.fit(x, km.labels_)

test=vectorizer.transform([article.encode("ascii", errors="ignore")])

classifier.predict(test)

import pickle
filename="j:/python/finalized_model.sav"

pickle.dump(classifier, open(filename, "wb"))

loaded_model = pickle.load(open(filename, 'rb'))

loaded_model.predict(test)

from sklearn.pipeline import Pipeline
newmodel=Pipeline([('vectorizer', vectorizer), ('classifier',classifier )])

filename1="j:/python/finalized_model1.sav"
pickle.dump(newmodel, open(filename1, "wb"))

filename2="j:/python/vectorizer.sav"
pickle.dump(vectorizer, open(filename2, "wb"))





