import mysql.connector

testdb = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    passwd='LmA7ZTyx120!#',
    database='pydungeon'
)

dbcursor = testdb.cursor()

dbcursor.execute("SHOW TABLES")

for table in dbcursor:
    print(table)
