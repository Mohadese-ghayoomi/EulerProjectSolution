#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=600851475143
list=[]
for i in range(2, n):
    for x in range(2, i):
        if i % x == 0 :
            pass
            break
    else:
        if(n%i == 0):
            list.append(i)
print(max(list))

