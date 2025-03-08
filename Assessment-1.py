#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


data = pd.read_excel("C:/Users/Chandrika/Movies_Dataset.xlsx")


# In[4]:


print(data)


# In[5]:


data.head()


# In[6]:


data.tail()


# In[11]:


#all movies in action genre
data_1 = data[data['Genre'] == 'Action']
print(data_1)


# In[12]:


#movies released after 2000
rel = data[data['Release_Year']>2000]
print(rel)


# In[13]:


rating = data[data['IMDb_Rating']>8.5]
print(rating)


# In[18]:


data[['Movie Name','Genre']]


# In[26]:


data_2 = data[(data['Release_Year'] >= 1990) & (data['Release_Year'] <= 2010)]
print(data_2)


# In[27]:


data['Genre'].value_counts()


# In[30]:


data_3 = data[data['IMDb_Rating'] == data['IMDb_Rating'].max()]
print(data_3)


# In[33]:


data['IMDb_Rating'].mean()


# In[34]:


data['Revenue'].sum()


# In[36]:


movies = data[data['Revenue']>500]
print(movies)


# In[39]:


data['Rank'] = data['IMDb_Rating'].rank(ascending=False)
data.head()


# In[44]:


data.sort_values(by='Release_Year',ascending=False)
data.head(10)


# In[47]:


data[data.duplicated(subset=['Movie Name'])]


# In[48]:


data.drop_duplicates(subset=['Movie Name'])


# In[51]:


dataa = data['Genre'].replace('Sci-Fi','Science Fiction')
print(dataa)


# In[52]:


data['Movie Name'].head(10)


# In[53]:


data['Movie Name'].tail(5)


# In[54]:


data.groupby('Genre')['IMDb_Rating'].mean()


# In[55]:


data['Release_Year'].value_counts().sort_index()


# In[56]:


data.groupby('Genre')['Revenue'].sum()


# In[ ]:




