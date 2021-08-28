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
    cur.execute("DELETE from mobile where id = 3") 
    connection.commit() 
    count = cur.rowcount 
    print(count, "Record deleted successfully from mobile table")

except (Exception, psycopg2.Error) as error: 
        print("Failed connect", error) 
finally:
# closing database connection. 
    if connection: connection.close() 
print("PostgreSQL connection is closed")