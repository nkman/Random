import requests as r
import time

def login():
	s = r.Session()
	url = "https://1.1.1.1/login.html"

	data = {

		"buttonClicked":4,
		"err_flag":0,
		"err_msg":"",
		"info_flag":0,
		"info_msg":"",
		"redirect_url":"",
		"network_name":"IIT",
		"username":"govind",
		"password":"Govind@123"
	}

	s.headers.update({
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate",
		"Accept-Language":"en-GB,en;q=0.8,en-US;q=0.6,hi;q=0.4",
		"Cache-Control":"max-age=0",
		"Connection":"keep-alive",
		"Content-Length":126,
		"Content-Type":"application/x-www-form-urlencoded",
		"DNT":1,
		"Host":"1.1.1.1",
		"Origin":"https://1.1.1.1",
		"Referer":"https://1.1.1.1/login.html",
		"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36"
	})

	q = s.post(url, data=data, verify=r"qq")
	print q.status_code

def main():
	login()

while True:
	main()
	time.sleep(50)
