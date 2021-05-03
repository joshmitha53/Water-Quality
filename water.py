import numpy as np 
import pandas as pd 
import os
data = pd.read_csv("C:/Users/Admin/Desktop/water quality system/IndiaAffectedWaterQualityAreas.csv",encoding='latin1')
print(data)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data.columns
data['State Name'].unique()
data["State Name"].value_counts()
data['Quality Parameter'].value_counts()
data.describe()
data['Quality Parameter'].groupby(data['State Name']).describe()
data.groupby("State Name").size()
import dateutil
data['date'] = data['Year'].apply(dateutil.parser.parse)
import datetime as dt
data['date'] = pd.to_datetime(data['date'])
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
State_Data = data[['State Name', 'Quality Parameter']]
import sklearn
from sklearn.preprocessing import LabelEncoder
numbers = LabelEncoder()
State_Data['Quality'] = numbers.fit_transform(State_Data['Quality Parameter'])
Group1 = State_Data.groupby(['State Name','Quality Parameter','Quality']).count().reset_index()
Group1
State_Quality_Count = pd.DataFrame({'count' : State_Data.groupby( [ "State Name", "Quality","Quality Parameter"] ).size()}).reset_index()
State_Quality_Count
TAMIL_NADU   =  State_Quality_Count[State_Quality_Count["State Name"] == "TAMIL NADU"]    
ANDHRA_PRADESH = State_Quality_Count[State_Quality_Count["State Name"] == "ANDHRA PRADESH"]
KERALA = State_Quality_Count[State_Quality_Count["State Name"] == "KERALA"]
KARNATAKA = State_Quality_Count[State_Quality_Count["State Name"] == "KARNATAKA"]
GUJARAT = State_Quality_Count[State_Quality_Count["State Name"] == "GUJARAT"]
MAHARASHTRA = State_Quality_Count[State_Quality_Count["State Name"] == "MAHARASHTRA"]
TAMIL_NADU
ANDHRA_PRADESH
KERALA
KARNATAKA
GUJARAT
MAHARASHTRA
plt.figure(figsize=(6,4))
ax = sns.barplot(x="count", y ="Quality Parameter", data = TAMIL_NADU)
ax.set(xlabel='Count')
plt.title("Water Quality Parameter In Tamil Nadu")
plt.figure(figsize=(6,4))
ax = sns.barplot(x="count", y ="Quality Parameter", data = ANDHRA_PRADESH)
ax.set(xlabel='Count')
sns.despine(left=True, bottom=True)
plt.title("Water Quality Parameter In Andhra Pradesh")
plt.figure(figsize=(6,4))
ax = sns.barplot(x="count", y ="Quality Parameter", data = KARNATAKA)
ax.set(xlabel='Count')
plt.title("Water Quality Parameter In Karnataka")
plt.figure(figsize=(6,4))
ax = sns.barplot(x="count", y ="Quality Parameter", data = KERALA)
ax.set(xlabel='Count')
plt.title("Water Quality Parameter In Kerala")
plt.figure(figsize=(6,4))
ax = sns.barplot(x="count", y ="Quality Parameter", data = GUJARAT)
ax.set(xlabel='Count')
plt.title("Water Quality Parameter In Gujarat")
plt.figure(figsize=(6,4))
ax = sns.barplot(x="count", y ="Quality Parameter", data = MAHARASHTRA)
ax.set(xlabel='Count')
plt.title("Water Quality Parameter In Maharashtra")
x = State_Quality_Count.groupby('State Name')
plt.rcParams['figure.figsize'] = (9.5, 6.0)
genre_count = sns.barplot(y='Quality Parameter', x='count', data=State_Quality_Count, ci=None)
plt.show()
