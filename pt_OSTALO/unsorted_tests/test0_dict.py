print("The contents of a dictionary 'D'")
D = {'a':1, 'b':2, 'c':3}
print(D)

print("\nPrinting SORTED key => value column ...")
for key in sorted(D):
    print(key, '=>', D[key])


N = "Gregor Redelonghi"
print("\nPrinting", "'" + N + "'", "in all UPPERCASE")
print('''with FOR loop:
<code>
for c in N:
    print(c.upper(), end='')
</code>
''')

print("Result:")
for c in N:
    print(c.upper(), end='')

print()
    

f = open("fajl.txt", "wt")
f.write("""
For example, to create a text output file, you would pass in its name and the 'w' pro-
cessing mode string to write data:
    f = open('data.txt', 'w')
    f.write('Hello\n') # Make a new file in output mode ('w' is write)
    # Write strings of characters to it
    f.write('world\n') # Return number of items written in Python 3.X
    f.close() # Close to flush output buffers to disk
    
This creates a file in the current directory and writes text to it (the filename can be a
full directory path if you need to access a file elsewhere on your computer). To read
back what you just wrote, reopen the file in 'r' processing mode, for reading text input
—this is the default if you omit the mode in the call. Then read the file’s content into
a string, and display it. A file’s contents are always a string in your script, regardless of
the type of data the file contains:
    122 | Chapter 4: Introducing Python Object Types
    www.it-ebooks.info>>> f = open('data.txt')
    >>> text = f.read()
    >>> text
    'Hello\nworld\n' # 'r' (read) is the default processing mode
    # Read entire file into a string
    >>> print(text)
    Hello
    world # print interprets control characters
    >>> text.split()
    ['Hello', 'world'] # File content is always a string
    
Other file object methods support additional features we don’t have time to cover here.
For instance, file objects provide more ways of reading and writing ( read accepts an
optional maximum byte/character size, readline reads one line at a time, and so on),
as well as other tools ( seek moves to a new file position). As we’ll see later, though, the
best way to read a file today is to not read it at all—files provide an iterator that auto-
matically reads line by line in for loops and other contexts:
    >>> for line in open('data.txt'): print(line)
""")
f.close()

f = open("fajl.txt", "rt")
text = f.read()
print(text)
