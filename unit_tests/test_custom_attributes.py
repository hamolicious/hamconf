import unittest
from src import parse_file, Config


"""
Currently there is no need for versioning, but just in case, I'd rather have the support partially implemented
"""


class CustomAttributes(unittest.TestCase):
	def test_versioning(self):
		obj = parse_file('unit_tests/files/basic_file.hamconf')
		self.assertEqual(obj.version, '1')

if __name__ == '__main__':
	unittest.main()
