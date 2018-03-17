import random as r

def calc():
	a = r.randint(1,100)
	b = r.randint(1,100)
	c = r.randint(1,3)
	if c == 1:
		k = '+'
	elif c == 2:
		k = '-'
	elif c == 3:
		k = '*'
	
	I = str(a)+k+str(b)
	return I
		

A = calc()
message = input(A+'=')

if eval(A) == int(message):
	print('맞았어요!')
else:
	print('틀렸어요!')
