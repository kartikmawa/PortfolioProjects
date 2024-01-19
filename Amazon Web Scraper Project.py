#!/usr/bin/env python
# coding: utf-8

# # Amazon Web Scraper Project

# In[28]:


# Import lib
import pandas as pd
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[13]:


# Connect to website
url = 'https://www.amazon.com/dp/B00GG1JCZG/ref=sspa_dk_detail_2?pd_rd_i=B00GG1JCZG&pd_rd_w=vlC1C&content-id=amzn1.sym.a53ea610-e450-44d1-897e-68c0c718bf50&pf_rd_p=a53ea610-e450-44d1-897e-68c0c718bf50&pf_rd_r=7BTTXMYZ4R7GAPTXYNK0&pd_rd_wg=3WGAL&pd_rd_r=e6bb04ad-e38d-4849-8e43-bf7689a2cd6a&s=apparel&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(url,headers=headers)

soup1 = BeautifulSoup(page.content,'html.parser')

soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

title = soup2.find(id='productTitle').get_text()

#for getting class related tags in a website
price = soup2.find(attrs={'class':"a-offscreen"}).get_text()

print(title)
print(price)


# In[14]:


price=price.strip()[1:]
title=title.strip()


# In[19]:


print(title)
print(price)


# In[22]:


import datetime

today = datetime.date.today()
print(today)


# In[27]:


import csv

header= ['Title', 'Price', 'Date']
data = [title, price, today]

with open('AmazonWebScraperData.csv','a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)




# In[30]:


df = pd.read_csv(r"C:\Users\HP\AmazonWebScraperData.csv")
df


# In[32]:


def check_price():
    url = 'https://www.amazon.com/dp/B00GG1JCZG/ref=sspa_dk_detail_2?pd_rd_i=B00GG1JCZG&pd_rd_w=vlC1C&content-id=amzn1.sym.a53ea610-e450-44d1-897e-68c0c718bf50&pf_rd_p=a53ea610-e450-44d1-897e-68c0c718bf50&pf_rd_r=7BTTXMYZ4R7GAPTXYNK0&pd_rd_wg=3WGAL&pd_rd_r=e6bb04ad-e38d-4849-8e43-bf7689a2cd6a&s=apparel&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1&psc=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url,headers=headers)

    soup1 = BeautifulSoup(page.content,'html.parser')

    soup2 = BeautifulSoup(soup1.prettify(),'html.parser')

    title = soup2.find(id='productTitle').get_text()

    #for getting class related tags in a website
    price = soup2.find(attrs={'class':"a-offscreen"}).get_text()

    price=price.strip()[1:]
    title=title.strip()

    import datetime

    today = datetime.date.today()

    import csv

    header= ['Title', 'Price', 'Date']
    data = [title, price, today]
    
    with open('AmazonWebScraperData.csv','a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    if(price<14):
        send_mail()
    


# In[ ]:


# For automating it to run for n seconds 
# We are going to run it every single day.
while(True):
    check_price()
    time.sleep(86400)


# In[34]:


df = pd.read_csv(r"C:\Users\HP\AmazonWebScraperData.csv")
df


# In[ ]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.elho()
    server.login('kartik.21810747@viit.ac.in','mawakartik02121999!!')
    subject = 'The Shirt you want is less than $14! Now is your chance to buy!'
    body = 'Hey, Kartik the T-shirt you want is within your expected price range, please go and buy it'
    msg = f"subject:{subject}\n\n{body}"
    server.sendmail(
        'kartik.21810747@viit.ac.in',
        msg
    )


# In[ ]:





# In[ ]:




