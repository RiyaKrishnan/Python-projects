#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pvlib

import pandas as pd

from pvlib import solarposition

from pvlib import irradiance

from pvlib.location import Location

from pvlib.iotools import read_tmy3


# In[16]:


haw=Location(19.74, -155.84, 'US/Hawaii', 700, 'Hawaii')


# In[17]:


times=pd.date_range(start='2016-07-01',end='2016-07-04',freq='1min',tz=haw.tz)


# In[18]:


latitude,logitude,tz,altitude,name=19.74,-155.84,'US/Hawaii',700,'Hawaii'


# In[19]:


solpos=pvlib.solarposition.get_solarposition(times,latitude,logitude)


# In[20]:


print(solpos)


# In[24]:


haw.get_clearsky(times)


# In[22]:





# In[23]:





# In[13]:





# In[ ]:




