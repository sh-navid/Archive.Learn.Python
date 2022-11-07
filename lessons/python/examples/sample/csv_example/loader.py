import sys
import csv

dictionary = {}

with open(sys.path[0]+'/source.csv', 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        word, meaning = row[0].split(",")
        dictionary[word] = meaning

print(dictionary)
print(dictionary["hi"])
