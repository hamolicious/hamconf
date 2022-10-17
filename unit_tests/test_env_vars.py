import unittest
from src import parse_file
import os


class EnvVarFetching(unittest.TestCase):
	def setUp(self) -> None:
		os.environ['SOME_ENV_VAR'] = '3.5734'
		os.environ['JSON_ENV_VAR'] = '{"value": 123}'

	def tearDown(self) -> None:
		del os.environ['SOME_ENV_VAR']
		del os.environ['JSON_ENV_VAR']

	def test_value_float_fetched(self):
		data = parse_file('unit_tests/files/env_vars.hamconf').get('SECTION.env_var_float')
		self.assertEqual(data, 3.5734)

	def test_value_json_fetched(self):
		data = parse_file('unit_tests/files/env_vars.hamconf').get('SECTION.env_var_json')
		self.assertEqual(data, {"value": 123})


if __name__ == '__main__':
	unittest.main()
