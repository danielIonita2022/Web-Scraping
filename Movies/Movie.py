def cleanInput(inputJ):
    inputK = inputJ.replace('\'', '')
    inputL = inputK.replace(' ', '-')
    inputM = inputL.lower()
    return inputM


def setScores(soup, movieOrTv, criticOrUser):
    if criticOrUser == 'critic':
        stringCriticOrUser = 'ms'
    else:
        stringCriticOrUser = 'us'

    score = soup.select(f"div.{stringCriticOrUser}_wrapper span.metascore_w.larger.{movieOrTv}.positive")
    if len(score) == 0:
        score = soup.select(f"div.{stringCriticOrUser}_wrapper span.metascore_w.larger.{movieOrTv}.mixed")
    if len(score) == 0:
        score = soup.select(f"div.{stringCriticOrUser}_wrapper span.metascore_w.larger.{movieOrTv}.negative")

    return score
