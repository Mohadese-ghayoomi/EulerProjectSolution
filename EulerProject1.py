#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list=[0,1]
Sum=[]
for i in range(2,34):
   list.append(list[-2]+list[-1])
print(list)
for i in list:
   if i%2==0:
       Sum.append(i)
print(sum(Sum))

