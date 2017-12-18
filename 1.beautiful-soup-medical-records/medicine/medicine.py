import requests
import re
from bs4 import BeautifulSoup
import MySQLdb


url = "http://www.drugs.com/imprints.html"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

###pick up links from url and append in 'a'

links = soup.find_all(href=re.compile("imprints"))
a = []
for link in links:
    link1 = "http://www.drugs.com" + link.get("href")
    a.append(link1)

###for each link in 'a' pick up links contained in it and append in 'b'

b=[]
for each_link in a:
    url1 = each_link
    new_r = requests.get(url1)
    new_soup = BeautifulSoup(new_r.content,"html.parser")
    new_links = new_soup.find_all(href=re.compile("/imprints/"))
    for link in new_links:
        link2 = "http://www.drugs.com" + link.get("href")
        b.append(link2)

###now for each link in 'b', scrape data and perform an insert in table

for each_url in b:
    rr = requests.get(each_url)
    soup = BeautifulSoup(rr.content,"html.parser")

    ###extract data other than heading

    div = soup.find("div","pid-info-grid")
    dd = div.find_all("dd")
    dt = div.find_all("dt")
    c=[]
    d=[]
    for i in dd:
        c.append(i.text)
    for j in dt:
        d.append(j.text)
    
    ###extract heading

    div1 = soup.find("div","pid-info")
    ahref = div1.find_all("a","big bold")
    var = ahref[0].text

    ###take everything in variables

    def fx(d,x):
        i=0
        while i<len(d):
            if d[i]=="Generic Name:" and x=="Generic Name:":
                return i
            elif d[i]=="Imprint:" and x=="Imprint:":
                return i
            elif d[i]=="Strength:" and x=="Strength:":
                return i
            elif d[i]=="Color:" and x=="Color:":
                return i
            elif d[i]=="Shape:" and x=="Shape:":
                return i
            i+=1
        return 40


    index = fx(d,"Generic Name:")
    if index!=40:
        var0 = c[index]
    else:
        var0 = "NULL"

    index = fx(d,"Imprint:")
    if index!=40:
        var5 = c[index]
    else:
        var5 = "NULL"

    index = fx(d,"Strength:")
    if index!=40:
        var2 = c[index]
    else:
        var2 = "NULL"

    index = fx(d,"Color:")
    if index!=40:
        var3 = c[index]
    else:
        var3 = "NULL"

    index = fx(d,"Shape:")
    if index!=40:
        var4 = c[index]
    else:
        var4 = "NULL"


    ###remove spaces and line feed from imprint data

    var57 = var5.replace(" ","")
    var6 = var57.replace("\n"," ")

    ###connect to mysql and perform insert

    conn = MySQLdb.connect("127.0.0.1","Shashank","root","root1")
    cc = conn.cursor()
    cc.execute("insert into medi1 (name,salts,strength,color,shape,imprint) values (%s,%s,%s,%s,%s,%s) ",([var.encode('latin-1','replace')],[var0.encode('latin-1','replace')],[var2.encode('latin-1','replace')],[var3.encode('latin-1','replace')],[var4.encode('latin-1','replace')],[var6.encode('latin-1','replace')]))
    conn.commit()

print "Complete"
