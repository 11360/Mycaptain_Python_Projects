#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/Hello_(Adele_song)"
req=requests.get(url)
content=req.content
soup=BeautifulSoup(content,"html.parser")
s=soup.find("div",{"class":"mw-content-container"})
print(s.text)


# In[ ]:




