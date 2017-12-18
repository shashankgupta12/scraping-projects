import MySQLdb

a=[]
b=[]
i=1
while i<=3270:
    email_id = "xyz" + str(i) + "@gmail.com"
    password = "abc" + str(i)
    a.append(email_id)
    b.append(password)
    i+=1


i=0
while i<3270:
    conn = MySQLdb.connect("127.0.0.1","Shashank","root","root1")
    c = conn.cursor()
    c.execute("insert into doc3 (email_id,password) values (%s,%s)",(a[i],b[i]) )
    conn.commit()
    i+=1

print "Complete"


