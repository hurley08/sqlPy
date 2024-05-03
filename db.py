# db.py

import sqlite3

conn = sqlite3.connect("legos.db")


def insert_new_piece(
        'studded'=False, 
        'units'=5, 
        'name'="5 studless beam",
        'description'=None, 
        'price'=0, 
        'color'="black"):
    c.execute(f"""INSERT INTO piece VALUES({studded}, 
                                            {units}, 
                                            {name},  
                                            {description}, 
                                            {price}, 
                                            {color})""")

c = conn.cursor()

c.execute("""CREATE TABLE pieces (
        studded binary,
        units   integer,
        name    text,
        description text,
        price   real,
        color   text
)""")


# Commit canges to db
conn.commit()



# Close db connection
conn.close()

