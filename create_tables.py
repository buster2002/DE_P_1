import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """Create the spartifydb database.
        1- conn : Create connection to studentdb database
        2- cur: Create Cursor object
        3- DROP the spartifydb database if it is existing
        4- create new spartifydb database with UTF8 encoding
        5- close connection with studentdb database
        6- connect with new database 'spartifydb database'
    """
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database 
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    #return cursor and connection
    return cur, conn


def drop_tables(cur, conn):
    """
    Pass two Args 'cur and conn' to drop tables in sql_queries by running drop_table_queries.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Pass two Args 'cur and conn' to create tables in sql_queries by running create_table_queries.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    drop_tables(cur, conn)
    create_tables(cur, conn)
    conn.close()

if __name__ == "__main__":
    main()