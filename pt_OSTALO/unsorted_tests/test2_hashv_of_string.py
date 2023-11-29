S = input("Enter a string: ___ ")
hsh =0
nhsh = 0
for chr in S:
    hsh = hsh + ord(chr)
    nhsh %= 5

print("Hash number of string \"" + S + "\" is:", hsh)
print("Mod 5 of hash value is:", nhsh)


