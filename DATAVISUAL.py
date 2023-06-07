#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Final research project Data-765 


# In[2]:


#Importing couple of modules here 


# In[30]:


import pandas as pd
import glob
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, mannwhitneyu
import seaborn as sns
import statsmodels as sm
from scipy.stats import kendalltau


# In[31]:


Data_df = glob.glob("/home/haziz/Data/*.csv" ) #intialization


# In[32]:


Data_df


# In[33]:


# I gathered all these data sets, so of them had a lot of missong data in them so I had to drop them.


# In[34]:


#The data were pulled from https://ourworldindata.org/ and cancer atlas
#I will be using few data-sets for my analysis 


# Analysis on Neoplasm Incidence for Both the sex.
# A new and abnormal growth of tissue in some part of the body, especially as a characteristic of cancer.
# This data was pulled from https://ourworldindata.org/
# 
# New Cases per 100,000 for different countries around the globe. 1990 to 2017

# In[35]:


cancer_type_df = pd.read_csv('/home/haziz/Data/cancer-incidence.csv')
cancer_type_df


# In[36]:


cancer_type_df.Entity.unique()


# In[37]:


cancer_type_df


# In[38]:


#checking for null values

cancer_type_df.isnull().sum()


# In[39]:


#Checking for length 
len(cancer_type_df)


# In[40]:


cancer_type_df = cancer_type_df.dropna()


# In[41]:


cancer_type_df.isnull().sum()


# top: Norway,Switzerland,Ireland,Germany, Australia,Iceland,United Kingdom,United States,Finland,Japan <br>
# low: Pakistan, Yemen, Liberia, Guinea, Congo, Mozambique,Afghanistan,Zimbabwe,Syria,Iraq      

# In[42]:


#cancer_type_df_new
cancer_type_df_new = cancer_type_df[(cancer_type_df['Year'] >=2002) & (cancer_type_df['Incidence - Neoplasms - Sex: Both - Age: Age-standardized (Rate) (new cases per 100,000)'] > 0)]
cancer_type_df_new


# In[43]:


#Replacing the column name 

cancer_type_df_new = cancer_type_df_new.rename(columns={"Incidence - Neoplasms - Sex: Both - Age: Age-standardized (Rate) (new cases per 100,000)":"Incidence_Neoplasms"})


# In[44]:


cancer_type_df_new


# In[18]:


cancer_type_df_new.describe()


# In[19]:


import seaborn as sns


# In[20]:


plt.figure(figsize=(20,10))

sns.boxplot('Year', 'Incidence_Neoplasms',   data=cancer_type_df_new)


# In[21]:


from ggplot import *


# In[22]:


ggplot(cancer_type_df_new, aes(x='Year', y='Incidence_Neoplasms') ) +    geom_boxplot() +    theme(element_text(face = "bold", color = "black", size = 12)) 
   
   
 


# Here we can see that Incidence of Neoplasm (Age standardised for both sexes per 100,000 new cases)  around the globe starting from 2002 to 2017.  In the year 2002 there was a decline in number of cases i.e., the maximum number of new cases were 1000 and the minimum less than 200. 

# In[23]:


#Picking the countries 

cancer_type_df_new1 = cancer_type_df_new.query('Entity in ["Norway", "Switzerland" , "Ireland" , "Germany" , "Australia" , "Iceland" , "United Kingdom" , "United States" , "Finland" , "Japan", "Pakistan" , "Yemen" , "Liberia" , "Guinea", "Congo", "Mozambique" , "Afghanistan" , "Zimbabwe" , "Syria" , "Iraq"] ')
   


# In[24]:


cancer_type_df_new1


# In[25]:


cancer_type_df_new1.max()


# In[26]:


cancer_type_df_new1.min()


# In[27]:


cancer_type_df_new1.describe()


# In[28]:


#I picked 10 high and 10 low HDI countries based on UN data

sns.FacetGrid(cancer_type_df_new1, hue="Entity", size=10)    .map(plt.scatter, "Year", "Incidence_Neoplasms"  ) .add_legend()


# In[29]:


import plotly.express as px
fig = px.scatter(cancer_type_df_new1, x="Year", y="Incidence_Neoplasms", color="Entity", color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta", "cyan", "crimson", "darkblue", "darkcyan", "black", "coral", "rosybrown", "purple", "chocolate", "cornsilk", "chartreuse", "turquoise", "darkmagenta", "plum", "yellow"], title="Neoplasms Incidence from 2002-2017 per new 100,000 cases based on 20 countries ")
fig.update_traces(marker=dict(size=10,
                              line=dict(width=1,
                                        color='black')),
                  selector=dict(mode='markers'))
fig.show()


# In[ ]:





# In[140]:


#GDP 


# In[45]:


cancer_type_df_2 = pd.read_csv('/home/haziz/Data/death-rate-from-cancers-vs-average-income.csv')


# In[46]:


cancer_type_df_2 


# In[47]:


cancer_type_df_2.isnull().sum()


# In[48]:


cancer_type_df_2 = cancer_type_df_2.dropna()


# In[49]:


cancer_type_df_2.isnull().sum()


# In[50]:


#colummn name chage 
cancer_type_df_GDP = cancer_type_df_2.rename(columns={"GDP per capita, PPP (constant 2011 international $) (constant 2011 international $)" : "GDP", "Cancers – age-standardized death rate (deaths per 100,000 individuals)":"Cancer_Deaths"})


# In[51]:


cancer_type_df_GDP.head()


# In[52]:


from scipy.stats import pearsonr, mannwhitneyu
import seaborn as sns
import statsmodels as sm
from scipy.stats import kendalltau
import numpy as np


# In[53]:


corrmatrix = cancer_type_df_GDP[['Cancer_Deaths','GDP','Total population (Gapminder)']].corr()


# In[54]:


corrmatrix


# In[55]:


f,ax = plt.subplots(figsize=(15, 9))
sns.heatmap(corrmatrix)


# In[56]:



sns.jointplot(cancer_type_df_GDP['GDP'], cancer_type_df_GDP['Cancer_Deaths'] ,
              
              kind="hex", stat_func=kendalltau, color="#FF030D")


# In[ ]:





# In[ ]:





# In[39]:


#HDI


# In[57]:


cancer_type_df_6 = pd.read_csv('/home/haziz/Data/human-development-index-vs-corruption-perception-index.csv')
cancer_type_df_6


# In[58]:


cancer_type_df_6.isnull().sum()


# In[59]:


cancer_type_df_6 = cancer_type_df_6.dropna()


# In[60]:


cancer_type_df_6.isnull().sum()


# In[61]:


cancer_type_df_6


# In[62]:


cancer_type_df_6_a = cancer_type_df_6[(cancer_type_df_6['Year'] >=2002)]


# In[63]:


cancer_type_df_6_a


# In[64]:


cancer_type_df_6_a = cancer_type_df_6[(cancer_type_df_6['Year'] >=2002) |(cancer_type_df_6['Year'] >=2017)]               


# In[65]:


cancer_type_df_6_a


# In[66]:


cancer_type_df_6_a = cancer_type_df_6_a.rename(columns={"Human Development Index ((0-1; higher values are better))":"HDI", "Population by country":"Population" })


# In[67]:


cancer_type_df_6_a


# In[ ]:





# In[84]:


#Merge


# In[68]:


result = pd.merge(cancer_type_df_GDP,
                 cancer_type_df_6_a[['Entity',  'HDI', 'Population']],
                 on='Entity')


# In[69]:


result


# In[70]:


result.isnull().sum()


# In[71]:


result1 = pd.merge(result,
                cancer_type_df_new[['Entity', 'Incidence_Neoplasms']],
                on='Entity' 
                )


# In[72]:


result1


# In[90]:


result1.isnull().sum()


# In[73]:


result1 = result1.dropna()


# In[74]:


result1


# In[79]:


#here the subset value will keep all the years 2002 to 2017 for the countries, while the drop duplicate will drop duplicate rows 
result1 = result1.drop_duplicates(subset =("Year", "Entity"))


# In[80]:


result1


# In[82]:


result1


# In[256]:


#After removing null values from both the merged tables the out come data is available from year 2002 to 2017 


# In[83]:


corrmatrix = result1[['HDI','GDP','Cancer_Deaths','Incidence_Neoplasms']].corr()


# In[84]:


corrmatrix


# In[85]:


f,ax = plt.subplots(figsize=(15, 9))
sns.heatmap(corrmatrix)


# In[86]:


sns.jointplot(result1['HDI'], result1['Cancer_Deaths'] , 
              kind="hex", stat_func=kendalltau, color="#FF030D", size = 8 )


# In[87]:


sns.jointplot(result1['GDP'], result1['Cancer_Deaths'] , 
              kind="hex", stat_func=kendalltau, color="#FF030D", size = 8 )


# In[89]:


#Picking the countries 

result2 = result1.query('Entity in ["Norway", "Switzerland" , "Ireland" , "Germany" , "Australia" , "Iceland" , "United Kingdom" , "United States" , "Finland" , "Japan", "Pakistan" , "Yemen" , "Liberia" , "Guinea", "Congo", "Mozambique" , "Afghanistan" , "Zimbabwe" , "Syria" , "Iraq"] ')

result2


# In[ ]:





# In[ ]:




