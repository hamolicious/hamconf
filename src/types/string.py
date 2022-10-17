from . import Definitions

class String(Definitions):
	type_name = 'str'

	@staticmethod
	def convert(value: str) -> str:
		return value[1:-1] \
			if value.startswith('\'') or value.startswith('\"') \
			else value

