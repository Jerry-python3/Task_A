w = open("a.txt", "r")
dd = w.read()
mass = []
summa = 0

words = dd.split(",")

for x in words: 
	for y in x:
		if y == '+':
			summa += 1

s = len(words)
print(s)
print(summa)

print(((s + summa+2)*100))