import urllib.request
import nltk
from bs4 import BeautifulSoup
articleURL="https://www.washingtonpost.com/powerpost/a-new-liberal-tea-party-is-forming-can-it-last-without-turning-on-democrats/2017/02/11/94421200-efdf-11e6-9973-c5efb7ccfb0d_story.html?hpid=hp_hp-top-table-main_pkcapitol-430pm%3Ahomepage%2Fstory&utm_term=.ce8b66e48619"


def getTextWaPo(url):
    req = urllib.request.Request(articleURL)
    response = urllib.request.urlopen(req)
    page= response.read().decode("utf-8","ignore")

    soup=BeautifulSoup(page,"lxml")
    text=" ".join(map(lambda p: p.text, soup.find_all("article")))
    return text.encode("ascii", errors="replace").replace(b'?', b' ').decode("utf-8")



from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

def summarize (text, n):
    sents=sent_tokenize(text)

    assert n<=len(sents)
    word_sent=word_tokenize(text.lower())

    _stopwords=set(stopwords.words("english") + list(punctuation))

    word_sent=[word for word in word_sent if word not in _stopwords]

    from nltk.probability import FreqDist
    freq=FreqDist(word_sent)

    #for f in freq.keys():
    #    print(f, freq[f])

    from heapq import nlargest
    #print(nlargest(10,freq, key=freq.get))

    from collections import defaultdict
    ranking=defaultdict(int)

    for i, sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]
    sents_idx=nlargest(n,ranking, key=ranking.get)

    print([sents[j] for j in sorted(sents_idx)])

    #for i in nlargest(10,ranking, key=ranking.get):
    #    print(sents[i])




summarize(getTextWaPo(articleURL), 5)
