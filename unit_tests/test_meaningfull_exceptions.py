import unittest
from src import parse_file
from src.exceptions import SectionNotFound, ValueNotFound


class MeaningfullExceptions(unittest.TestCase):

	def test_sectionless_assignment(self):
		try:
			parse_file('unit_tests/files/sectionless_assingment.hamconf')
		except SyntaxError as e:
			self.assertEqual(str(e), 'Section-less variables are not supported line:3')

	def test_acquiring_undefined_section(self):
		try:
			parse_file('unit_tests/files/basic_file.hamconf') \
				.get('NOT_A_SECTION.value')
		except SectionNotFound as e:
			self.assertEqual(str(e), 'Section path: NOT_A_SECTION cannot be found')

	def test_acquiring_undefined_value(self):
		try:
			parse_file('unit_tests/files/basic_file.hamconf') \
				.get('SECTION.not_a_value')
		except ValueNotFound as e:
			self.assertEqual(str(e), 'Value: not_a_value cannot be found')

	def test_missing_data_type(self):
		try:
			parse_file('unit_tests/files/missing_type.hamconf')
		except SyntaxError as e:
			self.assertEqual(str(e), 'At line 4: `str_hello_world = \'Hello World\'`')

	def test_invalid_data_type(self):
		try:
			parse_file('unit_tests/files/invalid_type.hamconf')
		except TypeError as e:
			self.assertEqual(str(e), 'Type: (something) is not defined')

	def test_acquiring_section_alone(self):
		try:
			parse_file('unit_tests/files/basic_file.hamconf').get('SECTION')
		except Exception as e:
			self.assertEqual(str(e), 'Path SECTION is invalid')

	def test_typeless_array(self):
		try:
			parse_file('unit_tests/files/typeless_array.hamconf')
		except SyntaxError as e:
			self.assertEqual(str(e), 'Array requires a type `[arr ____]` on line: 4')

	def test_wrong_type(self):
		try:
			parse_file('unit_tests/files/missmatched_type.hamconf')
		except ValueError as e:
			self.assertEqual(str(e), 'Value: 23.6534 is wrong format for type: int, line number: 4')

	def test_undefined_env_var(self):
		try:
			parse_file('unit_tests/files/undefined_env_var.hamconf')
		except ValueError as e:
			self.assertEqual(str(e), 'Environment variable VERY_IMPORTANT_ENV_VAR is not set')

if __name__ == '__main__':
	unittest.main()
