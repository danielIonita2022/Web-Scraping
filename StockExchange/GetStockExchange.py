import requests
from bs4 import BeautifulSoup as bs4
import re
import StockExchange

inputSymbol = input('Simbolul instrumentului financiar: ')
response = requests.get(f'https://bvb.ro/FinancialInstruments/Details/FinancialInstrumentsDetails.aspx?s={inputSymbol}')
soup = bs4(response.content, 'html.parser')

title = soup.select("title")
titleText = [text.getText() for text in title]
print("".join(titleText) + '\n')

text = soup.select("tr")
listText = [lText.getText() for lText in text]
stringText = "\n".join(listText)

newStringText = re.sub(r'\n\n', r'\n', stringText)
pos = newStringText.find('\n\n\n')
posSecond = newStringText.find('Bid')
renewStringText = newStringText[:pos]
secondRenewStringText = newStringText[posSecond:]
finalStringText = StockExchange.putNewline(secondRenewStringText)

print(renewStringText)
print('\n' + finalStringText)
