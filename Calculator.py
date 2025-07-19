def calc(x,y,ops):

	if ops not in "+-/*":
		return "Please,only +, -, /, *"


	if ops=="+":
		return str(x)+" "+ops+" "+str(y)+" "+"="+str(x+y)

	if ops=="-":
		return str(x)+" "+ops+" "+str(y)+" "+"="+str(x-y)

	if ops=="/":
		return str(x)+" "+ops+" "+str(y)+" "+"="+str(x/y)

	if ops=="*":
		return str(x)+" "+ops+" "+str(y)+" "+"="+str(x*y)




while True:
	x=int(input("Please write first number"))
	y=int(input("Please write second number"))
	ops=input("Selec: +, -, /, *")

	print(calc(x,y,ops))
