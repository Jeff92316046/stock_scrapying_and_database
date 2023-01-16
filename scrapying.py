from selenium import webdriver
import time


people = []
shares = []
#date_start = 0


def clean_str(a):
    return int(a.replace(",",""))



def scrapying(Stock_code):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    driver=webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
    #driver=webdriver.Chrome()
    driver.get("https://www.tdcc.com.tw/portal/zh/smWeb/qryStock")

    code = driver.find_element('xpath','/html/body/div[1]/div[1]/div/main/div[4]/form/table/tbody/tr[2]/td[2]/input')
    code.send_keys(Stock_code)


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
