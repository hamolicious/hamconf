import os

path = __file__.replace(os.path.basename(__file__), '')
all_files = ''
for file in os.listdir('unit_tests/'):
	filepath = os.path.join(path, file)
	if not file.startswith('test_') : continue
	all_files += f' {filepath}'

os.system(f'python -m unittest -v {all_files}')
