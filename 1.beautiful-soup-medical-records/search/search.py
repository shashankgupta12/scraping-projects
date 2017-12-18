#For the generation of array in typeahead search algorithm
#i have created a table named search with three fields viz. primary kry,
#name of centre and type of centre
#Then this table has been populated with values using "insert using select" and 
#update table command!

#Further generate a list having all the names from the search table
#as well as the city from city table and write the list to a file
#similarly generate a list of lists having each item as [id,name,type]

import MySQLdb
import sys

conn = MySQLdb.connect("127.0.0.1","Shashank","root","root1")
c = conn.cursor()
c.execute("Select * from search");
entries = c.fetchall()
c.execute("Select * from city");
entries1 = c.fetchall()
conn.commit()

a=[]
b=[]
c=[]
d=[]
data=[]
for _id,_name,_type in entries:
    d=[]
    d.append(_id)
    b.append(_name)
    d.append(_name)
    d.append(_type)
    data.append(d)

i=0
while i<len(entries1):
    city = entries1[i][0]
    b.append(city)
    i+=1

orig_stdout = sys.stdout
f = file('out.txt','w')
sys.stdout = f

print b

sys.stdout = orig_stdout
f.close()

orig_stdout = sys.stdout
f1 = file('out1.txt','w')
sys.stdout = f1

print data

sys.stdout = orig_stdout
f.close()