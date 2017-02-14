import pickle

filename="j:/python/finalized_model.sav"
filename1="j:/python/vectorizer.sav"
loaded_model = pickle.load(open(filename, 'rb'))

article = "Twitter Inc posted the slowest revenue growth since it went public four years ago, sending shares down more than 10 percent on Thursday on fears that rivals Snapchat and Facebook Inc(FB.O) were winning the war for advertising. Revenue from advertising fell from a year ago and a 4.0 percent year-on-year rise in users to 319 million fell short of Wall Street forecasts as well. Total revenue grew 1.0 percent to $717.2 million. The election of prolific tweeter Donald Trump as U.S. president failed to produce a Trump Bump in Twitters results, and Twitter declined to give guidance on future revenue with Chief Executive Jack Dorsey asking for patience. The microblogging service has struggled to find a formula that will attract a new crop of users or advertisers even as rivals have ridden a wave of rising investment in internet advertising. The lack of revenue growth has raised questions about Dorsey s leadership and whether the company would be bought by a bigger media firm. Financial markets speculated about a sale of Twitter last year, but no concrete bids were forthcoming. Dorsey also faced concerns about his dual role as the chief executive of both Twitter and Square Inc. Running two companies is not the best idea, Steve Ballmer, a Twitter investor and a former Microsoft Corp (MSFT.O) chief executive, told CNBC. Twitter was also hit by a string of executive departures in 2016, including in its products team, which had three heads in less than a year. In October, the company said it would cut 9.0 percent of its global workforce as part of a broader restructuring. Twitter s net loss widened to $167.1 million, or 23 cents per share, in the fourth quarter ended Dec. 31, from $90.24 million, or 13 cents per share, a year earlier."

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=pickle.load(open(filename1, 'rb'))


test=vectorizer.transform([article.encode("ascii", errors="ignore")])
print(loaded_model.predict(test))