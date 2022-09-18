#!/usr/bin/env python
# coding: utf-8

# In[2]:


numeros = [0,1,2,3,45,46,47,52,68,236,241,528]
print(numeros)


# In[3]:


pares = []
for valor in numeros:
    if valor % 2 == 0:
        pares.append(valor)

print(len(pares))


# In[ ]:




