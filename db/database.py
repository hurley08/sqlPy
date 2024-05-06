# db.py

import sqlite3





def connect_cursor():
    conn = sqlite3.connect("legos.db")
    c = conn.cursor()
    return c

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
g



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

    c.execute("""CREATE TABLE gears (
            style     char,
            units_diam  real,
            num_teeth   integer,
            shaft_type  char,
            description char,
            price       real,
            color       char
    )""")




def commit_and_close():
    # Commit canges to db
    conn.commit()
    # Close db connection
    conn.close()


if __name__=='__main__':
    c = connect_cursor()
    g = c.fetchall()
    create_table()
    commit_and_close()
    print(g)
