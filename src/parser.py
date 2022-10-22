import json
import os
from typing import Any, Type
from . import Config
from .types import Definitions


def convert_to_type(type_: str, value: str, line_number: int) -> Any:
	array = False

	if type_ == 'arr' : raise SyntaxError(f'Array requires a type `[arr ____]` on line: {line_number}')

	if type_.split(' ')[0] == 'arr' and '[' in value.split('=')[-1] and ']' in value.split('=')[-1]:
		array = True
		value = value[1:-1].replace(', ', ',').split(',')
		type_ = type_.split(' ')[-1]

	converter = Definitions.type_definitions.get(type_)
	if converter is None:
		raise TypeError(f'Type: ({type_}) is not defined')

	if type(value) is str and value.startswith('${'):
		env_var_name = value.replace('${', '')[:-1]
		new_value = os.environ.get(env_var_name)
		if new_value is None : raise ValueError(f'Environment variable {env_var_name} is not set')
		value = new_value

	try:
		if not array:
			return converter.convert(value)
		if array:
			return [converter.convert(v) for v in value]
	except ValueError:
		raise ValueError(f'Value: {value} is wrong format for type: {type_}, line number: {line_number}')


def read_file(filename: str) -> str:
	if not os.path.exists(filename):
		raise FileExistsError(f'File not found {filename}')

	with open(filename, 'r') as f:
		return f.read().split('\n')


def strip_comments(data: str) -> str:
	output = []
	for line in data:
		if '//' in line:
			line = line.split('//')[0].strip()

		output.append(line)

	return output


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

	value = convert_to_type(data_type, value, line_number)

	return var_name, data_type, value


def add_to_section(section: str, data: dict, var_name: str, new_data: dict) -> dict:
	data[section][var_name] = new_data
	return data


def parse_file(filename: str) -> Config:
	data = read_file(filename)
	data = strip_comments(data)

	config = {}
	attribs = {}

	current_section = None
	line_number = 0

	for line in data:
		line_number += 1
		if line == '' : continue

		if line.startswith('@'):
			attribs[line[1:].split(' ')[0].strip()] = line[1:].split(' ')[1].strip()
			continue

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

	return Config(config, attribs)

