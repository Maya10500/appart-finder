import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except :
        print("fail while connecting")

    return None

def insert_item(conn, item):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM PLAYER WHERE (id=?)', (id,))
    entry = cursor.fetchone()

    if entry is None:
        #print("entry is None !")
        cursor.execute("""INSERT INTO PLAYER(name, Id, clan) 
                       VALUES (?,?,?);""", (name, id, clan))
        conn.commit()
        #print("closed DB")

def creat_table(conn):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS item (
                                            id integer PRIMARY KEY,
                                            item_type text,
                                            summary text NOT NULL,
                                            description text,
                                            price integer
                                        ); """
    try:
        c = conn.cursor()
        c.execute(sql_create_projects_table)
    except Error as e:
        print(e)

def insert_if_not_exist(conn, item,type):
    print(item.ID)
    print(item.sujet)
    print(item.prix)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ITEM WHERE (id=?)', (item.ID,))
    entry = cursor.fetchone()

    if entry is None:
        # print("entry is None !")
        cursor.execute("""INSERT INTO ITEM(id, item_type, summary, description,price) 
                           VALUES (?,?,?,?, ?);""", (item.ID, type, item.sujet, item.definition, item.prix))
        conn.commit()
        # print("closed DB")

def get_item(conn, item):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM PLAYER WHERE (id=?)', (id,))
    entry = cursor.fetchone()

    if entry is None:
        #print("entry is None !")
        cursor.execute("""INSERT INTO PLAYER(name, Id, clan) 
                       VALUES (?,?,?);""", (name, id, clan))
        conn.commit()
        #print("closed DB")