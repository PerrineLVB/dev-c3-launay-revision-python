import csv

with open('exo/files/addresses.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    lines = list(csv_reader)

word_count = 0
for line in lines:
    words = line[0].split()
    word_count += len(words)

with open('exo/files/result.txt', 'w') as txt_file:
    txt_file.write("Nombre de mots dans le fichier csv : " + str(word_count))

txt_file.close()