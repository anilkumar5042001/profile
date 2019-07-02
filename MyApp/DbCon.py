import MySQL.db
conn=MySQL.db.connect("mysql.server","anil5042001","admin123","anil5042001$SubmitProfile")
c=conn.cursor()
c.execute('select * from Country')
rows=c.fetchall()
for eachrow in rows:
    print eachrow