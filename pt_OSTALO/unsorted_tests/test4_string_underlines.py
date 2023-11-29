def underl(name):
    L = "_"*75
    LL = list(L)
    
    for i in range(len(name)):
        if name[i] != ' ':
            LL[i+1] = name[i]

    for ltr in LL:
        print(ltr, end='')

    print()

        
NMS = ["Mark Redelonghi",
       "Tadeja Mali Redelonghi",
       "Zala Redelonghi",
       "Špela Redelonghi",
       "Gregor Redelonghi",
       "",
       "Valvasorjeva ulica 5, 1000 Ljubljana"
       ]
       
for NAMES in NMS:
    underl(NAMES)




