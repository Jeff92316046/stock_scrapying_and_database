import sqlite3

# 連線到資料庫檔案


def create_table():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE data (stock text , date text , number integer , people integer , share integer )")
    con.commit()
    con.close()

def del_stock_code(stock):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("DELETE FROM data WHERE stock = '" + stock + "'" )
    con.commit()
    con.close()
    
def insert_data(stock ,date ,number ,people ,share):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("INSERT INTO data VALUES (" + "'" + str(stock) + "'," 
                                            + "'" + str(date) + "',"
                                            + "'" + str(number) + "',"
                                            + "'"  + str(people) + "',"
                                            + "'"  + str(share) + "'" ")"
                )

    con.commit()
    con.close()

"""
def numbering_data():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM data")
    temp = cur.fetchall()
    for i in range(0,len(temp)) :
        if len(temp[i][0]) != 4:
            print(temp[i][0])
            del_stock_code(temp[i][0])
    con.commit()
    con.close()
"""
