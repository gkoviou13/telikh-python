import urllib2
import json
import datetime
r = []
def success(epp,tmpp):
	sum=0
	sum2=0
	for item in epp:
		for item_2 in tmpp:
			if item==item_2:
				sum+=1
	if sum>4:
		sum2+=1
	return sum2
ep = []
cur_date=datetime.datetime.now()
cur_date2=datetime.datetime.now()
x=raw_input("Give 10 numbers like 1,2,3,4,5,6,7,8,9,10: ")
ep = x.split(",")
for i in range (len(ep)):
	ep[i] = int(ep[i])
for i in range(31):
	cur_date= cur_date - datetime.timedelta(days=1)
	date_str= cur_date.strftime("%d-%m-%Y")
	url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	data = response.read()
	data=json.loads(data)
	klhrwseis= data['draws']['draw']
	sum3=0
	for k in klhrwseis:
		tmp=k["results"]
		sum3+= success(ep,tmp)
	r.append(sum3)
y=max(r)
theseis = []
for i in range (len(r)):
	if r[i] == y:
		theseis.append(i)
telhm = cur_date2 - datetime.timedelta(days=1)
for i in range (len(theseis)):
	print "The date with the most chances is:"
	kati = telhm - datetime.timedelta(days=theseis[i])
	print kati.strftime('%d-%m-%Y')


