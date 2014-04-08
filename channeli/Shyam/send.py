import requests
import re
import json

def Login(user='nair1uec',passw=''): #Login in Channeli.
	url = 'https://channeli.in/login/?next=/'
	s = requests.Session()
	s.get(url)
	csrftoken = s.cookies['csrftoken']
	login_data = dict(username=user, password=passw, csrfmiddlewaretoken=csrftoken, remember_me='off')
	s.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36'})
	s.post(url, data=login_data, headers=dict(Referer=url))
	return s

def CreateName():
	f = open('name.txt','w')
	f.close()
	f = open('name.txt','a')
	for i in range(97,123):
		for j in range(97,123):
			for k in range(97,123):
				f.write(chr(i)+chr(j)+chr(k)+'\n')
	f.close()

def Match(t,p):
	f = p.split('\n')
	if t not in p:
		return True
	else:
		return False

def PersonSearch():
	url = 'https://channeli.in/connect-e-dil/person_search/'
	hero = Login()
	csrftoken = hero.cookies['csrftoken']
	fm = {
	'Referer':'https://channeli.in/connect-e-dil/',
	'Host':'channeli.in',
	'X-Requested-With':'XMLHttpRequest',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36'}
	f = open('name.txt','r')
	names = f.read().split('\n')
	f.close()
	count = 1
	for n in names:
		data = {
		'term':n
		}
		try:
			g = open('userdata.json','r')
			co = g.read()
			g.close()
		except IOError:
			co = ''
			pass
		print "Trying with %s and sent %d" % (str(n),count)
		#fm.update({'csrftoken':hero.cookies['csrftoken']})
		
		try:
			p = hero.get(url,headers=fm,params=data)
		except Exception, e:
			pass
		f = open('userdata.json','a')
		if Match(p.text,co):
			if(json.loads(p.text)[0]['id'] != "00000000"):
				f.write(p.text+'\n')
				pass
		f.close()
		count += 1
		#print KillSession()
	#f.close()
	return "Success"

def send():
	j = 0
	url = 'https://channeli.in/connect-e-dil/'
	Hero = Login()
	csrftoken = Hero.cookies['csrftoken']
	p = open('userdata','r')
	a = p.read().split('\n')
	p.close()
	fm = {
	'Referer':'https://channeli.in/connect-e-dil/',
	'Host':'channeli.in',
	'Origin':'https://channeli.in',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36'}
	for n in a:
		n = json.loads(n)
		for i in range(0,len(n)):
			data = {
			'csrfmiddlewaretoken':csrftoken,
			'enroll':n[i]["id"],'person':n[i]["value"],
			'rose_colour':'RR',
			'anon':'on',
			'message':'',
			'rossy':'Send'
			}
			try:
				p = Hero.post(url,headers=fm,data=data)
				print "Sending %d Red rose to %s " % (j,n[i]["value"])
				pass
			except Exception, e:
				pass			
			j += 1
send()
