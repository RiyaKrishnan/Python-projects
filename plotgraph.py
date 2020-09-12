#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5,6])
y=np.array([6,7,8,9,10,11])
n= np.size(x)
m_x=np.mean(x)
m_y=np.mean(y)
SSyx= np.sum(y*x) - n*m_x*m_y
SSxx= np.sum(x*x) - n*m_x*m_x
b_1=SSyx/SSxx
b_0=np.sum(y)/n- (b_1*sum(x)/n)
print("the regressions are \n")
print("b1=\n", b_1)
print("b_0=\n", b_0)
plt.scatter(x,y,color = "m", marker = "o" , s= 30)
ypred= b_1 * x + b_0
plt.plot(x, ypred, color= 'g')
plt.xlabel('price')
plt.ylabel('price change in $')
plt.show()


# In[ ]:




