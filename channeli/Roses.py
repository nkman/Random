#Author - Nkman 

import requests
import re
import json

def Login(user='****',passw='****'): #Login in Channeli.
	url = 'https://channeli.in/login/?next=/'
	s = requests.Session()
	s.get(url)
	csrftoken = s.cookies['csrftoken']
	login_data = dict(username=user, password=passw, csrfmiddlewaretoken=csrftoken, remember_me='off')
	s.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36'})
	s.post(url, data=login_data, headers=dict(Referer=url))
	return s

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
		g = open('userdata.json','r')
		co = g.read()
		g.close()
		print "Trying with %s and sent %d" % (str(n),count)
		#fm.update({'csrftoken':hero.cookies['csrftoken']})
		p = hero.get(url,headers=fm,params=data)
		f = open('userdata.json','a')
		if Match(p.text,co):
			f.write(p.text+'\n')
			pass
		f.close()
		count += 1
		#print KillSession()
	#f.close()
	return "Success"

def send():
	url = 'https://channeli.in/connect-e-dil/'
	Hero = Login()
	csrftoken = Hero.cookies['csrftoken']
	p = open('userdata.json','r')
	a = p.read().split('\n')
	p.close()
	fm = {
	'Referer':'https://channeli.in/connect-e-dil/',
	'Host':'channeli.in',
	'Origin':'https://channeli.in',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36'}
	for n in a:
		n = json.loads(n)
		if(n[0]['id'] != "00000000"):
			data = {
			'csrfmiddlewaretoken':csrftoken,
			'enroll':n[0]["id"],'person':n[0]["value"],
			'rose_colour':'RR',
			'anon':'on',
			'message':'',
			'rossy':'Send'
			}
			p = Hero.post(url,headers=fm,data=data)
			print "Sending Red rose to %s " % n[0]["value"]
PersonSearch()
