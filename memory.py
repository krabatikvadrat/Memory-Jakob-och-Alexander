import random

row1 = [1,2,3,4,5,6] 
row2 = [7,8,9,10,11,12]
row3 = [13,14,15,16,17,18]
row4 = [19,20,21,22,23,24]
row5 = [25,26,27,28,29,30]
row6 = [31,32,33,34,35,36]

cards = [1,1,2,2,3,3,4,4,5,5,6,6,
         7,7,8,8,9,9,10,10,11,11,12,12
         ,13,13,14,14,15,15,16,16,17,17,18,18]

field1 = []
field2 = []
field3 = []
field4 = []
field5 = []
field6 = []

def randomize():
    while len(cards) != 0:
        length = len(cards)
        choice = random.randint(1,6)
        choice2 = random.randint(0,length-1)
        if choice == 1 and (len(field1) != 6):
            field1.append(cards[choice2])
            cards.remove(cards[choice2])
        elif choice == 2 and (len(field2) != 6):
            field2.append(cards[choice2])
            cards.remove(cards[choice2])
        elif choice == 3 and (len(field3) != 6):
            field3.append(cards[choice2])
            cards.remove(cards[choice2])
        elif choice == 4 and (len(field4) != 6):
            field4.append(cards[choice2])
            cards.remove(cards[choice2])
        elif choice == 5 and (len(field5) != 6):
            field5.append(cards[choice2])
            cards.remove(cards[choice2])
        elif choice == 6 and (len(field6) != 6):
            field6.append(cards[choice2])
            cards.remove(cards[choice2])

randomize()

def printField():
    print(field1)
    print(field2)
    print(field3)
    print(field4)
    print(field5)
    print(field6)

def rows():
    print(row1)
    print(row2)
    print(row2)
    print(row4)
    print(row5)
    print(row6)

def replace():
    val1 = int(input("Välj en rad: "))
    val2 = int(input("välj en kolumn: "))
    if val1 == 1:
        row1[val2] = field1[val2]
    elif val2 == 2:
        row2[val2] = field2[val2]
    elif val2 == 3:
        row3[val2] = field3[val2]
    elif val2 == 4:
        row4[val2] = field4[val2]
    elif val2 == 5:
        row5[val2] = field5[val2]
    elif val2 == 6:
        row6[val2] = field6[val2]

printField()
replace()
rows()

