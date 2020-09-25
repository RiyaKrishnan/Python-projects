#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd

from pvlib import irradiance

from pvlib import location


# In[42]:


lat,lon=39.755,-105.221


# In[43]:


tz='MST'


# In[44]:


site=location.Location(lat,lon,tz=tz)


# In[45]:


times=pd.date_range(start='2016-07-01',end='2016-07-04',freq='1min',tz=site.tz)


# In[46]:


site.get_clearsky(times)


# In[ ]:




