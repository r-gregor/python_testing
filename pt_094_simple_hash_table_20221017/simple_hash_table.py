print("Creating a list of 99 values ...")
keys = [x for x in range(100)]

# print(keys)
# print("---")

t_size = 8
print(f"Setting the size of hash table to {t_size} slots ...")

# # test
# for key in keys:
#     print(str(key) + "\t" + str(key % t_size))

print(f"Creating a hash map of size {t_size} slots ...")
map = {}
for key in range(t_size):
    map[key] = []
# print(map)

print("---")

print(f"Populating hash map with elements from list of 99 values into {t_size} slots ...")
print(f"(hash function: value % num of slots ({t_size}))")
for key in keys:
    map[key % t_size].append(key)

# print(map)
for slot in map.keys():
    print(f"slot {slot}: {map[slot]}")
print("---")

'''
slot = t_size - 2
print(f"Elements in slot {slot}: ", end ="")
print(map[slot])
'''

