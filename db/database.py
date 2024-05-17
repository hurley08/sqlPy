# db.py

import sqlite3





def connect_cursor():
    conn = sqlite3.connect("legos.db")
    c = conn.cursor()
    return c, conn


def print_all(cur):
    for row in cur.execute('SELECT * FROM beams;'):
        print(row)
    for row in cur.execute('SELECT * FROM bricks;'):
        print(row)
    for row in cur.execute('SELECT * FROM pins_conns_axle;'):
        print(row)

def insert_new_piece(
        studded=False, 
        units=5, 
        name="5 studless beam",
        description=None, 
        price=0, 
        color="black"):
    c.execute(f"""INSERT INTO piece VALUES('{studded}', 
                                            '{units}', 
                                            '{name}',  
                                            '{description}', 
                                            '{price}', 
                                            '{color}')""")

def create_table():
    try:    
        c.execute("""CREATE TABLE beams (
                studded     binary,
                units_len   integer,
                units_height integer,
                units_width real,
                name        text,
                angle       integer,
                description text,
                price       real,
                color       char
        )""")
    except:
        print("beams already exists")

    try:
        c.execute("""CREATE TABLE bricks (
                technic    binary,
                units_len   integer,
                units_height integer,
                units_width real,
                name        text,
                description text,
                price       real,
                color       char
        )""")
    except:
        print("bricks already exists")

    try:
        c.execute("""CREATE TABLE pins_conns_axle (
                type     char,
                units_len   integer,
                friction    binary,
                connection  char,
                adapter     binary,
                description char,
                price       real,
                color       char
        )""")
    except:
        print("pins_conns_axle already exists")

    try:
        c.execute("""CREATE TABLE gears (
                style     char,
                units_diam  real,
                num_teeth   integer,
                shaft_type  char,
                description char,
                price       real,
                color       char
        )""")
    except:
            print("gears already exists")



def commit_and_close(conn):
    # Commit canges to db
    conn.commit()
    # Close db connection
    conn.close()


if __name__=='__main__':
    c, conn = connect_cursor()
    g = c.fetchall()
    #create_table()
    print_all(c)
    commit_and_close(conn)
    print(g)
