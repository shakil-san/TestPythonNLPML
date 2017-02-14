import nltk
text ="Mary had a little lab. Her fleece was white as snow"
from nltk.tokenize import word_tokenize, sent_tokenize
sents=sent_tokenize(text)
#print(sents)

words=[word_tokenize(sent) for sent in sents]
#print(words)

from nltk.corpus import stopwords
from string import punctuation

customStopWords=set(stopwords.words("english")+list(punctuation))
#print(customStopWords)

wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
#print(wordsWOStopwords)

from nltk.collocations import *
bigram_measures=nltk.collocations.BigramAssocMeasures()
finder=BigramCollocationFinder.from_words(wordsWOStopwords)
finder2=TrigramCollocationFinder.from_words(wordsWOStopwords)

#print(sorted(finder2.ngram_fd.items()))

text2="Mary closed on closing night when she was in the mood to close."

from nltk.stem.lancaster import LancasterStemmer
st=LancasterStemmer()
stemmedWords=[st.stem(word) for word in word_tokenize(text2)]
#print(stemmedWords)

#print(nltk.pos_tag(word_tokenize(text2)))

from nltk.corpus import wordnet as wn

#for ss in wn.synsets("bass"):
#    print(ss, ss.definition())

from nltk.wsd import lesk
sense1=lesk(word_tokenize("Sing in a lower toen, along with the bass"),"bass")
print(sense1, sense1.definition())

sense2=lesk(word_tokenize("This sea bass was really hard to catch"),"bass")
print(sense2, sense2.definition())


