import requests
from bs4 import BeautifulSoup as bs4
from Movie import cleanInput
from Movie import setScores

movieOrTvShow = input("Movie or TV Show?\n")
s = requests.session()
s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                          'Chrome/37.0.2062.120 Safari/537.36 '

if movieOrTvShow == "movie":
    inputJ = input("Searched movie:\n")
    url = f'https://www.metacritic.com/movie/{cleanInput(inputJ)}'
    movieOrTvShow = 'movie'
else:
    inputJ = input("Searched TV Show:\n")
    url = f'https://www.metacritic.com/tv/{cleanInput(inputJ)}'
    movieOrTvShow = 'tvshow'

response = s.get(url)
soup = bs4(response.content, 'html.parser')
scoreCritic = setScores(soup, movieOrTvShow, 'critic')
scoreUser = setScores(soup, movieOrTvShow, 'user')

textScoreCritic = [text.getText() for text in scoreCritic]
textScoreUser = [text.getText() for text in scoreUser]
stringScoreCritic = "".join(textScoreCritic).strip('')
stringScoreUser = "".join(textScoreUser).strip('')
print('\n' + inputJ.capitalize() + '\n')
print('Critics score: ' + stringScoreCritic)
print('Audience score: ' + stringScoreUser)

summary = soup.select("div.summary_deck.details_section")
textSummary = [text.getText() for text in summary]
stringSummary = "".join(textSummary).strip('')
print(stringSummary)
