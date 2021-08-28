import psycopg2

def updatedata (id,price):
    try: 
        print('Connecting to the PostgreSQL database...') 
        connection = psycopg2.connect(user="postgres", 
                                    password="admin", 
                                    host="127.0.0.1", 
                                    port="5432",
                                    database="bigdatacilsy")
        cur = connection.cursor() 
        # execute a statement 
        print("Table Before updating record ") 
        sql_select_query = "select * from mobile where id = %s" 
        cur.execute(sql_select_query, id) 
        record = cur.fetchone() 
        print(record) 

        # Update single record now 
        sql_update_query = "Update mobile set price = %s where id = %s" 
        cur.execute(sql_update_query, (price, id)) 
        connection.commit() 
        count = cur.rowcount 
        print(count, "Record Updated successfully ") 

        print("Table After updating record ") 
        sql_select_query = "select * from mobile where id = %s" 
        cur.execute(sql_select_query, (id)) 
        record = cur.fetchone() 
        print(record)

    except (Exception, psycopg2.Error) as error: 
        print("Failed connect", error) 
    finally:
    # closing database connection. 
        if connection: connection.close() 
        print("PostgreSQL connection is closed")

updatedata ("1",1000)