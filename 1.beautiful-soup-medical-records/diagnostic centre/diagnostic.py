from bs4 import BeautifulSoup
import requests
import re
import MySQLdb

temp_url = "http://y*********s.s*****a.com/diagnostic-centers_delhi_"
b=[]
j=1
while j<57:
    url = temp_url + str(j)
    b.append(url)
    j+=1

a=[]
for new_url in b:
    r = requests.get(new_url)
    soup = BeautifulSoup(r.content,"html.parser")
    links = soup.find_all("a",{"class":"YPTRACK GAQ_C_BUSL"})
    for url1 in links:
        url2 = "http://yellowpages.sulekha.com" + url1.get("href")
        a.append(url2)

for each_url in a:
    r = requests.get(each_url)
    soup = BeautifulSoup(r.content,"html.parser")

    def fx(temp):
        if temp==None:
            return "NULL"
        else:
            temp = temp.text
            temp = temp.strip()
            temp = temp.replace("\n"," ")
            return temp

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
    temp = ul.find("span",{"itemprop":"email"})
    email = fx(temp)
    temp = ul.find("a","weblink YPTRACK GAQ_C_TOPWEBSITE")
    website = fx(temp)
    temp = ul.find("time",{"itemprop":"openingHours"})
    timings = fx(temp)
    temp = soup.find("span",{"itemprop":"name"})
    name = fx(temp)

    conn = MySQLdb.connect("127.0.0.1","Shashank","root","root1")
    c = conn.cursor()
    c.execute("insert into diag1 (name,street,locality,region,postalcode,timings,telno,emailid,website) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",([name.encode('latin-1','replace')],[street.encode('latin-1','replace')],[locality.encode('latin-1','replace')],[region.encode('latin-1','replace')],[postalcode.encode('latin-1','replace')],[timings.encode('latin-1','replace')],[telno.encode('latin-1','replace')],[email.encode('latin-1','replace')],[website.encode('latin-1','replace')]))
    conn.commit()

print "Complete"

    
