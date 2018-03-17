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
		
D = input("What's your name?")
print('Hello '+D+'!!!!!!!!!!!!!!!!!!!!!!!!!')


B = True
while B:
	A = str(calc())
	message = input(A+'=')
	if eval(A) == message:
		print('맞았어요!')
	else:
		print('틀렸어요!')
	C = input('Continue? (yes/no)')
	if C == 'no':
		B = False

print( 'Bye Bye '+D+'!!!!!!!!!!!!!!!!!!!')
