import random

def diff(a):
	b = []
	for each in range(4):
		b.append(a%10)
		a = a//10
	if b[0]==b[1] or b[0]==b[2] or b[0]==b[3] or b[1]==b[2]or b[1]==b[3]or b[2]==b[3]:
		return False
	else:
		return True

def check(a,b):
	golden = 0
	blue = 0
	c = []
	d = []
	for i in range(4):
		c.append(a%10)
		d.append(b%10)
		a = a//10
		b = b//10
		if c[i]==d[i]:
			golden = golden+1
	for i in range(4):
		for j in range(4):
			if i!=j and c[i]==d[j]:
				blue = blue+1
	print("Golden:{0}, Blue:{1}".format(golden, blue))

while True:
	a = random.randint(1,1000)
	if diff(a):
		break

while True:
	b = int(input("猜数字："))
	if not diff(b):
		print("RULES!")
		continue
	if b==a:
		print("Bingo!")
		break
	else:
		check(a,b)