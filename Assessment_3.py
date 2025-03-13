#!/usr/bin/env python
# coding: utf-8

# ### Importing Necessary Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import IPython
from IPython.display import Image


# In[2]:


Image("C:/Users/Chandrika/Documents/codegnan/Data Analysis/archive/netflix img.png")


# ### Loading the dataset

# In[3]:


file_path = "C:/Users/Chandrika/Documents/codegnan/Data Analysis/archive/netflix_titles_2021.csv" 
netflix = pd.read_csv(file_path)


# ### Data Overview

# In[5]:


netflix.head()


# In[6]:


netflix.sample()


# In[7]:


netflix.columns


# In[8]:


netflix.info()


# In[9]:


netflix.shape


# In[10]:


netflix.describe()


# In[11]:


netflix.describe(include = 'all')


# #### Identifying NULL Values

# In[12]:


netflix.isna().sum()


# #### Deleting NULL Values

# In[13]:


netflix.dropna(subset=['date_added', 'rating', 'duration'], inplace = True) 


# In[14]:


netflix.fillna({'director':'Unknown', 'cast':'Unknown', 'country':'Unknown'}, inplace=True) 


# In[15]:


netflix.isnull().sum()


# ### Data Formatting

# In[16]:


netflix['date_added'] = pd.to_datetime(netflix['date_added'], errors='coerce')


# In[17]:


netflix['date_added'].head()


# ## Visualization On Data

# #### Distribution of Netflix Content Type

# In[18]:


sns.countplot(x = 'type', data = netflix)
plt.title('Distribution of Netflix Content Types')
plt.show()

netflix.type.value_counts()pie_chart = netflix.type.value_count()

plt.pie(pie_chart, labels = pie_chart.index, autopct = "1.2f%%")
plt.show()
# #### Distribution of Content Ratings

# In[19]:


netflix.rating.value_counts()


# In[20]:


plt.figure(figsize = (15,8))
sns.countplot(x = 'rating', data = netflix, order = netflix['rating'].value_counts().index)
plt.title('Distribution of Content Ratings')
plt.show()


# #### Top 10 Countries Producing Most Netflix Content

# In[21]:


content = netflix['country'].value_counts().head(10)

sns.barplot(y = content.index, x = content.values)
plt.title("Top 10 Countries Producing Most Netflix Content")
plt.show()


# #### Movie Duration Analysis

# In[23]:


#converting str into floats vals

movie_duration = netflix[netflix['type']=='Movie'].copy()
movie_duration['duration'] = movie_duration['duration'].str.replace('min','').astype('float')

plt.hist(movie_duration['duration'],color='grey', edgecolor = 'red')
plt.xlabel('Minutes')
plt.ylabel('Count')
plt.title('Movie Duration Analysis')
plt.show()


# #### Distribution of Release Years

# In[24]:


plt.figure(figsize = (12,6))
sns.histplot(netflix['release_year'], bins = 20, color = 'purple', edgecolor = 'red', kde = True)
plt.title('Distribution of Release Years')
plt.show()


# #### Most Frequent Directors

# In[28]:


directors = netflix.loc[netflix['director'] != 'Unknown', 'director'].value_counts().head(10)

plt.bar(directors.index, directors.values, color = 'purple')
plt.xlabel('Names of Directors')
plt.xticks(rotation=90)
plt.ylabel('Count')
plt.title('Most Frequent Directors')
plt.show()


# #### Most Watched Shows On Netflix

# In[29]:


type_show = ['Movie', 'TV Show']
value_counts = [5522, 178]
plt.pie(value_counts, labels = type_show, autopct = '%2.22f%%')
plt.legend('Most Watched Shows On Netflix')
plt.show()


# #### Highest rating TV Show or Movie?

# In[30]:


netflix.groupby("type")['rating'].agg(pd.Series.mode)


# In[ ]:




