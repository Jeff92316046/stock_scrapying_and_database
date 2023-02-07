import sqlite3
import copy 
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
    cur.execute("SELECT DISTINCT * FROM data WHERE stock = '" + str(stock) + "' ORDER BY date ASC")
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
    
    return data

def find_data_share(stock):
    data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT * FROM data WHERE stock = '" + str(stock) + "' ORDER BY date ASC")
    k = 0
    for i in cur.fetchall():
        data[k%15].append(clean_str(i[4])) 
        k += 1
      
    data[15] = copy.deepcopy(data[0])
    
    for i in range(1,len(data)-1):
        for j in range(len(data[i])):
            data[15][j] += data[i][j]
    
    for i in range(len(data[0])):
        for j in range(len(data)-1):
            data[j][i] = data[j][i] / data[15][i]
    data.pop()
    
    

    con.commit()
    con.close()
    
    return data
    
    

