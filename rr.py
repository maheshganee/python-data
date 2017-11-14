data='''1234 hari bangalore 9000
1235 ravi chennai 100000
1236 rajesh hyderabad 11000
1237 kiran bangalore 12000
1238 raju bangalore 13000
1240 chinnu hyderabad 14000'''
m={}
for row in data.split('\n'):
	i=row.split()
	m[i[0]] = {'name':i[1],'location':i[2],'salary':i[3]}
print m