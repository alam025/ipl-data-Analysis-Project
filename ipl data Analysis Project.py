#!/usr/bin/env python
# coding: utf-8

# # ipl data Analysis Project

# In[21]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go;


# In[22]:


data=pd.read_csv((r"C:\Users\alamm\Downloads\IPL 2022.csv.csv"))


# In[23]:


data


# # Number of matches won by each tean in ipl 2022

# In[24]:


figure=px.bar(data,x=data['match_winner'], title="Number of Matches won in ipl 2022")
figure.show()


# In[25]:


data['won_by']=data['won_by'].map({'Wickets':'Chasing','Runs':'Defending'})
won_by=data['won_by'].value_counts()
label=won_by.index
counts=won_by.values
colors=['red','lightgreen']
fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text="Number of matches won by defending or chasing")
fig.update_traces(hoverinfo='label+percent',textinfo='value',textfont_size=30,marker=dict(colors=colors,line=dict(color='black',width=3)))


# In[26]:


figure=px.bar(data,x=data['best_bowling'],title='Best Bowler in IPL 2022')
figure.show()


# In[30]:


figure=px.bar(data,x=['player_of_the_match'],title='Most Player of the Match Award in IPL 2022')
figure.show()


# # top Scorer in IPL 2022

# In[32]:


figure=px.bar(data,x=data['top_scorer'],y=data['highscore'],color=data['highscore'],title="Top Scorers in IPL 2022")
figure.show()


# In[33]:


figure=px.bar(data,x=['toss_winner'],title='Most team toss winner in ipl 2022')
figure.show()


# In[ ]:




