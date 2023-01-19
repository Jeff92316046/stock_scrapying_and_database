from selenium import webdriver
import sqlite3



def create_table():
    con = sqlite3.connect('stock_code_list.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE data (stock text)")
    con.commit()
    con.close()

def insert_data(stock):
    con = sqlite3.connect('stock_code_list.db')
    cur = con.cursor()

    cur.execute("INSERT INTO data VALUES (" + "'" + str(stock) + "')")

    con.commit()
    con.close()

def get_stock_code_data():
    stock_code_list = []
    con = sqlite3.connect('stock_code_list.db')
    cur = con.cursor()

    cur.execute("select * from data")
    for row in cur:
        stock_code_list.append(row[0])
    con.commit()
    con.close()
    return stock_code_list

def del_stock_code(k):
    con = sqlite3.connect('stock_code_list.db')
    cur = con.cursor()

    cur.execute("DELETE FROM data WHERE stock = "+ str(k))
    con.commit()
    con.close()
def scrapying():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver=webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
    #driver=webdriver.Chrome()
    driver.get("https://www.tdcc.com.tw/portal/zh/smWeb/psi")

    button = driver.find_element('xpath','/html/body/div[1]/div[1]/div/main/div[4]/form/table/tbody/tr[6]/td/input')
    button.click()


    date_list_str = driver.find_element('xpath',"/html/body/div[1]/div[1]/div/main/div[6]/div/table/tbody")    #"tr[1""]"

    
    stock_code = date_list_str.find_elements('xpath',"./*")

    for i in stock_code:
        insert_data(i.find_element('xpath',"./td[1]").text)

        
#scrapying()

'''
for i in stock_code:
    print(i)
'''