n = open("mula_01.txt","r")  # open file, read-only
s = open("mula_02.txt", "w") # open file, write
lines = n.readlines()
lines.sort()

for line in lines:
	s.write(line)
n.close()
s.close()
