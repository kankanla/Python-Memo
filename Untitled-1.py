import sqlite3

db = 'loto.db'
con = sqlite3.connect(db)
csql = con.execute('select s1,s2,s3,s4,s5,s6 from loto7 limit 5')
for cl in csql:
    for val in list(cl):
        print(str(val)+',' ,end='')
    print('\n\r')
csql.close()	
con.close()
