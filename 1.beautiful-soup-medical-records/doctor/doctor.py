import requests
from bs4 import BeautifulSoup
import MySQLdb

url = "https://www.******.com/delhi/doctors?"
a=[]
a.append(url)
j=2
while j<1784:
    append_url = url + "page=" + str(j)
    a.append(append_url)
    j+=1

for each_url in a:
    r = requests.get(each_url)
    soup = BeautifulSoup(r.content,"html.parser")

    div_listing = soup.find_all("div","listing-row")

    def fx(value):
        if value==None:
            return "NULL"
        else:
            var = value.text
            var = var.replace('\n',' ')
            var = var.strip()
            return var

    for each in div_listing:
        doc_details = each.find("div","doc-details-block")
        temp = doc_details.find("h2",{"itemprop":"name"})
        name = fx(temp)
        temp = doc_details.find("p","doc-qualifications")
        qualifications = fx(temp)
        temp = doc_details.find("p","doc-exp-years")
        experience = fx(temp)
        temp = doc_details.find("span",{"itemprop":"medicalSpecialty"})
        speciality = fx(temp)
        temp = doc_details.find("span",{"itemprop":"name"})
        clinic = fx(temp)
        
        doc_availability = each.find("div","doc-availability-block")
        temp = doc_availability.find("span",{"itemprop":"addressLocality"})
        locality = fx(temp)
        temp = doc_availability.find("span",{"itemprop":"addressRegion"})
        city = fx(temp)
        temp = doc_availability.find("span","fees-amount")
        fees = fx(temp)
        temp = doc_availability.find("span","strong")
        days = fx(temp)
        temp = doc_availability.find("span","hours-timing")
        timing = fx(temp)
        print name," ",qualifications," ",experience," ",speciality," ",clinic," ",locality," ",city," ",fees," ",days," ",timing

        conn = MySQLdb.connect("127.0.0.1","Shashank","root","root1")
        cc = conn.cursor()
        cc.execute("insert into doc1 (name,hospital) values (%s,%s) ",([name.encode('latin-1','replace')],[clinic.encode('latin-1','replace')]))
        cc.execute("insert into doc2 (qualification,specialization,locality,city,fees,timings,no_of_days) values (%s,%s,%s,%s,%s,%s,%s) ",([qualifications.encode('latin-1','replace')],[speciality.encode('latin-1','replace')],[locality.encode('latin-1','replace')],[city.encode('latin-1','replace')],[fees.encode('latin-1','replace')],[timing.encode('latin-1','replace')],[days.encode('latin-1','replace')]))
        conn.commit()


print "Complete"
