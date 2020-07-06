#!/usr/bin/env python
# coding: utf-8

# In[2]:


#directory to add element
Dict= { 1: 'my' }
Dict[2]= 'name'
Dict[3]= 'is' , 'riya'
print(Dict)


# In[3]:


#directory (to remove element)
Dict= {1: 'the' , 'name' : 'for'}
Dict.pop(1)
print(Dict)


# In[5]:


#set (to add elements)
name= {4,2,3}
name.add(6)
print(name)


# In[6]:


#set (to remove element)
name={4,6,2,5,3}
name.remove(6)
print(name)


# In[12]:


#list (to add element)
List=['flying', 'away']
List.append(5)
print(List)


# In[14]:


#list (to remove an element)
List=['flying', 'away' , 5]
List.remove(5)
print(List)


# In[ ]:




