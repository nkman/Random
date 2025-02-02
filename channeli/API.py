#Author - Nkman 

import requests
import re

def Login(user='nair1uec',passw=''): #Login in Channeli.
	url = 'https://channeli.in/login/?next=/'
	s = requests.Session()
	s.get(url)
	csrftoken = s.cookies['csrftoken']
	login_data = dict(username=user, password=passw, csrfmiddlewaretoken=csrftoken, remember_me='off')
	s.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36'})
	s.post(url, data=login_data, headers=dict(Referer=url))
	return s

def Birthday(): #get Todays Birthday.
	hero = Login()
	csrftoken = hero.cookies['csrftoken']
	fm = {
	'X-Requested-With':'XMLHttpRequest',
	'X-CSRFToken':csrftoken,
	'Referer':'https://channeli.in/',
	'Origin':'https://channeli.in',
	'Host':'channeli.in'}
	p = hero.post('https://channeli.in/birthday/today',data=dict(csrfmiddlewaretoken=csrftoken),headers=dict(fm))
	return p.text

def UpcomingEvents(): #get Upcoming birthdays.
	hero = Login()
	csrftoken = hero.cookies['csrftoken']
	fm = {
	'X-Requested-With':'XMLHttpRequest',
	'X-CSRFToken':csrftoken,
	'Referer':'https://channeli.in/',
	'Origin':'https://channeli.in',
	'Host':'channeli.in'}
	data = {
	'calendar_name':'all',
	'action':'first',
	'number':'3',
	'by_month_year':'',
	'id':''
	}
	p = hero.post('https://channeli.in/events/fetch',data=data,headers=dict(fm))
	return p.text

def Feeds(): #Get Feeds here
	hero = Login()
	data = {
	'action':'first',
	'id':'null',
	'number':'50'}
	csrftoken = hero.cookies['csrftoken']
	fm = {
	'X-Requested-With':'XMLHttpRequest',
	'X-CSRFToken':csrftoken,
	'Referer':'https://channeli.in/',
	'Origin':'https://channeli.in',
	'Host':'channeli.in'}
	p = hero.post('https://channeli.in/feeds/fetch',data=data,headers=dict(fm))
	return p.text

def KillSession():
	hero = Login()
	url = 'https://channeli.in/settings/sessions/'
	csrftoken = hero.cookies['csrftoken']
	fm = {
	'X-Requested-With':'XMLHttpRequest',
	'Referer':url,
	'X-CSRFToken':csrftoken,
	'Origin':'https://channeli.in',
	'Host':'channeli.in'}
	p = hero.post(url,headers=dict(fm))
	urls = re.findall(r'href = [\'"]?([^\'" >]+)', p.text)
	for i in urls:
		print 'logging out from session %s' % i.replace('/settings/killsession/','')
		hero.get('https://channeli.in'+i)
	return "Logged out from all %d sessions" % len(urls)

def Download(course): #Download lectures of a course #NotWorking
	hero = Login()
	url = 'https://channeli.in/lectut/pages/search.php'
	data = {
	'search':str(course) }
	csrftoken = hero.cookies['csrftoken']
	PHPSESSID = hero.cookies['PHPSESSID']
	fm = {
	'Referer':'https://channeli.in/lectut/pages/final_student.php',
	'Host':'channeli.in',
	'csrftoken':csrftoken,
	'PHPSESSID':PHPSESSID,
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36'}
	p = hero.get(url,data=data,headers=fm)
	return p.text

def Grades():
	grades = {}
	hero = Login()
	url = 'https://channeli.in/grades/'
	csrftoken = hero.cookies['csrftoken']
	PHPSESSID = hero.cookies['PHPSESSID']
	fm = {
	'Referer':'https://channeli.in/login/?next=/grades/',
	'Host':'channeli.in',
	'csrftoken':csrftoken,
	'PHPSESSID':PHPSESSID,
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36'}
	p = hero.get(url,headers=fm)
	urls = re.findall(r'<tr class="row"><td>[\'"]?([^\'"><]+)', p.text)
	grad = re.findall(r'</td><td>[\'"]?([^\'"><]+)', p.text)
	for i in range(0,len(urls)):
		grades[urls[i]] = grad[i]
	return grades

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

def CreateName():
	f = open('name.txt','a')
	for i in range(97,123):
		for j in range(97,123):
			for k in range(97,123):
				f.write(chr(i)+chr(j)+chr(k)+'\n')

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
	f.close()

#CreateName()
#PersonSearch()
print KillSession()
#print Download('ec-252')
