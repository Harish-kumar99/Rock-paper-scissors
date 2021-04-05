while True :
	print('Winning Rules as follows : \n Rock vs paper-> paper wins \n Rock vs scissor-> Rock wins \n paper vs scissor-> scissor wins.')
	print('Enter choice \n 1. Rock \n 2. paper \n 3. scissor ')
	p=int(input('enter your choice : '))
	i=['rock','paper','scissor']
	print('your coice is : ',i[p-1])
	import time
	print('computer is making choice wait.....')
	time.sleep(1.5)
	import random 
	j=random.randint(1,3)
	print('computers choice is : ',i[j-1])
	time.sleep(1)
	if (p==1 and j==1):
		print('both same try again')
		break
	elif (p==1 and j==2):
		print('computer won')
		break
	elif (p==1 and j==3):
		print('you won')
		break
	elif (p==2 and j ==1):
		print('you won')
		break 	
	elif (p==2 and j ==2):
		print('both same')
		break
	elif (p==2 and j ==3):
		print('computer won')
		break
	elif (p==3 and j ==1):
		print('computer won')
		break
	elif (p==3 and j ==2):
		print('you won')
		break
	elif (p==3 and j ==3):
		print('Both same')
		break
	
		
				