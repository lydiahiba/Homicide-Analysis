# import streamlit as st 
# import pandas as pd
# from sqlalchemy import create_engine
# import time

# st.text('Hello world')

# conn = create_engine('mysql+pymysql://root:rootpassword@localhost:3308/MY_DB')
# SQL_script = st.text_area(label='SQL Input', value='SELECT * FROM country_info')

# @st.cache
# def load_data():
#     with st.spinner('Loading Data...'):
#         time.sleep(0.5)
#         df = pd.read_sql_query(SQL_script, conn)
#     return df

# raw_data = load_data()
# raw_data

import streamlit as st
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
st.title("YO Whassupp!")
import mysql.connector
mydb = mysql.connector.connect(
    host="mysql", ## LE NOM DU SERVICE mysql SUR docker-compose 
    port="3308", ## le port sur lequel est mapper le container 
    user="root", 
    password="rootpassword",
    database = "MY_DB"
)
st.title("Connection Done!")
print(mydb)
cursor = mydb.cursor()
# #sql = "CREATE TABLE regions (id INT AUTO_INCREMENT PRIMARY KEY, region VARCHAR(255));"
# #cursor.execute(sql)
# st.write(cursor.execute("SHOW TABLES"))

def view_all_notes():
    # cursor.execute('SELECT * FROM country_info')
    # data = cursor.fetchall()
    # data = pd.DataFrame(data=cursor.fetchall(), index = None)
    query='SELECT * FROM country_info'
    data=pd.read_sql(query, mydb)
    return data

data = view_all_notes() 
st.write(data)
