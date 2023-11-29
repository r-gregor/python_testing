actors = { "James Franco": ["Spiderman", "172 hours", "Mountain X" ],
            "Tobey McGuire": ["My Hospital", "Garry Fisher", "Spiderman"],
            "Gillian Anderson": ["The X files", "My Hospital", "Faithful"]
}

print("----------------------------------------------------------------------")
for k, v in actors.items():
    print("{}".format(k), end = ": ")
    print(*v, sep = ", ")


print("----------------------------------------------------------------------")
dic = {'key1': ["value1",  "value2"],
       'key2': ["value77", "something"] }
print("value77" in [x for v in dic.values() for x in v])


print("----------------------------------------------------------------------")
for k in actors.keys():
    for e in actors[k]:
        if "Spiderman" in e:
            print(k)

print("----------------------------------------------------------------------")
print([k for k in actors.keys() for e in actors[k] if "Spiderman" in e])


print("----------------------------------------------------------------------")
for v in actors.values():
    for e in v:
        print(e)


print("----------------------------------------------------------------------")
print({e for v in actors.values() for e in v})


'''
print("----------------------------------------------------------------------")
for k in actors.keys():
    for e in actors[k]:
        if e in {e for v in actors.values() for e in v}:
            print(k, e)
'''

print("----------------------------------------------------------------------")
for m in {e for v in actors.values() for e in v}:
    for k in actors.keys():
        if m in actors[k]:
            print(k, end = ", ")
    print(" __" + m + "__ ")
