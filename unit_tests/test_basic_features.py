import unittest
from src import parse_file, Config


class BasicFeatures(unittest.TestCase):

	def test_basic_parsing(self):
		obj = parse_file('unit_tests/files/basic_file.hamconf')
		self.assertIsInstance(obj, Config)

	def test_acquiring_values(self):
		obj = parse_file('unit_tests/files/basic_file.hamconf')
		value = obj.get('SECTION.str_hello_world')
		self.assertEqual(value, 'Hello World')

if __name__ == '__main__':
	unittest.main()
