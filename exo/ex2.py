phrase = input ('Merci de saisir une phrase :')

if phrase.isdigit():
    print("Votre phase ne contient que des nombres")
else:
    phraseMaj = phrase.upper()
    print (phraseMaj)
    phraseMin = phrase.lower()
    print (phraseMin)
    nbWords = len (phrase.split())
    print (nbWords)
