import requests
from bs4 import BeautifulSoup
import MySQLdb

temp_url = "http://y*********s.s*****a.com/pharmacies_delhi_"
j=1
a=[]
while j<192:
    url = temp_url + str(j)
    a.append(url)
    j+=1

b=[]
for each_link in a:
    r = requests.get(each_link)
    soup = BeautifulSoup(r.content,"html.parser")
    links = soup.find_all("a","YPTRACK GAQ_C_BUSL")
    for link in links:
        u1 = link.get("href")
        url1 = "http://yellowpages.sulekha.com" + u1
        b.append(url1)

for url in b:
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")

    def fx(value):
        if value==None:
            return "NULL"
        else:
            value = value.text
            value = value.strip()
            value = value.replace("\n","")
            return value

    soup = BeautifulSoup(r.content,"html.parser")
    ul = soup.find("ul","ul-horizontal")
    temp = ul.find("em",{"itemprop":"telephone"})
    telno = fx(temp)
    temp = ul.find("span",{"itemprop":"streetAddress"})
    street = fx(temp)
    temp = ul.find("span",{"itemprop":"addressLocality"})
    locality = fx(temp)
    temp = ul.find("span",{"itemprop":"addressRegion"})
    region = fx(temp)
    temp = ul.find("span",{"itemprop":"postalCode"})
    postalcode = fx(temp)
    temp = soup.find("span",{"itemprop":"name"})
    name = fx(temp)
    
    print name," ",telno," ",street," ",locality," ",region," ",postalcode

    conn = MySQLdb.connect("127.0.0.1","Shashank","root","root1")
    c = conn.cursor()
    c.execute("insert into medi1 (name,telno,street,locality,region,postalcode) values (%s,%s,%s,%s,%s,%s)",([name.encode('latin-1','replace')],[telno.encode('latin-1','replace')],[street.encode('latin-1','replace')],[locality.encode('latin-1','replace')],[region.encode('latin-1','replace')],[postalcode.encode('latin-1','replace')]))
    conn.commit()

print "Complete"
