import MySQLdb

18046
3820
i=1
while i<=3820:
    j=1
    while j<=18046:
        conn = MySQLdb.connect("127.0.0.1","Shashank","root","root1")
        c = conn.cursor()
        c.execute("insert into medi2 (store_id,med_id) values (%s,%s)",(i,j))
        conn.commit()
        j+=1
    i+=1

print "Complete"
