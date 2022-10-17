from . import Definitions
import json

class JSON(Definitions):
	type_name = 'json'

	@staticmethod
	def convert(value: str) -> dict:
		return json.loads(value)

