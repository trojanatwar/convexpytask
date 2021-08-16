#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("flightData.csv")


# In[3]:


df.head()


# In[4]:


# Creating dummy column to store new generated data
df = df.assign(total_flights="")


# In[12]:


df['total_flights'] = df.groupby(['passengerId'])[['from','to']].transform(lambda x : ' '.join(x))


# In[13]:


df


# In[14]:


# f_count funtion will take string as an agrument and returns maximum distance between two same occurance in the list

def f_count(s):
  l = s.split(' ')
  d = 0
  for i in range(len(l)):
    for j in range(i + 1, len(l)):
      if l[i] == l[j]:
        d = j - i
  
  return d


# In[15]:


df['Longest_Run'] = df.apply(lambda x: f_count(x['total_flights']), axis=1)
df


# In[19]:


new_df = df[['passengerId', 'Longest_Run']]
new_df.sort_values('Longest_Run', ascending=False)


# In[ ]:


new_df.to_csv("output4.csv")

