import requests
from bs4 import BeautifulSoup as bs4
import Weather

inputCounty = input("Judetul: ")
inputCity = input("Orasul: ")

county = inputCounty.lower()
city = inputCity.lower().replace(" ", "")

r = requests.get(f'https://www.vremea.ro/{county}/{city}/')
soup = bs4(r.content, 'html.parser')
newsNowSoup = soup.select("div.news.wxnow")
newsNow = [news.getText() for news in newsNowSoup]
newsNowString = ("".join(newsNow).strip(''))

city = Weather.get_city(inputCity, newsNowString)[0]
stringLen = Weather.get_city(inputCity, newsNowString)[1]
weatherConditions = Weather.get_weather_conditions(stringLen, newsNowString)

print(city)
print("\n".join(weatherConditions))
