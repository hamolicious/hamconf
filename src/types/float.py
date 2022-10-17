from . import Definitions

class Float(Definitions):
	type_name = 'float'

	@staticmethod
	def convert(value: str) -> float:
		return float(value)

