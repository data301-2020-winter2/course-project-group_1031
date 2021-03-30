#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


def load_and_process(path): 
    
    data = pd.read_csv(path)
    
    newdf = (   
    pd.DataFrame(data)
    .rename(columns={"alcohol": "Alc"}) #Abbreviating longer column names
    .rename(columns={"free sulfur dioxide": "F.S.D."})
    .rename(columns={"total sulfur dioxide": "T.S.D."})
    .sort_values("quality", ascending=False) #Sorting by wine Quality to answer our research question
    .reset_index(drop=True) #Adjusted Index to match our new sorted dataframe
    )

    return newdf


# In[4]:


def load_and_process2(path):

    df = (
        pd.read_csv(path)
        .rename(columns={"residual sugar":"RS"})
        .rename(columns={"free sulfur dioxide":"Free SO2"})
        .rename(columns={"total sulfur dioxide":"Total SO2"})
        .rename(columns={"fixed acidity":"A (fixed)"})
        .rename(columns={"volatile acidity":"A (volatile)"})
        .sort_values("quality", ascending=False)
        .reset_index(drop=True)
    )
    
    return df


# In[ ]:




