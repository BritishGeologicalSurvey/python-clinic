# Read
with open('co2_mm_mlo.txt') as f:
	lines = f.readlines()
# Process
decade_data = {}
old_decade = '1900'
for line in lines:
	if not line.startswith('#'):
		line = line.strip().split()
		decade = line[0][0:3] + '0'
		if decade > old_decade:
			old_decade = decade
			decade_data[decade] = 'decimal_date,interpolated\n'
		decade_data[decade] += ','.join([line[2], line[4]]) + '\n'
# Write
for decade in decade_data:
	with open(f'co2_mm_{decade}s.csv', 'w') as f:
		f.write(decade_data[decade])
