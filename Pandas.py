#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import 


# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}


# In[5]:


pd.Series(data=my_data)


# In[6]:


pd.Series(data=my_data,index=labels)


# In[7]:


pd.Series(arr)


# In[9]:


ser1=pd.Series([1,2,3,4],['USA','JAPAN','USSR','GERMANY'])


# In[10]:


ser1


# In[11]:


ser2=pd.Series([1,2,3,4],['USA','ITELY','USSR','GERMANY'])


# In[12]:


ser2


# In[13]:


ser1['USA']


# In[14]:


ser3=pd.Series(data=labels)


# In[15]:


ser3


# In[16]:


ser3[0]


# In[17]:


ser1+ser2


# In[ ]:




