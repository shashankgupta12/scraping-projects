import MySQLdb

b=[]
i=1
while i<=1117:
    password = "abc" + str(i)
    b.append(password)
    i+=1


i=0
while i<1117:
    conn = MySQLdb.connect("127.0.0.1","Shashank","root","root1")
    c = conn.cursor()
    c.execute("insert into diag2 (password) values (%s)",[b[i]])
    conn.commit()
    i+=1

print "Complete"


