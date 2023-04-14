def get_city(inputCity, newsNowString):
    sizeOfCity = len(inputCity)
    stringLen = 9 + sizeOfCity
    city = newsNowString[:stringLen]
    return city, stringLen


def get_weather_conditions(stringLen, newsNowString):
    stringLen += 1
    length = stringLen
    weatherList = []
    for i in range(5):
        weather = ""
        stringLen = length - 1
        for string in newsNowString[stringLen:]:
            length += 1
            if string != '\n':
                if i == 0:
                    if string != 'T':
                        weather += string
                    else:
                        break
                elif i == 1:
                    if string != 'V':
                        weather += string
                    else:
                        break
                elif i == 2:
                    if string != 'P':
                        weather += string
                    else:
                        break
                elif i == 3:
                    if string != 'U':
                        weather += string
                    else:
                        break
                elif i == 4:
                    if string != 'C':
                        weather += string
                    else:
                        break
        if i == 1:
            string = 'T'
        elif i == 2:
            string = 'V'
        elif i == 3:
            string = 'P'
        elif i == 4:
            string = 'U'
        if i == 0:
            weatherString = "{0}{1}".format(weather[0].upper(), weather[1:])
        else:
            weatherString = "{0}{1}".format(string, weather)
        weatherList.append(weatherString)
    return weatherList
