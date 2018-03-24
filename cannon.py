import turtle as t
import random
#위 화살표를 누르면 각도가 올라간다
def up():
	t.left(2)
#아래 화살표를 누르면 각도가 내려간다 	
def down():
	t.right(2)
#스페이스바를 누르면 화살표가 나간
def shoot():
	ang = t.heading()
	while t.ycor()>0:
		t.fd(15)
		t.right(5)
	dis = t.distance(target,0)
	t.sety(random.randint(10,100))
	if dis <= 25:
		t.color('blue')
		t.write("Good!",False,"center",("",15))
		
	else:
		t.color('red')
		t.write('Awoooo',False,"center",("",15))
	
	t.goto(-200,10)
	t.setheading(ang)
	t.color('black')
#바탕 
t.color('green')
t.goto(-300,0)
t.down()
t.goto(300,0)
#타겟 
t.up()
t.color('blue')
target = random.randint(50,150)
t.pensize(10)
a = target+25
b = target-25
t.goto(a,0)
t.down()
t.goto(b,0)
t.up()
t.color('black')
t.goto(-200,10)
#키 연동
t.onkeypress(up,'Up')
t.onkeypress(down,'Down')
t.onkeypress(shoot,'space')
t.listen()

t.mainloop()
