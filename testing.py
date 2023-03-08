import snapInvLiDoc

oldFile = open("snapInvLiDoc.py", 'r')
edFile = open("editedsnapInvLiDoc.py", 'w')

seCat = ""
seItem = ""

parties = snapInvLiDoc.Parties
giftBags = snapInvLiDoc.GiftBags
slimeIngredients = snapInvLiDoc.SlimeIngredients
cleaningSupplies = snapInvLiDoc.CleaningSupplies
random = snapInvLiDoc.Random

cats = [parties, giftBags, slimeIngredients, cleaningSupplies, random]

def dispLabel(seCat):
    if seCat == "parties":
        print(parties.keys())
        seItem = input("Which item?")
        for key in parties:
            if seItem == key:
                print(parties[key])
    if seCat == "giftBags":
        print(giftBags.keys())
        seItem = input("Which item?")
        for key in giftBags:
            if seItem == key:
                print(giftBags[key])
    if seCat == "slimeIngredients":
        print(slimeIngredients.keys())
        seItem = input("Which item?")
        for key in slimeIngredients:
            if seItem == key:
                print(slimeIngredients[key])
    if seCat == "cleaningSupplies":
        print(cleaningSupplies.keys())
        seItem = input("Which item?")
        for key in cleaningSupplies:
            if seItem == key:
                print(cleaningSupplies[key])
    if seCat == "random":
        print(random.keys())
        seItem = input("Which item?")
        for key in random:
            if seItem == key:
                print(random[key])

def upAmouont():
    return

def main():
    dispLabel(input("Which category(write as seen):\nparties\ngiftBags\n" +
                  "slimeIngredients\ncleaningSupplies\nrandom\n"))
    return

main()

