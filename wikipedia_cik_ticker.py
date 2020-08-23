#!/usr/bin/env python
# coding: utf-8

# In[2]:


#A script to extract the SP500 table from Wikipedia and convert it to a CSV

#conda install -c conda-forge wikipedia
import wikipedia as wp
import pandas as pd

#enter the address for the wikipedia page and save to html variable
html = wp.page("List_of_S%26P_500_companies").html().encode("UTF-8")

#[] represents which table from the page you want to use. [0] is the first table on the wikipedia page and contains
#sp500 information table that is needed. 
df = pd.read_html(html)[0]
df.to_csv(r'path_to_csv')

#Extract just the second column of the CSV that contains the ticker symbols using 'usecols=[1]'
#Different columns can be extracted depending on what's needed
dfTicker = pd.read_csv("path_to_csv", usecols=[1])

#Remove the header which says 'Symbol' and the index which numbers the rows
dfTicker.to_csv(r'path_to_csv', header=False, index=False)

#extract the CIK number from the csv file and output to csv. Remove the header 'CIK' and the index which numbers the rows
dfCIK = pd.read_csv("path_to_csv", usecols=[8])
dfCIK.to_csv(r'path_to_csv', header=False, index=False)




# 

# In[ ]:





# In[ ]:




