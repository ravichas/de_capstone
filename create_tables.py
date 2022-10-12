# load libraries 
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

# create a function for creating the database
def create_database():
    """
    - Creates and connects to the sparkifydb
    @return: cursor and connection to sparkifydb
    """
    try: 
        conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student") 
    except psycopg2.Error as e: 
        print("Error: Could not make connection to the Postgres database")
        print(e)
    
    # use the connect to get a cursor that we will use to execute queries
    
    try: 
        cur = conn.cursor() 
    except psycopg2.Error as e: 
        print("Error: Could not get curser to the Database")
        print(e)
    
    conn.set_session(autocommit=True)
    
    # connect to default database
    # conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    # conn.set_session(autocommit=True)
    # cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    try: 
        cur.execute("DROP DATABASE IF EXISTS sparkifydb")
        cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    except psycopg2.Error as e:
        print(e)

    # close connection to default database
    try: 
        conn.close()
    except psycopg2.Error as e: 
        print(e)
    
    # connect to sparkify database
    try: 
        conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    except psycopg2.Error as e: 
        print("Error: Could not make connection to the Postgres database")
        print(e)
        
    try: 
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("Error: Could not get curser to the DB")
        print(e)
    
    conn.set_session(autocommit=True)
    
    return cur, conn

def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    @param cur:
    @param conn:
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    """
    This function will create each table using the queries in `create_table_queries` list.
    @param cur:
    @param conn:
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    - Drop DB, if exists, and Create the Sparkify DB 
    - Establish connection with the Sparkify DB and get a cursor
    - Drop all the tables  
    - Create all tables, if needed 
    - Finally, close the connection
    
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.close()

# default 
if __name__ == "__main__":
    main()
