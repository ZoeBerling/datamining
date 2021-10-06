from csv import reader
import numpy as np

itemSetCount = dict()

NUMTRANS = 0

minSupCount = 3

read_obj = open("inputExercise4.csv.txt", "r")

csv_reader = reader(read_obj)

for row in csv_reader:

    NUMTRANS += 1

    itemSet = ''

    for i in range(len(row)):
        itemSet += row[i]

    if (itemSet in itemSetCount):

        itemSetCount[itemSet] = itemSetCount[itemSet] + 1

    else:

        itemSetCount[itemSet] = 1
#
# print(itemSetCount)

sortedByCount = ({k: v for k, v in sorted(itemSetCount.items(), key=lambda item: item[1])})

# print("\nAfter sorting by value:")
#
#print(sortedByCount)
#
# print("\nhere are the frequent itemsets ")

# for k, v in sortedByCount.items():
#
#     if (v >= minSupCount):
#        # print(str(k) + '  ' + str(v))


read_obj = open("inputExercise4.csv.txt", "r")
csv_reader = reader(read_obj)

# all 5-itemsets
for row in csv_reader:


    for a in range(len(row) - 4):  # note the -2 at the end

        for b in range(a + 1, len(row) - 3):  # note  the -1 at the end

            for c in range(b + 1, len(row) - 2):

                for d in range(c + 1, len(row) - 1):

                    for e in range(d + 1, len(row)):

                        itemSet = row[a] + row[b] + row[c] + row[d] + row[e]
                        if itemSet in sortedByCount.keys():
                            sortedByCount[itemSet] += 1

# row content a 4-itemset
read_obj = open("inputExercise4.csv.txt", "r")
csv_reader = reader(read_obj)

for row in csv_reader:
    for a in range(len(row) - 3):  # note the -2 at the end

        for b in range(a + 1, len(row) - 2):  # note  the -1 at the end

            for c in range(b + 1, len(row) - 1):

                for d in range(c + 1, len(row)):

                    itemSet = row[a] + row[b] + row[c] + row[d]
                    if itemSet in sortedByCount.keys():
                        sortedByCount[itemSet] += 1

# row content a 3-itemset
read_obj = open("inputExercise4.csv.txt", "r")
csv_reader = reader(read_obj)

for row in csv_reader:
    for a in range(len(row) - 2):  # note the -2 at the end

        for b in range(a + 1, len(row) - 1):  # note  the -1 at the end

            for c in range(b + 1, len(row)):

                itemSet = row[a] + row[b] + row[c]
                if itemSet in sortedByCount.keys():
                    sortedByCount[itemSet] += 1


# row content a 2-itemset
read_obj = open("inputExercise4.csv.txt", "r")
csv_reader = reader(read_obj)

for row in csv_reader:
    for a in range(len(row) - 1):  # note the -2 at the end

        for b in range(a + 1, len(row)):  # note  the -1 at the end

            itemSet = row[a] + row[b]
            if itemSet in sortedByCount.keys():
                sortedByCount[itemSet] += 1


# row content a 1-itemset
read_obj = open("inputExercise4.csv.txt", "r")
csv_reader = reader(read_obj)
for row in csv_reader:
    for a in range(len(row)):
        itemSet = row[a]
        if itemSet in sortedByCount.keys():
            sortedByCount[itemSet] += 1

#print(sortedByCount)

newDict = {key:value for key,value in sortedByCount.items() if value > 400}
print(newDict)


lst = []
for key in newDict.keys():
    for char in key:
       conf = newDict[key]/newDict[char]
       print(conf)
       if conf > .5:
           lst.append([key, char, conf])

print(lst)