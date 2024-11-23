#!/usr/bin/env python
# coding: utf-8

# In[66]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml


# In[9]:


url = requests.get('https://timesofindia.indiatimes.com/elections/lok-sabha-elections/uttar-pradesh/news/priyanka-salutes-congress-cadre-hails-their-courage-in-toughest-of-times/articleshow/110774557.cms')


# In[10]:


soup = BeautifulSoup(url.content,'lxml')


# In[11]:


soup.prettify()


# In[26]:


for tag in soup.find_all('h1',class_='HNMDR'):
    Heading = tag.text


# In[27]:


for tag in soup.find_all('div',class_='xf8Pm byline'):
    Date = tag.text


# In[28]:


for tag in soup.find_all('div',class_='_s30J clearfix'):
    Content = tag.text


# In[68]:


data = {
    'Headline' : [Heading],
    'Date' : [Date],
    'content' : [Content]
}


# In[69]:


pd.DataFrame(data)


# In[ ]:





# In[ ]:




