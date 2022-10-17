from typing import Any
from .exceptions import SectionNotFound, ValueNotFound


class Config:
	def __init__(self, config: dict, attribs: dict) -> None:
		self.__config = config
		self.__set_attributes(attribs)

	def __set_attributes(self, attribs: dict) -> None:
		for key in attribs:
			self.__setattr__(key, attribs.get(key))

	def get(self, path: str) -> Any:
		if '.' not in path:
			raise SyntaxError(f'Path {path} is invalid')

		var = path[-path[::-1].index('.')::]
		path = path.replace(var, '')[:-1:]
		end_path = self.__config.get(path)

		if end_path is None:
			raise SectionNotFound(f'Section path: {path} cannot be found')
		if end_path.get(var) is None:
			raise ValueNotFound(f'Value: {var} cannot be found')

		value = end_path.get(var).get('value')
		return value


