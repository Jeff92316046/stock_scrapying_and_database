import sqlite3

# 連線到資料庫檔案


def create_table():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE data (stock text , date text , number integer , people integer , share integer )")
    con.commit()
    con.close()

def insert_data(stock ,date ,number ,people ,share):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("INSERT INTO data VALUES (" + "'" + str(stock) + "'," 
                                            + "'" + str(date) + "',"
                                            + "'" + str(number) + "',"
                                            + "'"  + str(people) + "',"
                                            + "'"  + str(share) + "'" + ")"
                )

    con.commit()
    con.close()



