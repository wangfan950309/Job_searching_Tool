import pandas as pd
import math
import numpy as np
from web_scraping.scraping import *

def search_algorithm(keywords):
    search_key = keywords
    keys = search_key.split()
    key_dic = dict()
    df = pd.read_csv("%s/data/Job_search.csv" % main_path(), index_col=None)
    search_field = df['Job_Name'].tolist()
    for key in keys:
        idf_counter = 0
        for field in search_field:
            if key in field:
                idf_counter += 1
        key_dic[key] = math.log(len(df.index)/1+idf_counter)
    df['TF-IDF'] = 0
    for key in keys:
        tf = []
        for field in search_field:
            counter = 0
            job = field.split()
            for i in job:
                if key.lower() == i.lower():
                    counter += 1
            tf.append(counter/len(job))
        df[key] = np.array(tf)
        df[key] = df[key]*key_dic[key] ##### TF * IDF = TF-IDF
        df['TF-IDF'] = df['TF-IDF'] + df[key]
    df = df.sort_values(by=['TF-IDF'], ascending=False)
    df = df.loc[df['TF-IDF'] != 0]
    df = df.iloc[:, :4]
    return df
