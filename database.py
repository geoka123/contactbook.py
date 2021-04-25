import sqlite3

conn = sqlite3.connect('contact.db')
c = conn.cursor()


c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='contacts' ''')

if c.fetchone()[0]==1 : 
	pass
else :
	c.execute("""CREATE TABLE contacts (
    name text,
    phone integer
    )
    """)

conn.commit()