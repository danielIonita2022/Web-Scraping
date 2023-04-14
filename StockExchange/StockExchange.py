def putNewline(string):
    newString = ''
    markAlpha = False
    for letter in string:
        if letter.isdigit() is True:
            if markAlpha is True:
                newString += ':\n'
                markAlpha = False
        else:
            markAlpha = letter.isalpha()
        newString += letter
    return newString
