from selenium import webdriver
import time
import get_stock_code
import data_collecter

people = []
shares = []

#date_start = 0


def clean_str(a):
    return int(a.replace(",",""))



def scrapying_1():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver=webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
    #driver=webdriver.Chrome()
    driver.get("https://www.tdcc.com.tw/portal/zh/smWeb/qryStock")

    code = driver.find_element('xpath','/html/body/div[1]/div[1]/div/main/div[4]/form/table/tbody/tr[2]/td[2]/input')
    code.send_keys()


    date_list_str = "/html/body/div[1]/div[1]/div/main/div[4]/form/table/tbody/tr[1]/td[2]/select/option"

    for j in range(0,51) :
        date_option = driver.find_element('xpath',date_list_str + "[" + str(j+1) + "]")
        date_option.click()
        #if j == 0:
        #    date = clean_str(date_option.text)
        click1 = driver.find_element('xpath','/html/body/div[1]/div[1]/div/main/div[4]/form/table/tbody/tr[4]/td/input')
        click1.click()
        for i in range(0,15):
            temp_1 = driver.find_element('xpath',"/html/body/div[1]/div[1]/div/main/div[6]/div/table/tbody/tr["+str(i+1)+"]/td[3]")
            temp_2 = driver.find_element('xpath',"/html/body/div[1]/div[1]/div/main/div[6]/div/table/tbody/tr["+str(i+1)+"]/td[4]")
            people.insert(0,clean_str(temp_1.text))
            shares.insert(0,clean_str(temp_2.text))
        print ("S"+str(j+1))



def scrapying_2():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver=webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
    #driver=webdriver.Chrome()
    driver.get("https://www.tdcc.com.tw/portal/zh/smWeb/qryStock")

    gsc = get_stock_code.get_stock_code_data()

    
    for k in range(0,len(gsc)+1):  

        print(gsc[k])
        code = driver.find_element('xpath','/html/body/div[1]/div[1]/div/main/div[4]/form/table/tbody/tr[2]/td[2]/input')
        code.clear()
        code.send_keys(gsc[k])
        time.sleep(0.5)
        date_list_str = "/html/body/div[1]/div[1]/div/main/div[4]/form/table/tbody/tr[1]/td[2]/select/option"
        
        for j in range(0,51) :
            date_option = driver.find_element('xpath',date_list_str + "[" + str(j+1) + "]")
            date_text = date_option.text
            date_option.click()
            time.sleep(0.5)
            #if j == 0:
            #    date = clean_str(date_option.text)
            click1 = driver.find_element('xpath','/html/body/div[1]/div[1]/div/main/div[4]/form/table/tbody/tr[4]/td/input')
            click1.click()
            time.sleep(1)
            for i in range(0,15):
                temp_1 = driver.find_element('xpath',"/html/body/div[1]/div[1]/div/main/div[6]/div/table/tbody/tr["+str(i+1)+"]/td[3]").text
                temp_2 = driver.find_element('xpath',"/html/body/div[1]/div[1]/div/main/div[6]/div/table/tbody/tr["+str(i+1)+"]/td[4]").text
                data_collecter.insert_data(str(gsc[k]),date_text,i+1,temp_1,temp_2)
            print ("S"+str(j+1))
            #except:                       
             #   check = driver.find_element('xpath',"/html/body/div[1]/div[1]/div/main/div[6]/div/table/tbody/tr/td").text  
             #   print(check)
        get_stock_code.del_stock_code()
        time.sleep(5)


scrapying_2()

'''
for i in range(0,15):
    for j in range(0,10):
        print(data[i][j])
    print(" ")
'''


        
    
    







"""


for lists in list:
    for data_ in lists:
        print(data_)
"""      
