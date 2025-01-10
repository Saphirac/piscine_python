def NULL_not_found(object: any) -> int:
	
	t = type(object)

	if (object == None) :
		print("Nothing : None", t)
	elif (object == float("NaN")) :
		print("Cheese : nan", t)
	elif (object == 0 and t == int) :
		print("Zero :", 0, t)
	elif (object == '') :
		print("Empty :", t)
	elif (object == False) :
		print("Fake :", t)
	else :
		print("Type not Found")
		return 1
	return 0

