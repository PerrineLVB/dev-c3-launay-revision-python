nb = input('Saisir un chiffre : ')

if nb.isdigit():
    nb = int(nb)
    result = 1
    i = 1
    while i <= nb:
        result = result * i
        i = i + 1
    print (result)
else:
    print("Vous n'avez pas saisi un chiffre.")
    