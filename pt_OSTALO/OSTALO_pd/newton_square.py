n1 = 1.0

for i in range (15):

    n2 = (1.0/2.0) * (n1 + (2.0/n1))
    print(f"{n2:.52f}")
    n1 = n2

