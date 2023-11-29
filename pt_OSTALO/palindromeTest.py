#! /usr/bin/env python3

def isEqual(L, D):
    if L == D:
        return True
    else:
        return False

def pTest(string):
    S1 = string.replace(" ", "").upper()
    print("\"" + S1 + "\"", end=" ")
    i = 0
    j = len(S1) - 1

    while not j < i:
        Levi = S1[i]
        Desni = S1[j]

        if not isEqual(Levi, Desni):
            print("String is NOT palindrome!")
            break

        # print(i, Levi, j, Desni)

        i += 1
        j -= 1

        if j < i:
            print("Hurray! String IS palindrome!")

for str in ["ana Voli MiloVana", "Gregor Redelonghi", "ANA", "MIHA", "ABBA", "AC/DC", "AABBcBBAA"]:
    pTest(str)
    
