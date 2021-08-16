#!/usr/bin/env python
# coding: utf-8

# ## Intializing with importing library and loading dataset

# In[1]:


import pandas as pd


# In[2]:


data_frame = pd.read_csv("flightData.csv")


# In[3]:


data_frame.head()


# In[4]:


data_frame.info()


# In[5]:


# checking date format
    
date = data_frame['date']   
date


# In[10]:


# Extracting month from the given date format for sake simplicity

# data_frame['date'] = pd.to_datetime(data_frame['date'], format='%Y/%m/%d').dt.strftime('%d-%m-%Y')

data_frame['month'] = pd.DatetimeIndex(data_frame['date']).month


# In[7]:


# Seprating 'month' and 'to' columns to perform aggregation operation. 

df1 = data_frame[['month', 'to']]

# Creating dummy column

df1 = df1.assign(NoOfFlights="") 
df1


# ## Total number of flights to each location for each month

# In[8]:


df2 = df1.groupby(['month','to']).count().reset_index(drop = False)
df2


# In[9]:


result = (
  data_frame
  .groupby(['month','to'])
  .apply(lambda x: pd.Series({
      'no_of_flights': x['to'].count()
  }))
  .reset_index()
)
result

