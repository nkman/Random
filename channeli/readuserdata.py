import json

f = open('userdata.json','r')
data = f.read().split('\n')
f.close()
q = []
i = 0
f = open('userdata','a')
for t in data:
	try:
		if (json.loads(t)[0]["id"] != '00000000'):
			f.write(t+'\n')
			i += 1
		pass
	except ValueError:
		pass
	
	print i
	
f.close()