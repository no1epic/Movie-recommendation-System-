#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


credits_df = pd.read_csv("/Users/sahilgawande/Downloads/credits.csv")
movies_df = pd.read_csv("/Users/sahilgawande/Downloads/movies_1.csv")


# In[3]:


credits_df.head(5)


# In[4]:


movies_df.head(5)


# In[5]:


movies_df = movies_df.merge(credits_df, on = 'title')


# In[6]:


movies_df.shape


# In[7]:


movies_df.info()


# In[8]:


movies_df = movies_df[['movie_id','title','overview','genres','keywords','cast','crew']]


# In[9]:


movies_df


# In[10]:


movies_df.isnull().sum()


# In[11]:


movies_df.dropna(inplace = True)


# In[12]:


movies_df.duplicated().sum()


# In[13]:


movies_df.iloc[0].genres


# In[14]:


import ast
from ast import literal_eval


# In[15]:


def convert(obj):
    L=[]
    for i in literal_eval(obj):
        L.append(i['name'])
        return L


# In[16]:


movies_df['genres'] = movies_df['genres'].apply(convert)
movies_df['keywords'] = movies_df['keywords'].apply(convert)


# In[17]:


movies_df.head()


# In[18]:


def convert3(obj):
    L=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else: 
            break
        return L


# In[19]:


movies_df['cast'] = movies_df['cast'].apply(convert3)


# In[20]:


movies_df.head()


# In[21]:


def fetch_director(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L        


# In[22]:


movies_df['crew'] = movies_df['crew'].apply(fetch_director)


# In[23]:


movies_df['overview'] =movies_df['overview'].apply(lambda x:x.split())


# In[27]:


movies_df['genres'] = movies_df['genres'].apply(lambda x:[i.replace(" ","") for i in x] if x is not None else [])
movies_df['keywords'] = movies_df['keywords'].apply(lambda x: [i.replace(" ", "") for i in x] if x is not None else [])
movies_df['cast'] = movies_df['cast'].apply(lambda x: [i.replace(" ", "") for i in x] if x is not None else [])
movies_df['crew'] = movies_df['crew'].apply(lambda x: [i.replace(" ", "") for i in x] if x is not None else [])


# In[28]:


movies_df['tags'] = movies_df['overview'] + movies_df['genres'] + movies_df['keywords'] + movies_df['cast'] +movies_df['crew']


# In[29]:


movies_df


# In[30]:


new_df = movies_df[['movie_id','title','tags']]


# In[31]:


new_df


# In[32]:


new_df['tags'] = new_df['tags'].apply(lambda x:' '.join(x))


# In[33]:


new_df.iloc[0]


# In[34]:


new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())


# In[35]:


new_df


# In[36]:


from sklearn.feature_extraction.text import CountVectorizer


# In[37]:


cv = CountVectorizer(max_features = 5000, stop_words ='english')


# In[38]:


cv.fit_transform(new_df['tags']).toarray().shape


# In[39]:


vectors = cv.fit_transform(new_df['tags']).toarray()


# In[40]:


vectors[0]


# In[41]:


len(cv.get_feature_names())


# In[42]:


import nltk


# In[44]:


from nltk.stem.porter import PorterStemmer
ps= PorterStemmer()


# In[45]:


def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
        return " ".join(y)


# In[46]:


new_df['tags'] = new_df['tags'].apply(stem)


# In[48]:


from sklearn.metrics.pairwise import cosine_similarity


# In[49]:


cosine_similarity(vectors)


# In[50]:


cosine_similarity(vectors).shape


# In[51]:


similarity = cosine_similarity(vectors)


# In[52]:


sorted(list(enumerate(similarity[0])), reverse= True, key= lambda x:x[1])[1:6]


# In[53]:


def reccomend(movie):
    movie_index = new_df[new_df['title']== movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    for i in movies_list:
        print(new_df.iloc[i[0]].title)
        


# In[59]:


reccomend('The Dark Knight Rises')


# 

# 
