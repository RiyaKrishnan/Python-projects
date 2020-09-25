#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd

from pvlib import solarposition,tracking

from pvlib import location


# In[33]:


times=pd.date_range(start='2016-07-01',end='2016-07-04',freq='1min',tz=tus.tz)


# In[34]:


latitude,logitude,tz,altitude,name=32.2,-111,'US/Arizona',700,'Tuscon'


# In[35]:


solarposition.get_solarposition(times,latitude,logitude)


# In[ ]:




