#!/usr/bin/env python
# coding: utf-8

# # Scraping Data from a Real Website + Pandas

# In[4]:


from bs4 import BeautifulSoup
import requests


# In[5]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page= requests.get(url)
soup = BeautifulSoup(page.text,'html')


# In[6]:


print(soup.prettify())


# In[ ]:


#table tag name
#<table class="wikitable sortable jquery-tablesorter">
#<caption>


# In[7]:


soup.find('table', class_='wikitable sortable')


# In[8]:


soup.find_all('table')[1]


# In[9]:


table=soup.find_all('table')[1]


# In[15]:


print(table)


# In[10]:


world_title=table.find_all('th')


# In[11]:


world_title


# In[20]:


world_table_titles = [title.text.strip() for title in world_title]
print(world_table_titles)


# In[21]:


import pandas as pd


# In[22]:


df = pd.DataFrame(columns=world_table_titles)
df


# In[23]:


column_data=table.find_all('tr')


# In[24]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length=len(df)
    df.loc[length] = individual_row_data


# In[44]:


df


# In[45]:


df.to_csv(r'D:\DATA_ANALYTICS\Campanies.csv', index =False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




