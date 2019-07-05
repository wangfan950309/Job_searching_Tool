# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
import yaml
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait


"""Main module."""


def parser(config):
    df = pd.DataFrame(columns=['Rank', 'Company_Name', 'Company_Website', 'Company_Type', 'Company_Location'])
    for i in config['web']:
        url = i
        driver = webdriver.Chrome('C:\webdrivers/chromedriver.exe')
        driver.execute_script('window.scrollTo(0,3000)')
        driver.get(url)
        time.sleep(2)
        source = driver.page_source
        driver.close()
        # response = requests.get(config['web'])
        # while response.status_code != 200:
        #     response = requests.get(config['web'])
        # data = response.text
        soup = BeautifulSoup(source, 'html.parser')
        container = soup.find_all('div', class_= 'kn-list-one-column kn-list-container clearfix')

        for company in container:
            company = company.find('div', class_ = 'kn-details-group-column')
            if i == config['large']:
                field = 'field_2544'
            elif i == config['medium']:
                field = 'field_2543'
            else:
                field = 'field_2542'
            rank_body = company.find('tr', class_= field)
            ranking = rank_body.td.span.h1.text
            com_name_body = company.find('tr', class_='field_1486')
            com_name = com_name_body.td.span.a.text
            com_page = com_name_body.td.span.a['href']
            com_page = '%s/%s' % (i, com_page)
            com_type_body = company.find('tr', class_='field_1722')
            com_type = com_type_body.td.span.text
            com_loc_body = company.find('tr', class_='field_1345')
            com_loc = com_loc_body.td.span.text
            df = df.append(
                {'Rank':ranking ,
                'Company_Name':com_name,
                'Company_Website': com_page,
                'Company_Type':com_type,
                'Company_Location':com_loc
                 }, ignore_index= True
            )
    return df

def main_path():
    path = os.getcwd()
    path = os.path.abspath(os.path.join(path, '..'))
    return path
def get_config():
    path = os.getcwd()
    path = os.path.abspath(os.path.join(path, '..'))
    with open('%s/config/config.yaml' % path, 'r') as file:
        config = yaml.load(file)
    return config

if __name__ == '__main__':
    path = os.getcwd()
    path = os.path.abspath(os.path.join(path, '..'))
    df = parser(get_config())
#    os.makedirs('%s/data' % path)
    df.to_csv('%s/data/ranking_list.csv' % path, index = False )
