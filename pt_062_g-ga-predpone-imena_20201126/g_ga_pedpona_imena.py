#! /usr/bin/env python3

inf = "names.txt"
outf = "imena-s-predponami.txt"

mimena = [
"Miha",
"Jaka",
"Matija",
"Luka",
"Mitja",
"Žiga",
"Grega",
"Aljoša"
]

kimena = []

with open(inf, "r") as NMS:
    for line in NMS:
        line = line.strip()
        ime = line.split(",")[0]
        if ime.endswith("a") and ime not in mimena:
            pref = "Ga."
        else:
            pref = "G."
        # print(pref + "," + line)
        kimena.append((pref,line))

with open(outf, "w") as DBS: 
    for el in kimena:
        line = el[0] +","+ el[1] + "\n"
        DBS.write(line)
