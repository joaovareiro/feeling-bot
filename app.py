import openpyxl
import snscrape.modules.twitter as sns

book = openpyxl.Workbook()

book.create_sheet('bot_sheet')

bot_sheet = book['bot_sheet']

query = "(candidate) lang:pt"
tweets = []
max_size = 300
bot_sheet.append(['sentimento', 'datahora','mensagem'])
for tweet in sns.TwitterSearchScraper(query).get_items():
    bot_sheet.append([' ', str(tweet.date),tweet.content])
    print([' ', tweet.date,tweet.content])  
    tweets.append([tweet.username,tweet.content])
    if len(tweets) > max_size:
        break

book.save('candidate.xlsx')