import os
from typing import Any, Type
from . import Config
from .types import Definitions

def type_str_to_type(type_: str) -> Type:
	converter = Definitions.type_definitions.get(type_)
	if converter is None:
		raise TypeError(f'Type: ({type_}) is not defined')
	return converter.convert


def read_file(filename: str) -> str:
	if not os.path.exists(filename):
		raise FileExistsError(f'File not found {filename}')

	with open(filename, 'r') as f:
		return f.read()


def strip_comments(data: str) -> str:
	new_data = ''
	slashes = 0
	for char in data:
		if char == '/'  : slashes += 1
		if char == '\n' : slashes = 0
		if slashes == 0 : new_data += char

	return new_data


def remove_multiple_chars(string: str, chars: str) -> str:
	for char in chars:
		string = string.replace(char, '')
	return string


def parse_assignment_line(line: str, line_number: int) -> tuple[str, Type, Any]:
	var_name, data_type, value = None, None, None

	try:
		var_name = line.replace(' ', '').split('[')[0].strip()
		data_type = line.split('[')[1][:line.split('[')[1].index(']')].strip()
		value = line.split('=')[-1].strip()
	except Exception as e:
		raise SyntaxError(f'At line {line_number}: `{line}`')

	value = type_str_to_type(data_type)(value)

	return var_name, data_type, value


def add_to_section(section: str, data: dict, var_name: str, new_data: dict) -> dict:
	data[section][var_name] = new_data
	return data


def parse_file(filename: str) -> Config:
	data = read_file(filename)
	data = strip_comments(data)

	config = {}

	current_section = None
	line_number = 0

	for line in data.split('\n'):
		line_number += 1
		if line == '' : continue

		if line.startswith('@') : continue

		if line.startswith('[') and line.endswith(']'):
			config[remove_multiple_chars(line, '[]')] = {}
			current_section = remove_multiple_chars(line, '[]')
			continue

		if current_section is None:
			raise SyntaxError(f'Section-less variables are not supported line:{line_number}')

		var_name, data_type, value = parse_assignment_line(line, line_number)
		config = add_to_section(current_section, config, var_name, {
			'value': value, 'type': data_type
		})

	return Config(config)
