# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 18:46:08 2021

@author: WB
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import os
import wget

## Can use pandas instead:
file =  open('ztargets_107','r')
protein_id_lst = []
#count = 0
# 檢查ID數並對齊內容
for line in file:
    text = line.strip().split('  ')
    if '' in text:
       text.remove('')
    if len(text)>1:
        protein_id_lst += text
        #count += len(text) ##雙重對照檢查
        #if len(text)!=10:##找出未對齊
        #    print(text)
file.close()
#print(count)
#print(len(protein_id_lst))
#print(protein_id_lst)
protein_id_lst = [s.replace(' ','') for s in protein_id_lst]
#print(protein_id_lst)

# time to sleep
sleep_t = 5 #測試時瀏覽器開啟時間
# To avoid DeprecationWarning, use Service
PATH = 'C:/Users/WB/Desktop/chromedriver_win32/chromedriver.exe'
s = Service(PATH)
#driver = webdriver.Chrome(service=s)
#driver.get('https://www.rcsb.org/downloads')

# 建立資料夾
path = os.path.join('pdb_data')
#os.mkdir(path)



for p_id in protein_id_lst:
    #print(p_id)
    driver = webdriver.Chrome(service=s)
    driver.get('https://www.rcsb.org/downloads')


    # 找到網頁搜尋相關物件
    search_protien_id = driver.find_element(By.ID,'downloadsIdList')
    search_data_file_format = driver.find_element(By.XPATH,'//*[@id="coordinatesOptions"]')
    generate_download = driver.find_element(By.XPATH,'//*[@id="download-table"]/div[3]/div[1]/button')

    # 自動化搜尋
    search_protien_id.send_keys(p_id)
    action = ActionChains(driver)
    action.move_to_element(search_data_file_format)
    action.click()
    action.perform()
    action.move_to_element(generate_download)
    action.click()
    action.perform()

    # 等候搜尋結果並建立下載連結物件
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="downloadsContainer"]/div[2]/div/div[2]/div/div/div[2]/table/tr[2]/td/div[1]/a/h4')))
    batch_download = driver.find_element(By.PARTIAL_LINK_TEXT,'Batch')
    #driver.find_element(By.XPATH,'//*[@id="downloadsContainer"]/div[2]/div/div[2]/div/div/div[2]/table/tr[2]/td/div[1]/a/h4')

    save_as = os.path.join(path, p_id+'.zip')
    #print(batch_download.get_attribute('href'))
    wget.download(batch_download.get_attribute("href"), save_as)
    #time.sleep(sleep_t)
    driver.quit()
    #time.sleep(60)

