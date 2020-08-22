

#----------entry of the numbers by the two players--------

import getpass, termcolor
from termcolor import colored,cprint

print()
i=1
p1=0
p2=0
game_run=True
while game_run:
	r=colored("                               ROUND ","green")
	print(r,i)
	i+=1
	print()
	k=getpass.getpass("PLAYER 1,please,enter your number ")
	k1=getpass.getpass("PLAYER 2,please,enter your number ")
	a=int(""+k)
	b=int(""+k1)
	if a<0:
		print("PLAYER 1,please enter a positive number greater than 0.")
		k2=getpass.getpass("PLAYER 1,please,enter your number ")
		c=int(""+k2)
		a=c
	if b<0:
		print("PLAYER 2,please enter a positive number greater than 0.")
		k3=getpass.getpass("PLAYER 2,please,enter your number ")
		d=int(""+k3)
		b=d
	print()
	print()
	
	#------------revealing of the numbers----------
	
	e=int(input("when you both are ready to reveal the numbers,input 1.  Take your time :) "))
	if e==1:
		print("PLAYER 1:",a)
		print("PLAYER 2:",b)
	print()
	print()
	
	
	#--------------------grading----------------------
	
	if a>b:
		cprint("first gets 2 points!",'cyan')
		p1+=2
		if b==a-1:
			cprint("second gets 1 point!",'red')
			p2+=1
	elif a==b:
		cprint("it's a draw!!",'green')
	else:
		cprint("second gets 2 points!",'red')
		p2+=2
		if a==b-1:
			cprint("first gets 1 point!","cyan")
			p1+=1
	print()
	print()
	
	
	#-----------------------score analysis------------------
	
	if p1>=5 and p1>p2:
		cprint("                      !!! PLAYER 1  WINS !!!","yellow")
		game_run=False
	elif p2>=5 and p2>p1:
		cprint("                      !!! PLAYER 2  WINS !!!","yellow")
		game_run=False
	elif p1==p2==5:
		cprint("                      !!! IT'S A DRAW!!!","green")
		game_run=False
	print()
	print()
	
	
	



