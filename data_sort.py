import sqlite3
"""
def sort_data(stock):
    data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    
    i = 0
    for P in pre_data:
        i += 1
        data[i%15].append(P)
    return data
"""
def clean_str(a):
    return int(str(a).replace(",",""))

def find_data_people(stock):
    data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT * FROM data WHERE stock = '" + str(stock) + "'")
    j = 0
    for i in cur.fetchall():
        if j%15 != 0:
            data[j%15].append(clean_str(i[3]))
            j += 1
        else: 
            data[j%15].append(0)
            j += 1
    con.commit()
    con.close()
    print("done")
    return data

def find_data_share(stock):
    data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT * FROM data WHERE stock = '" + str(stock) + "'")
    j = 0
    for i in cur.fetchall():
        data[j%15].append(clean_str(i[4])) 
        j += 1
    con.commit()
    con.close()
    print("done")
    return data
    
    

