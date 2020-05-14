#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[18]:


from numpy.random import randn


# In[19]:


np.random.seed(101)


# In[20]:


df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[21]:


df


# In[22]:


df['W']


# In[23]:


type(df['W'])


# In[24]:


df.W


# In[25]:


df[['W','Z']]


# In[26]:


df['new']=df['W']+df['Y']


# In[27]:


df


# In[30]:


df.drop('new',axis=1,inplace=True)


# In[31]:


df


# In[33]:


df.shape


# In[34]:


df.loc['A']


# In[35]:


df.iloc[0]


# In[36]:


df.loc['B','Y']


# In[38]:


df.loc[['A','B'],['W','Y']]


# In[ ]:




