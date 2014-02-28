import requests as r
import urllib2 as u
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def Login():
	s = r.Session()
	
	data = { 'email':'anonymous@anonimity.com',
		'password':'bitchesaway' }
	url = 'http://www.cipher.azeotropy.com/'
	s.get(url)
	s.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36'})
	s.post(url, data=data)
	return s

def Generator():
	url = ['http://en.wikipedia.org/wiki/One_Ring','http://en.wikipedia.org/wiki/The_Lord_of_the_Rings','http://en.wikipedia.org/wiki/Chemical_engineering']
	text_obtained = ''
	for t in url:
		print "Fetching %s from Internet" % t
		p = u.urlopen(t).read()
		p = remove_tags(p)
		text_obtained = text_obtained + p
	send_data = text_obtained.split()
	print send_data
	send_data = set(list(send_data))
	return send_data

def worker():
	data = Generator()
	user = Login()
	i = 0
	for t in data:
		data_ = {'answer':str(t),'ajax':'ajax'}
		t_ = user.post('http://www.cipher.azeotropy.com/start',data=data_)
		if(t_.text=='{status: true}'):
			print t_
		print str(i)+ " Requests sent"
		i += 1

	
worker()
