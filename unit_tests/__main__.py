import os

path = __file__.replace(os.path.basename(__file__), '')
for file in os.listdir('unit_tests/'):
	filepath = os.path.join(path, file)
	if not file.startswith('test_') : continue
	os.system(f'python -m unittest -v {filepath}')
