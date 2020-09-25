#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pvlib

import pandas as pd

from pvlib import clearsky,atmosphere,solarposition

from pvlib.location import Location

from pvlib.iotools import read_tmy3


# In[27]:


tus=Location(32.2, -111, 'US/Arizona', 700, 'Tuscon')


# In[28]:


times=pd.date_range(start='2016-07-01',end='2016-07-04',freq='1min',tz=tus.tz)


# In[29]:


latitude,logitude,tz,altitude,name=32.2,-111,'US/Arizona',700,'Tuscon'


# In[30]:


solpos=pvlib.solarposition.get_solarposition(times,latitude,logitude)


# In[31]:


print(solpos)


# In[ ]:




