from sqlalchemy.orm import Session, relationship
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, ForeignKeyConstraint
import pandas as pd
engine = create_engine('mysql+pymysql://root:rootpassword@127.0.0.1:3308/MY_DB')
meta = MetaData()

country_df = pd.read_csv('./Data/country_info_table.csv')
table_name = 'country_info'
country_df.to_sql(
 table_name,
 engine,
 if_exists='replace',
 index=False,
 chunksize=500,
 dtype={
    'country': String(50), 
    'Subregion': String(50),
    'Rate': Float, 
    'Count': Integer,
    'Region': String(50), 
    'Happiness_Rank': Float,
    'Happiness_Score': Integer,
    'Lower_Confidence_Interval': Float,
    'Upper_Confidence_Interval': Float, 
    'Family': Float,
    'Life_Expectancy': Float, 
    'trust': Float,
    'Generosity': Float, 
    'Dystopia_Residual': Float,
    'gdp_per_capita': Float, 
    'gdp_for_year': Float,
    'population': Integer,
	'suicides_no':Float,
	'suicides_rate_per_100k':Float,
	'region_id':Integer,
 }
)
table_df = pd.read_sql_table(
 table_name,
 con=engine
)

id_df = pd.read_csv('./Data/country_id_table.csv')
table_name = 'country_id'
id_df.to_sql(
 table_name,
 engine,
 if_exists='replace',
 index=False,
 chunksize=500,
 dtype={
    'country': String(50), 
    'region_id':Integer,
 }
)
table_df = pd.read_sql_table(
 table_name,
 con=engine
)


## create primary key and foreign key 
engine.execute('ALTER TABLE country_info ADD PRIMARY KEY (country);')
engine.execute('ALTER TABLE country_info ADD FOREIGN KEY (region_id);')
