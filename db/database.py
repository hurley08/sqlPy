# db.py

import sqlite3

conn = sqlite3.connect("legos.db")



def connect_cursor():
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
    c.execute("""CREATE TABLE pieces (
            studded binary,
            units   integer,
            name    text,
            description text,
            price   real,
            color   text
    )""")




def commit_and_close():
    # Commit canges to db
    conn.commit()
    # Close db connection
    conn.close()


if __name__=='__main__':
    c = connect_cursor()
    g = c.fetchall()
    print(g)