"""
Find the mode of the values in the Inventory List
Author: Dan
"""

fOp = open("snapInvLiDoc.py", 'r')

words = []
categ = []
items = []
itAmo = []
dicti = {}

for line in fOp:
    for word in line.split():
        words.append(word.upper())

for word in words:
    number = dicti.get(word, None)
    if number == None:
        dicti[word] = 1
    else:
        dicti[word] = number + 1
maxNum = max(dicti.values())
for key in dicti:
    print("The mode is ", key)
    print(dicti[key])
    break
