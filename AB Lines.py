
letters = ["A","B"]
Line1 = []
Line2 = []
def linemaker1(Line1):
    count = 3
    while count>0:
        for i in range(0, 2):
            Line1.extend(letters[i])
        count-=1
    return Line1
def linemaker2(Line2):
    count = 3
    while count>0:
        for i in range(0, 2):
            Line2.extend(letters[i-1])
        count-=1
    return Line2
def printline(Line1, Line2):
    i = 3
    while i>0:
        print(Line1)
        print(Line2)
        i-=1
printline(linemaker1(Line1),linemaker2(Line2))