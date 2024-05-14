
# coding: utf-8

# # This notebook is ready for your projects and experiments
# 
# Go ahead and code!

# In[1]:


# Import the variables

import pandas as pd
data = pd.read_csv('happyscore_income.csv')
happy = data['happyScore']
income = data['avg_income']
ineq = data['income_inequality']
gdp = data['GDP']
satis = data['avg_satisfaction']
country = data['country']


# In[2]:


# Sort the data

data.sort_values('happyScore', inplace=True)
lowest_happy = data.iloc[0]
highest_happy = data.iloc[-1]

print(lowest_happy)

data.sort_values('GDP', inplace=True)
lowest_gdp = data.iloc[0]
highest_gdp = data.iloc[-1]


# In[53]:


# Plot the data

import matplotlib.pyplot as plt
plt.scatter(gdp,happy)
plt.title("Happy Score vs GDP")
plt.xlabel('GDP',fontdict=None)
plt.ylabel('Happy Score',fontdict=None)

for k, row in data.iterrows():
    plt.text(lowest_gdp['GDP'],
             lowest_gdp['happyScore'],
             lowest_gdp['country'])
    
for k, row in data.iterrows():
    plt.text(highest_gdp['GDP'],
             highest_gdp['happyScore'],
             highest_gdp['country'])
    
for k, row in data.iterrows():
    plt.text(lowest_happy['GDP'],
             lowest_happy['happyScore'],
             lowest_happy['country'])
    
for k, row in data.iterrows():
    plt.text(highest_happy['GDP'],
             highest_happy['happyScore'],
             highest_happy['country'])

print('I plotted happyScore against GDP to see if there is a correlation between the economic health of a country and the happy score. As per the graph, it shows a positive trend implying higher GDP generally leads to a higher happy score. I sorted the data for GDP in ascending order. I labelled the country with lowest and highest GDP to see their respective happy scores.')


# In[34]:


# K-Means

from sklearn.cluster import KMeans
import numpy as np

gdp_happy = np.column_stack((gdp,happy))
km_res = KMeans(n_clusters = 3).fit(gdp_happy)
clusters = km_res.cluster_centers_
plt.scatter(gdp,happy)
plt.scatter(clusters[:,0],clusters[:,1], s = 100)


# In[50]:


# Sort the data

data.sort_values('happyScore', inplace=True)
lowest_happy = data.iloc[0]
highest_happy = data.iloc[-1]


# In[48]:


plt.scatter(gdp,happy)
plt.title("Happy Score vs GDP")
plt.xlabel('GDP',fontdict=None)
plt.ylabel('Happy Score',fontdict=None)

for k, row in data.iterrows():
    plt.text(lowest_happy['GDP'],
             lowest_happy['happyScore'],
             lowest_happy['country'])
    
for k, row in data.iterrows():
    plt.text(highest_happy['GDP'],
             highest_happy['happyScore'],
             highest_happy['country'])

