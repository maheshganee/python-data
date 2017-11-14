data='''hari bangalore 9000
		ravi chennai 100000
		rajesh hyderabad 11000
		kiran bangalore 12000
		raju bangalore 13000
		chinnu hyderabad 14000'''
f=[]
for row in data.split('\n'):
	if 'bangalore' in row.split():
		f.append(row.split()[0])		
print f