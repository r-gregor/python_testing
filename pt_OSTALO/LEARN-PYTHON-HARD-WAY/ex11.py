#! /usr/bin/env python3

print("How old are you?",)
age = input()

print("How tall are you?",)
height = input()

print("How much do you weigh?")
weight = input()

print("So, you'r %r old, %r tall and %r heavy." % (age, height, weight))


print("""
# replaced %r and %s:
print("How old are you?")
age = input()

print("How tall are you?")
height = input()

print("How much do you weigh?")
weight = input()

print("So, you'r %s old, %s tall and %s heavy." % (age, height, weight))
""")
