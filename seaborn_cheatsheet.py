#!/usr/bin/env python
# coding: utf-8

# # Seaborn Cheatsheet

# In[1]:


get_ipython().system('pip install seaborn')


# In[2]:


import seaborn as sn


# In[3]:


import pandas as pd
data1 = pd.read_csv("data.csv")


# # Statistical Relationship - Scatter Plot

# In[4]:


sn.relplot(x = 'hours', y= 'marks', hue = 'age', data = data1)


# # Statistical Relationship - Line Plot

# In[5]:


sn.relplot(x = 'hours',y = 'marks',hue = 'age',data = data1,kind = 'line',style = 'internet')


# In[6]:


sn.relplot(x = 'hours',y = 'marks',hue = 'age',data = data1,col = 'internet')


# # Data Distribution - Histogram

# In[8]:


sn.displot(data1, x = 'marks', binwidth = 0.5, hue = 'internet')


# In[11]:


sn.displot(data1,x = 'age', bins = [10,11,12,13,14,15,16,17,18,19,20])


# In[15]:


sn.displot(data1, x = 'marks',hue = 'age',col = 'internet')


# # Data distribution - Bivarte Distribution

# In[16]:


sn.displot(data1, x= 'age', y = 'marks', hue = 'internet')


# # DD - Kernel Density Estimation

# In[17]:


sn.displot(data1, x = 'age', y = 'marks', kind = 'kde', hue = 'internet')


# # DD - Pair Plot

# In[18]:


sn.pairplot(data1)


# # Categorical Data

# # Scatter plot

# In[19]:


sn.catplot(x = 'age', y = 'marks', data = data1, hue = 'internet')


# # Box plot

# In[20]:


sn.catplot(x = 'age', y = 'marks', data = data1,kind = 'box', hue = 'internet')


# # Regression Output

# In[21]:


sn.regplot(x = 'marks',y = 'hours', data = data1)


# In[26]:


sn.lmplot(x = 'marks', y='hours', data = data1, hue = 'internet', markers = ['o','x'], palette = 'Set2');


# # Using SNS theme in other graph

# In[29]:


import numpy as np
import matplotlib.pyplot as mp
def sinplot(flip = 1):
    x = np.linspace(0,14,100)
    for i in range(1,10):
        mp.plot(x,np.sin(x+i*.5) * (7 - i) * flip)
sn.set_context("talk")
sinplot()
        


# # End of the Module
# 

# In[ ]:




