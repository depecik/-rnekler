import sqlite3 as sql
db = sql.connect(r"d:\İbrahim EDİZ\23022019\Örnekler\IEDB.db")
cursor = db.cursor()
cursor.execute("""select * from v_hesap""")
liste = cursor.fetchall()
for a,b,c,d in liste:
    print("{}- {}  {}  {}".format(a,b,c,d))

