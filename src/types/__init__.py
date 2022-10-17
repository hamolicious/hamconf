

import os
from typing import Any


class Definitions:
	type_definitions = {}
	type_name: str = 'base'

	@classmethod
	def _register(cls):
		Definitions.type_definitions[cls.type_name] = cls

	@staticmethod
	def convert(value: str) -> Any: ...

if __name__ != '__main__':
	path = __file__.replace(os.path.basename(__file__), '')
	for file in os.listdir(path):
		if file.startswith('__') : continue
		package = __import__(f'src.types.{file.replace(".py", "")}')

	for cls in Definitions.__subclasses__():
		cls._register()

