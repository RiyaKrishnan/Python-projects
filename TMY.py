#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os

import inspect

import pvlib


# In[8]:


pvlib_abspath=os.path.dirname(os.path.abspath(inspect.getfile(pvlib)))


# In[9]:


file_abspath=os.path.join(pvlib_abspath,'data','703165TY.csv')


# In[10]:


tmy3_data, tmy3_metadata=pvlib.iotools.read_tmy3(file_abspath)


# In[11]:


tmy3_metadata


# In[12]:


tmy3_data.index.tz

