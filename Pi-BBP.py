#!/usr/bin/env python
# coding: utf-8

# In[10]:


from decimal import Decimal,getcontext

getcontext().prec=1000

print (sum(1/Decimal(16)**k * 
          (Decimal(4)/(8*k+1) - 
           Decimal(2)/(8*k+4) - 
           Decimal(1)/(8*k+5) -
           Decimal(1)/(8*k+6)) for k in range(1000))
      )


# In[ ]:
# This is the child branch program





