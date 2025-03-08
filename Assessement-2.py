#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import pandas as pd
import statistics


# In[12]:


#loading data set
data = pd.read_csv("C:/Users/Chandrika/Indian_Cricket_Team_Dataset.csv")


# In[13]:


data


# In[15]:


data['Age']


# In[17]:


#Convert 'Age' column to a NumPy array.
age = np.array([a.Age])
age


# In[19]:


# Find the average age of players. 
age.mean()


# In[20]:


# Find the oldest and youngest player age.
age.min()


# In[21]:


age.max()


# In[24]:


# Count the total number of players above 30 years old.
age[age > 30]


# In[26]:


# Find the median batting average. 
data.head()


# In[27]:


data['Batting Average'].median()


# In[31]:


# Find the standard deviation of strike rates
data['Strike Rate'].std


# In[33]:


# Find the 90th percentile of batting average
data.describe()


# In[45]:


percentile_90 = np.percentile(data['Batting Average'], 90)
print(percentile_90)


# In[35]:


# Find the number of players with strike rate above 150
strike_rate = data['Strike Rate'] > 150
strike_rate.sum()


# In[53]:


# Reshape the first 20 batting averages into a 4x5 matrix.
bat_avg = data['Batting Average'].head(20)


# In[54]:


bat_avg


# In[58]:


bat_avg.shape


# In[62]:


matrix = bat_avg.to_numpy().reshape(4, 5)
print(matrix)


# In[64]:


# Compute row-wise sum of reshaped matrix
matrix.sum(axis=0)


# In[66]:


# Compute column-wise mean of reshaped matrix. 
matrix.mean(axis=1)


# In[67]:


# Transpose the reshaped matrix.
trans_mat = matrix.T
trans_mat


# In[70]:


# Find the variance of batting average. 
data['Batting Average'].var()


# In[74]:


# Stack age and matches played horizontally.
stacked = np.stack((data['Age'],data['Matches Played']))
stacked


# In[77]:


# Split the batting average array into 5 equal parts.
split_arr = np.split(data['Batting Average'],5)


# In[78]:


print(split_arr)


# In[79]:


s_a = np.split(bat_avg,5)
print(s_a)


# In[ ]:




