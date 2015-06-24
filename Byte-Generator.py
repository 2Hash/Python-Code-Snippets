import sys
b = [i for i in range(10)]
b.extend(['a', 'b', 'c', 'd', 'e', 'f', "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
byte = b
 
for x in b:
    for y in b:
       sys.stdout.write('\\x' + str(x) + str(y))
