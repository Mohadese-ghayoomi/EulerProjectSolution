#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list=[]
for index in range(1,1000):
    x=index*3 
    y=index*5
    if x<1000 and x not in list:
        list.append(x)
    if y<1000 and y not in list:
        list.append(y)
sum(list)

