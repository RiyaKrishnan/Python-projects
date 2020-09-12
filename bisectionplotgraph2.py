#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x*x*x - 7*x + 5
a=2
b=3

def bisection(a,b):
    
    if(func(a)*func(b) >= 0):
        print("you have not assumed right a and b\n")
        return
    while((b-a) >= 0.001):
        
        c=(a+b)/2
        
        if(func(c)==0.0):
            break
        if(func(c)*func(a) < 0):
            b=c
        else:
            a=c
    print("the value of root is: ","%.4f"%c)
bisection(a,b)
x=np.linspace(-3,3,50)
plt.plot(x, func(x))
plt.grid()
plt.show()
    


# In[ ]:




