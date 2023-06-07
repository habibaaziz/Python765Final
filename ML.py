#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Final Project Machine learning 


# In[2]:


#For Machine Learning I will use the following two data sets 


# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


cancer_type_df_1 = pd.read_csv('/home/haziz/Data/cancer-death-rates-by-age.csv')
cancer_type_df_1


# In[7]:


cancer_type_df_1 = cancer_type_df_1[(cancer_type_df_1['Year'] >=2002)]


# In[8]:


cancer_type_df_1


# In[9]:


#Picking the countries 

cancer_type_df_1  = cancer_type_df_1 .query('Entity in ["Norway", "Switzerland" , "Ireland" , "Germany" , "Australia" , "Iceland" , "United Kingdom" , "United States" , "Finland" , "Japan", "Pakistan" , "Yemen" , "Liberia" , "Guinea", "Congo", "Mozambique" , "Afghanistan" , "Zimbabwe" , "Syria" , "Iraq"] ')

cancer_type_df_1 


# In[10]:


cancer_type_df_1['Entity'] = cancer_type_df_1['Entity'].map({ "Norway": 0, "Switzerland": 1, "Ireland": 2, "Germany": 3, "Australia": 4, "Iceland": 5, "United Kingdom": 6, "United States": 7, "Finland": 8, "Japan": 9, "Pakistan": 10, "Yemen": 11, "Liberia": 12, "Guinea": 13, "Congo": 14, "Mozambique": 15, "Afghanistan": 16, "Zimbabwe": 17, "Syria": 18, "Iraq": 19 })


# In[11]:


cancer_type_df_1.isnull().sum()


# In[12]:


cancer_type_df_1 = cancer_type_df_1.dropna()


# In[13]:


cancer_type_df_1.isnull().sum()


# In[14]:


cancer_type_df_1


# In[ ]:





# In[15]:


#Class Distribution
cancer_type_df_1.groupby('Entity').size()


# In[16]:


#cancer_type_df_1['Entity'] = cancer_type_df_5.fit_transform(data['Entity'])
cancer_type_df_1 = cancer_type_df_1.drop(['Code'],axis=1)


# In[17]:


cancer_type_df_1 = cancer_type_df_1.dropna()


# In[18]:


cancer_type_df_1.describe()


# In[19]:


#set up the data
X = cancer_type_df_1.drop('Entity',axis=1)
y = cancer_type_df_1['Entity']


# In[20]:


from sklearn.model_selection import train_test_split


# In[21]:


X_train, X_test, y_train, y_test = train_test_split(X, y)


# In[22]:


from sklearn.tree import DecisionTreeClassifier


# In[23]:


model_cancer = DecisionTreeClassifier().fit(X, y)


# In[24]:


#Steps to test accuracy score


# In[25]:


y_pred_class = model_cancer.predict(X)


# In[26]:


from sklearn import metrics


# In[27]:


import pydotplus
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz


# In[28]:


dot_data = StringIO() #output your visualization to a PNG file
export_graphviz(model_cancer, #DATA
out_file=dot_data,
feature_names=X.columns,
filled=True,
rounded=True,
special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png()) # PNG saved to your local directory


# In[44]:


from sklearn.metrics import accuracy_score


# In[46]:



print('Model accuracy score with criterion gini index: {0:0.4f}'. format(accuracy_score(y, y_pred_class)))


# In[32]:


from sklearn.metrics import classification_report,confusion_matrix


# In[33]:


from sklearn.neural_network import MLPClassifier


# In[36]:


print(confusion_matrix(y, y))


# In[ ]:


from sklearn.metrics import classification_report
#checking for the accuracy 


# In[42]:


print(classification_report(y, y_pred_class))


# In[ ]:




