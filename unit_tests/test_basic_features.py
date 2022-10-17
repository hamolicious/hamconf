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

	def test_acquiring_float_arrays(self):
		obj = parse_file('unit_tests/files/basic_file.hamconf')
		value = obj.get('SECTION.SUB_SECTION.float_array')
		self.assertTrue(all(
			map(lambda v : type(v) is float, value)
		))

	def test_acquiring_string_arrays(self):
		obj = parse_file('unit_tests/files/basic_file.hamconf')
		value = obj.get('SECTION.SUB_SECTION.str_array')
		self.assertTrue(all(
			map(lambda v : type(v) is str, value)
		))

if __name__ == '__main__':
	unittest.main()
