import unittest 
from name_function import retorna_nome_formatado

class NamesTestCase(unittest.TestCase): # Método de herança, herda todos os métodos e atributos da unittest.TestCase
	"""Testes para 'name_function.py'"""
	
	def test_primeiro_segundo_nome(self):
		"""Nomes como 'Janis Joplin' funcionam?"""
		nome_formatado = retorna_nome_formatado('janis', 'joplin')
		self.assertEqual(nome_formatado, 'Janis Joplin') # método de asserção verifica se um resultado recebido é igual ao resultado que você esperava receber.
                                                         # vê se o nome_formatado é igual a 'Janis Joplin'
                                                         # se não for, me avise!!!
	def test_primeiro_meio_final_nome(self):
		"""Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""
		nome_formatado = retorna_nome_formatado('wolfgang', 'mozart', 'amadeus')
		self.assertEqual(nome_formatado, 'Wolfgang Amadeus Mozart')
		
		
unittest.main()
