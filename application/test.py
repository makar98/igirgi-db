import pymysql

con = pymysql.connect('localhost', 'a_makeev',
                      'Cgfhnfr18011998', 'igirgi')

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))