class Employee():
	
	def __init__(self, first, last, salario_anual):
		self.first = first
		self.last = last
		self.salario_anual = salario_anual
	
	
	def give_raise(self, aumento_salario=''):
		if aumento_salario:
			self.salario_anual = self.salario_anual + aumento_salario
		else:
			self.salario_anual = self.salario_anual + 5000
	
	def printa_novo_salario(self):
		print(self.novo_salario)
			



			 
		
