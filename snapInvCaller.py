import snapInvLiDoc

#Parties dictionary call and variable set
p1 = 'Plates'
p2 = 'PlasticwareFork'
p3 = 'PlasticwareSpoon'
p4 = 'PlasticwareKniv'
p5 = 'Napkins'
p6 = 'bDayShirtsTotal'
p7 = 'bDayShirtsS'
p8 = 'bDayShirtsM'
p9 = 'bDayShirtsL'
p10 = 'Tableclothes'
p11 = 'Nametags'

plates = str(snapInvLiDoc.Parties[p1])
plasticwareFork = snapInvLiDoc.Parties[p2]
plasticwareSpoon = snapInvLiDoc.Parties[p3]
plasticwareKniv = snapInvLiDoc.Parties[p4]
Napkins = snapInvLiDoc.Parties[p5]
bDayShirtsTotal = snapInvLiDoc.Parties[p6]
bDayShirtsS = snapInvLiDoc.Parties[p7]
bDayShirtsM = snapInvLiDoc.Parties[p8]
bDayShirtsL = snapInvLiDoc.Parties[p9]
Tableclothes = snapInvLiDoc.Parties[p10]
Nametags = snapInvLiDoc.Parties[p11]

#Gift Bags dictionary call and variable set
g1 = 'Pencils'
g2 = 'bags'
g3 = 'Kits'
g4 = 'bracelets'
g5 = 'stickers'
g6 = 'tattoos'
g7 = 'campFlyers'
g8 = 'Buttons'

Pencils = snapInvLiDoc.Gift_Bags[g1]
bags = snapInvLiDoc.Gift_Bags[g2]
Kits = snapInvLiDoc.Gift_Bags[g3]
bracelets = snapInvLiDoc.Gift_Bags[g4]
stickers = snapInvLiDoc.Gift_Bags[g5]
tattoos = snapInvLiDoc.Gift_Bags[g6]
campFlyers = snapInvLiDoc.Gift_Bags[g7]
buttons = snapInvLiDoc.Gift_Bags[g8]

#Slime Ingredients dictionary call and variable set
s1 = 'Bowls'
s2 = 'Shaving Cream'
s3 = 'Glue'
s4 = 'Baking Soda'
s5 = 'Contact Solution'

Bowls = snapInvLiDoc.Slime_Ingredients[s1]
shavingCream = snapInvLiDoc.Slime_Ingredients[s2]
Glue = snapInvLiDoc.Slime_Ingredients[s3]
bakingSoda = snapInvLiDoc.Slime_Ingredients[s4]
contactSolution = snapInvLiDoc.Slime_Ingredients[s5]

#Cleaning Supplies dictionary call and variable set
c1 = 'Surface Cleaner'
c2 = 'Paper Towels'
c3 = 'Clorox Wipes'
c4 = 'Black Bags(L)'
c5 = 'White Bags(S)'
c6 = 'Windex'
c7 = 'Dish Soap'
c8 = 'Toilet Cleaner'
c9 = 'Hand soap'
c10 = 'Toilet Paper'
c11 = 'Gloves'
c12 = 'Swiffer Wipes'

surfaceCleaner = snapInvLiDoc.Cleaning_Supplies[c1]
towels = snapInvLiDoc.Cleaning_Supplies[c2]
clorox = snapInvLiDoc.Cleaning_Supplies[c3]
blackBags = snapInvLiDoc.Cleaning_Supplies[c4]
whiteBags = snapInvLiDoc.Cleaning_Supplies[c5]
Windex = snapInvLiDoc.Cleaning_Supplies[c6]
dishSoap = snapInvLiDoc.Cleaning_Supplies[c7]
toiletCleaner = snapInvLiDoc.Cleaning_Supplies[c8]
handSoap = snapInvLiDoc.Cleaning_Supplies[c9]
toiletPaper = snapInvLiDoc.Cleaning_Supplies[c10]
gloves = snapInvLiDoc.Cleaning_Supplies[c11]
swifferWipes = snapInvLiDoc.Cleaning_Supplies[c12]

#Random dictionary call and variable set
r1 = 'Snacks'
r2 = 'Kleenex'
r3 = 'Ziploc Total'
r4 = 'Ziploc Sandwich'
r5 = 'Ziploc Quart'
r6 = 'Ziploc Gallon'
r7 = 'Water Cups'
r8 = 'WEDO Extras'
r9 = 'USB'
r10 = 'Confetti'
r11 = 'Paper Bags'
r12 = 'Flying Toys'
r13 = 'Box Crayons'
r14 = 'Color Notebooks'
r15 = 'Toys'
r16 = 'Animal Toys'

Snacks = snapInvLiDoc.Random[r1]
Kleenex = snapInvLiDoc.Random[r2]
ziplocT = snapInvLiDoc.Random[r3]
ziplocS = snapInvLiDoc.Random[r4]
ziplocQ = snapInvLiDoc.Random[r5]
ziplocG = snapInvLiDoc.Random[r6]
waterCups = snapInvLiDoc.Random[r7]
wExtras = snapInvLiDoc.Random[r8]
uSB = snapInvLiDoc.Random[r9]
confetti = snapInvLiDoc.Random[r10]
paperBags = snapInvLiDoc.Random[r11]
fToys = snapInvLiDoc.Random[r12]
crayons = snapInvLiDoc.Random[r13]
cNotebooks = snapInvLiDoc.Random[r14]
toys = snapInvLiDoc.Random[r15]
aToys = snapInvLiDoc.Random[r16]


#Functions to display dictionairy amounts
def main():
    return


print("We have " + plates + " plates.")
#while '__name__' == '__main__':
    #main()
    #break