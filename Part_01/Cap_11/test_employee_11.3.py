import unittest
from Funcionarios_113 import Employee

class EmployeeTestCase(unittest.TestCase):
	def setUp(self):
		self.funcionario = Employee('Davi', 'Silva', 5000)
	
	def test_give_default_raise(self):
		self.funcionario.give_raise()
		self.assertEqual(self.funcionario.salario_anual, 10000)
		
	def test_give_custom_raise(self):
		self.funcionario.give_raise(200)
		self.assertEqual(self.funcionario.salario_anual, 5200)


unittest.main()
