class Calculater:

	def __init__(self):
		print("

	def add(self,num_list):
		result=0
		for num in num_list:
			result += num
		return result
	def min(self,num_list):
		result=num_list[0]*2
		for num in num_list:
			result -= num
		return result

	
	def mul(self,num_list):
		result=1
		for num in num_list:
			result *= num
		return result

	def div(self,num_list):
		result=num_list[0]**2
		for num in num_list:
			result /= num
		return result
	
