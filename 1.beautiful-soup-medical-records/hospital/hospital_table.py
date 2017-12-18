from bs4 import BeautifulSoup
import requests
import MySQLdb

url = "http://www.h*******nlink.com/hospitals-india/hospitals-west-bengal.htm"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

div = soup.find("div")
table = div.find("table",{"id":"AutoNumber1"})
##tbody = table.find("tbody")
tr = table.find_all("tr")
table_1 = tr[1].find("table")
tr_1 = table_1.find_all("tr")
links=[]
for each_tr in tr_1:
    td = each_tr.find_all("td")
    for each_td in td:
        a = each_td.find("a")
        if a==None:
            continue
        else:
            link = a.get("href")
            links.append(link)

i=0
for each_link in links:
    link1 = "http://www.hindustanlink.com/hospitals-india/"
    links[i] = link1 + each_link
    i+=1

links.append("http://www.hindustanlink.com/hospitals-india/hospitals-west-bengal.htm")
i=0

def func(value):
    value = value.replace("\n"," ")
    value = value.replace("\t"," ")
    value = value.strip()
    value = value.encode('latin-1','replace')
    return value

for link in links:
    if i==0:
        i+=1
        continue
    else:
        r = requests.get(link)
        soup = BeautifulSoup(r.content,"html.parser")
        div = soup.find("div")
        table = div.find("table",{"id":"AutoNumber1"})
        tr = table.find_all("tr")
        td = tr[9].find("td")
        table_2 = td.find("table")
        trs = table_2.find_all("tr")
        j=0
        for each_tr in trs:
            if j<2:
                j+=1
                continue
            else:
                tds = each_tr.find_all("td")
                td1 = func(tds[1].text)
                td2 = func(tds[2].text)
                td3 = func(tds[3].text)
                td4 = func(tds[4].text)
                conn = MySQLdb.connect("127.0.0.1","Shashank","root","root1")
                cc = conn.cursor()
                cc.execute("insert into hospital (name,city,address,contact) values (%s,%s,%s,%s)",([td1],[td2],[td3],[td4]))
                conn.commit()
        
print "Complete"
