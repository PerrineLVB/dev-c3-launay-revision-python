import random

nbList = [random.randint(1, 1000) for i in range(10)]
print ("Liste random : " + str(nbList))

if len(nbList) == 0:
    print ("Liste vide")

nbList.sort()
print ("Ordre croissant : " + str(nbList))

mini = nbList[0]
print ("Minimum : " + str(mini))

maxi = nbList[-1]
print ("Maximum : " + str(maxi))

moy = sum(nbList) / len(nbList)
print ("Moyenne : " + str(moy))