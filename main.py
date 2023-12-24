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

# create a new table
def create_table(table_name, table_rows):
    query = "CREATE TABLE {} {}"
    query = query.format(table_name, table_rows)
    print(query)
    dbcursor.execute(query)


# show all columns in a table
def show_rows(table):
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


show_tables()
