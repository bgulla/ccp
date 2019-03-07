import sqlite3
from datetime import datetime



DATABASE_NAME = "prod.db"

def create_db():

    """
    Creates the database if needed
    :return:
    """


    sql_create_cuss_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        last_date text

                                    ); """
    # create a database connection
    conn = sqlite3.connect(DATABASE_NAME)
    if conn is not None:
        # create tasks table
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS projects
                          (id integer PRIMARY KEY, date text) """)
        conn.commit()

        conn.close()


    else:
        print("Error! cannot create the database connection.")
    return conn

def insert_new_record():
    conn = sqlite3.connect(DATABASE_NAME)
    if conn is not None:
        # create tasks table
        cursor = conn.cursor()
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO projects (date) VALUES ('%s')" % date_time)
        conn.commit()
        conn.close()

def get_count():
    """
    Retuns the count of curses in the database
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    if conn is not None:
        query = "select * from projects"
        cursor= conn.cursor()
        cursor.execute(query)
        size = len(cursor.fetchall())
        conn.close()
        return size

def get_last_record():
    """
    Retuns the count of curses in the database
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    if conn is not None:
        query = "select * from projects ORDER BY id ASC"
        cursor= conn.cursor()
        cursor.execute(query)
        results = (cursor.fetchall())
        if results is None or len(results) < 1:
            return "null"
        date_time = results[-1][1]
        conn.close()
        return date_time

create_db()
