

def super_sum(*args):
	'''
	takes in any number of numbers or a list and sums them up
	'''
	total = 0
	for element in args:
		if type(element) == list:
			for i in element:
				if type(i) == int:
					total= total + i
					
				elif type(i) != int:
		

		else:
			if type(element) == int:
				total = total + element
			else:
				return "wrong datatype"

	return total


