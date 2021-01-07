import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate'#Create a handle, page, to handle the contents of the website
soup = BeautifulSoup(url,'lxml')#Store the contents of the website under doc
print(soup.prettify())
