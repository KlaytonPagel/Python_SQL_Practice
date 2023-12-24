import mysql.connector

testdb = mysql.connector.connect(
    host="127.0.0.1",
    user='root',
    passwd='LmA7ZTyx120!#',
    database='pydungeon'
)

dbcursor = testdb.cursor()


# show tables in the database
def show_tables():
    dbcursor.execute("SHOW TABLES")

    for table in dbcursor:
        print(table)


# show all columns in a table
def show_columns(table):
    query = "SELECT * FROM {}"
    query = query.format(table)
    dbcursor.execute(query)

    for column in dbcursor:
        print(column)

# Adds rows to your database
def add_rows(table, values):
    query = "INSERT INTO {} (username, password) VALUES (%s, %s)"
    query = query.format(table)
    dbcursor.execute(query, values)

    testdb.commit()


show_columns('login_credentials')
