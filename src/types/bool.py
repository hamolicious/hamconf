from . import Definitions

class Boolean(Definitions):
	type_name = 'bool'

	@staticmethod
	def convert(value: str) -> bool:
		return value.lower() == 'true'

