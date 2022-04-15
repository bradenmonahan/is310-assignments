#!/usr/bin/env python
# coding: utf-8

# In[95]:


import pandas as pd
# disable chained assignments
pd.options.mode.chained_assignment = None


# In[96]:


char_list=pd.read_csv('character_list5.csv',encoding = "ISO-8859-1")
char_map=pd.read_csv('character_mapping.csv',encoding = "ISO-8859-1")
meta=pd.read_csv('meta_data7.csv',encoding = "ISO-8859-1")
print(char_list)


# In[97]:


char_list['age'].isna()


# In[98]:


char_list['age'].unique()


# In[99]:


char_list[['age']].fillna(0.0,inplace=True)


# In[100]:


char_list.rename(columns = {'imdb_character_name':'character_name'},inplace=True)
char_map.rename(columns = {'character_from_script':'character_name'},inplace=True)

words_per_script = char_list.groupby('script_id')['words'].sum().reset_index()

word_increase_over_years=pd.merge(words_per_script,meta,on='script_id')
word_increase_over_years.sort_values('year')


# In[101]:


word_increase_over_years.sort_values('gross',ascending=False)

