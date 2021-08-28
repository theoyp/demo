import psycopg2

try: 
    print('Connecting to the PostgreSQL database...') 
    connection = psycopg2.connect(user="postgres", 
                                password="admin", 
                                host="127.0.0.1", 
                                port="5432",
                                database="bigdatacilsy")
    cur = connection.cursor() 
    # execute a statement 
    cur.execute ("ALTER TABLE mobile ADD COLUMN qty int")
    connection.commit()
    # cur.execute("INSERT INTO mobile (id, name, price) VALUES (4, 'iPhone', 1150)") 
    # connection.commit() 
    # count = cur.rowcount 
    # print(count, "Record inserted successfully into mobile table")
    # cur.execute("""CREATE TABLE mobile (id SERIAL PRIMARY KEY, 
    # name VARCHAR(255) NOT NULL, price int NOT NULL )""")
    # connection.commit()
    # print("Table created!")
    # print('PostgreSQL database version:') 
    # cur.execute('SELECT version()') 
    # db_version = cur.fetchone() 
    # print(db_version)

except (Exception, psycopg2.Error) as error: 
        print("Failed connect", error) 
finally:
# closing database connection. 
    if connection: connection.close() 
print("PostgreSQL connection is closed")