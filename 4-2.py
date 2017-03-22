#!/usr/bin/python
import sys
print(sys.argv)
f = open(sys.argv[1])
lines = f.readlines()
f.close()

print(lines)

fint = [int(line) for line in lines]
fint =[]
for line in lines:
	fint.append(int(line))
