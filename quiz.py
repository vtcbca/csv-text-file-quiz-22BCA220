#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv 


# In[4]:


#field name
fields=['name','contect']
data=[['om','6355786899'],['sai','9023137700'],
      ['ram','8160876821'],['kishan','9979246401']
     ]
filename="contect.csv"


# In[6]:


with open(filename, 'w',newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(data)


# In[7]:


with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
    field=next(csvreader)


# In[ ]:




