#!/usr/bin/env python
# coding: utf-8

# In[8]:


import requests
api_address='http://api.openweathermap.org/data/2.5/weather?appid=61d6f5e07edeed8a1d3c317e61c67601&q= '
city= input('city name:')
url=api_address + city
json_data=requests.get(url).json()
print('=========Weather Report========')
print('city name: ' + json_data ["name"])
print('Timezone: ' + str(json_data["timezone"]))


# In[ ]:




