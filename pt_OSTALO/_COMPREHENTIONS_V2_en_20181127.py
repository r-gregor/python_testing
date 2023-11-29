#! /usr/bin/env python3

actors = { "James Franco": ["Spiderman", "172 hours", "Mountain X" ],
			"Tobey McGuire": ["My Hospital", "Garry Fisher", "Spiderman"],
			"Gillian Anderson": ["The X files", "My Hospital", "Faithful"],
			"Willem Dafoe": ["Movie 1, The X Files", "Spiderman"],
			"Kirsten Dunst": ["My Hospital", "Spiderman", "Anoinette"]
}

acts = list(actors.keys())

mvs = set()
for m in actors.values():
	for el in m:
		mvs.add(el)

print("Actors list", acts)
print("Movies:", mvs)

groupsL = []
groupsS = set()
for mv in mvs:
	groups = []
	
	for act in acts:
		if mv in actors[act]:
			groups.append(act)
	if len(groups) == 2:
		groupsL.append(set(groups))
	elif len(groups) > 2:
		for i in range(len(groups)):
			for j in range(i+1, len(groups)):
				pairs = set()
				pairs.add(groups[i])
				pairs.add(groups[j])
				groupsL.append(pairs)
				
print(*groupsL, sep = "\n")

for el in groupsL:
	groupsS.add(frozenset(el))
	
print(groupsS)


