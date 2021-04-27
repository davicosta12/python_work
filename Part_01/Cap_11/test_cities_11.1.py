import unittest
from city_functions import devolve_city_country

class CityTestCase(unittest.TestCase):
	
	def test_city_country(self):
		city_formatada = devolve_city_country("são paulo", "brasil")
		self.assertEqual(city_formatada, "São Paulo, Brasil")
		
		
unittest.main()
		
