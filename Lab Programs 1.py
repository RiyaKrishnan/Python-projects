#!/usr/bin/env python
# coding: utf-8

# In[1]:


#no.of didgits
num=1000056709
count=0
while num!=0:
    num //=10
    count+=1
print("totalcounts are:", count)    


# In[2]:


#display multiples of 5 and stop after 150
list1=[12,15,32,42,55,75,122,132,150,180,200]
for i in list1:
    if(i % 5==0):
        print(i)
    if(i>=150):
        break


# In[ ]:




