import sqlite3

conn = sqlite3.connect('places.db')

c =conn.cursor()



def find_place(place):
    c.execute("SELECT* FROM places WHERE place=:place", {'place': place})
    return c.fetchone()


funka = find_place('dag')
print(funka)

# c.execute("""CREATE TABLE places (
#             place text
#             )""")
# c.execute("INSERT INTO places VALUES ('ica')")

# c.execute("SELECT* FROM places WHERE place='coop'")
# print(c.fetchall())
conn.commit()

conn.close()
