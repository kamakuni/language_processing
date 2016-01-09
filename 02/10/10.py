with open("hightemp.txt","r") as file:
	print(sum(1 for _ in file))