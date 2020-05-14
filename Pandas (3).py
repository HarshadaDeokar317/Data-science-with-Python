#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[74]:


d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}


# In[75]:


df=pd.DataFrame(d)


# In[76]:


df


# In[78]:


df.dropna(axis=1)


# In[79]:


df.fillna(value='Fill value')


# In[80]:


df['A'].fillna(value=df['A'].mean())


# In[68]:


df.loc['G2'].loc[2]['B']


# In[72]:


df.xs('G1')


# In[73]:


df.xs(1,level='num')


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


# In[40]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[48]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[53]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




