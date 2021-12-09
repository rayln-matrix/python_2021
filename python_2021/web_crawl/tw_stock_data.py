# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:01:17 2021

@author: WB
"""


import requests as r
from lxml import etree
import json
from datetime import datetime, date
import pandas as pd
import yfinance as yf


### twse_stock_info() is from:
# https://nbviewer.org/github/histockhero/youtube_code/blob/main/Part2_%E8%82%A1%E5%B8%82%E8%B3%87%E6%96%99%E4%B8%8B%E8%BC%89%EF%BC%86%E6%8A%80%E8%A1%93%E5%88%86%E6%9E%90/2.1%E8%82%A1%E5%B8%82%E8%B3%87%E6%96%99%E4%B8%8B%E8%BC%89/%E4%B8%80%E5%8F%A3%E6%B0%A3%E4%B8%8B%E8%BC%89%E5%A4%9A%E6%94%AF%E4%B8%8A%E5%B8%82%E5%8F%B0%E8%82%A1%E5%80%8B%E8%82%A1%E6%AD%B7%E5%8F%B2%E8%B3%87%E6%96%99.ipynb

def twse_stock_info():
    # 下載代碼
    url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
    res = r.get(url)
    root = etree.HTML(res.text)
    data = root.xpath('//tr')[1:]
    
    df = pd.DataFrame(columns = ["上市有價證券種類", "有價證券代號代碼", "有價證券代號名稱", "國際證券辨識號碼(ISIN Code", "上市日", "市場別", "產業別", "CFICode", "備註"])
    
    # read data
    category = ''
    row_num = 0
    for row in data:
        row = list(map(lambda x: x.text, row.iter()))[1:]
        if len(row) == 3:
            category = row[1].strip(' ')
        else:
            stock_code, stock_name = row[0].split('\u3000')
            data_row = [category, stock_code, stock_name, row[1], row[2], row[3], row[4], row[5], row[6]]
            df.loc[row_num] = data_row
            row_num += 1
    
    return df

#url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=2'
#res = r.get(url)
#print(res)
#root = etree.HTML(res.text)
#print(root)
#data = root.xpath('//tr')[1:]
#for row in data:
#        row = list(map(lambda x: x.text, row.iter()))[1:]
#        print(row)
#print(data)
stock_info_all_df = twse_stock_info()
stock_code_df = stock_info_all_df.loc[stock_info_all_df['上市有價證券種類']  == '股票']#['有價證券代號代碼','有價證券代號名稱','國際證券辨識號碼(ISIN Code','上市日','市場別']
select_columns = stock_code_df.columns.tolist()[1:-1]
#print(select_columns)
#print(stock_code_df[select_columns])
stock_code_data_df = stock_code_df[select_columns]
stock_code_for_yahoo = [name + '.TW' for name in stock_code_data_df['有價證券代號代碼']]
#print(stock_code_for_yahoo)

yahoo_df = pd.DataFrame()
error_code = []
for yf_stock_code in stock_code_for_yahoo:
    try:
        yf_stock_df = yf.download(yf_stock_code, "2000-01-01", "2021-11-30")
        yf_stock_df.insert(0, 'stock_code', yf_stock_code)
        yahoo_df = yahoo_df.append(yf_stock_df, ignore_index = True)
    except TypeError:
        error_code.append(yf_stock_code)
        continue
print(yahoo_df)
#test_df = yf.download('4148.TW', "2000-01-01", "2021-11-30")
#print(test_df)
yahoo_df.to_csv('tw_stock_data_csv_2021.csv', index = False, encoding = 'utf-8')
stock_code_df.to_csv('tw_stock_code_2021.csv', index = False, encoding = 'utf_8_sig')
print(stock_code_df.head())
print(len(error_code)) ## 沒抓到的

for code in stock_code_for_yahoo:
    print(code[:-3])