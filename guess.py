import random

n = 0
while True:
	n = int(input("选择答案位数："))
	if n<1 or n>10:
		print("位数至少为1，至多为10！")
	else:
		break

def diff(a):
	b = []
	for each in range(n):
		b.append(a%10)
		a = a//10
	for i in range(n):
		for j in range(i+1,n):
			if b[i]==b[j]:
				return False
	else:
		return True

def check(a,b):
	golden = 0
	blue = 0
	c = []
	d = []
	for i in range(n):
		c.append(a%10)
		d.append(b%10)
		a = a//10
		b = b//10
		if c[i]==d[i]:
			golden = golden+1
	for i in range(n):
		for j in range(n):
			if i!=j and c[i]==d[j]:
				blue = blue+1
	print("Golden:{0}, Blue:{1}".format(golden, blue))

while True:
	min=0
	max=0
	for i in range(n):
		min = min*10+i
		max = max*10-i+9
	a = random.randint(min,max+1)
	if diff(a):
		break

while True:
	c = input("猜数字：")
	if c == "answer":
		if a<10**(n-1):
			print("Answer is 0" + str(a))
		else:
			print("Answer is " + str(a))
		continue
	else:
		b = int(c)
	if not diff(b):
		print("RULES!")
		continue
	if b==a:
		print("Bingo!")
		break
	else:
		check(a,b)