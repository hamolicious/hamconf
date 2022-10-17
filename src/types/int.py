from . import Definitions

class Int(Definitions):
	type_name = 'int'

	@staticmethod
	def convert(value: str) -> int:
		return int(value)

