#!/usr/bin/env python
# coding: utf-8

# #**Electric Vehicles Market Size Analysis using Python**

# In[4]:

#Introduction
'''The adoption of electric vehicles (EVs) is rapidly increasing as governments, industries, and consumers shift towards more sustainable modes of transportation. Understanding the trends in EV title and registration activities is crucial for policymakers, manufacturers, and infrastructure planners. This case study leverages data from Data.gov, specifically focusing on electric vehicle title and registration activities across US region. The analysis aims to uncover key insights into the growth patterns, regional distribution, and demographic factors influencing the adoption of electric vehicles. By exploring this dataset, we can gain a deeper understanding of the evolving landscape of electric mobility and its implications for the future.'''
#My goal was to forecast the electric vehicle (EV) market growth over the next five years using this data. This prediction will enable manufacturers and infrastructure planners to allocate resources effectively and develop targeted marketing strategies, with the aim of boosting EV registrations in regions where adoption is currently low.

#Ask Phase
#This analysis focuses on leveraging electric vehicle (EV) title and registration data to forecast market growth and guide strategic decisions. The primary goal is to extract valuable insights into EV adoption trends, regional distribution, and consumer preferences. By identifying key patterns and growth opportunities in the EV market, I aim to provide actionable recommendations for manufacturers and infrastructure planners, ensuring their strategies align with current and future market demands.
#The 4 key Business Tasks:

'''1. Analyze EV Adoption Over Time:

Examine historical data to assess the growth trends of electric vehicle (EV) registrations by model year. Identify patterns and shifts in adoption rates over different years to forecast future growth.

2. Assess Geographical Distribution:

Map the distribution of EV registrations by geographic regions (e.g., counties or cities) to understand regional adoption rates. Determine which areas have higher concentrations of EVs and identify regions with potential for growth.

3. Categorize EV Types:

Break down the dataset by electric vehicle types (e.g., Battery Electric Vehicles (BEVs), Plug-in Hybrid Electric Vehicles (PHEVs)) to understand the market share of different EV categories. Analyze trends in consumer preferences for specific types of EVs.

4. Evaluate Make and Model Popularity:

Identify the most popular makes and models of electric vehicles from the registration data. Determine which manufacturers and models are leading in the market and how their popularity has evolved over time.

5. Analyze Electric Range:

Assess the electric range of various EV models to gauge advancements in EV technology. Analyze how improvements in range are influencing consumer choices and market dynamics.

6. Estimate Growth in Market Size:

Calculate the estimated growth in the market size of electric vehicles based on historical data and current trends. Develop forecasts for future market expansion and identify key drivers of growth.'''

#Data Source
#For this analysis, I used the public dataset "Electric_Vehicle_Title_and_Registration_Activity" available on DATA.GOV, which contains 1,079,230 records. The dataset includes information such as Clean Alternative Fuel Vehicle Type, DOL Vehicle Type, Model Year, Make, Model, Electric Range, County, City, Sales Date, and Sales Price. These data points provide a comprehensive view of electric vehicle registrations and characteristics, offering valuable insights to inform market growth forecasts and strategic planning for the EV industry.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:

# Next we import the 
EVdata = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')


# In[6]:


EVdata.info()


# In[7]:


EVdata.isnull().sum()


# In[8]:


EVdata.dropna(inplace = True)


# In[9]:


EVdata.isnull().sum()


# In[75]:


# EV Adoption Over Time
EV_adoption_by_year = EVdata['Model Year'].value_counts()
EV_adoption_by_year


# In[78]:


plt.figure(figsize = (10,8))
sns.barplot(x = EV_adoption_by_year.index, y = EV_adoption_by_year.values, palette = 'viridis')
plt.xlabel("Year")
plt.ylabel("Number of vehicles registered")
plt.title('EV Adoption Over Time')
plt.xticks(rotation = 45)
plt.show()


# In[10]:


EVdata['County'].value_counts()


# In[11]:


Distribution = EVdata.groupby(['County', 'City']).size().sort_values(ascending=False).reset_index(name='Count').head(10)
Distribution 


# #To Plot the graph

# In[80]:


plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Count', hue = 'County',data = Distribution, palette='viridis')
plt.xlabel('City')
plt.ylabel('Count')
plt.title("Top 10 Cities with the Highest Number of EV's")
plt.xticks(rotation=45)
plt.show()


# In[13]:


Vehicle_type = EVdata['Clean Alternative Fuel Vehicle Type'].value_counts()
print(Vehicle_type)
EVdata['Clean Alternative Fuel Vehicle Type'].unique()


# In[14]:


plt.figure(figsize=(10, 6))
plt.pie(Vehicle_type, labels= Vehicle_type.index, autopct='%1.1f%%', startangle= 130)

# Add title
plt.title('Vehicle types')

# Show the plot
plt.show()


# In[15]:


#popularity of electric vehicle manufacturers and models among the registered vehicles


# In[16]:


#So, let’s have a look at the most popular manufacturers and then drill down into the most popular models within those manufacturers:


# In[17]:


Top_manufacturers = EVdata['Make'].value_counts().head(10)
Top_manufacturers


# In[18]:


plt.figure(figsize = (10,6))
sns.barplot(x = Top_manufacturers.values, y = Top_manufacturers.index, palette = "cubehelix")
plt.title('Top 10 popular manufacturers')
plt.xlabel("Number of Vehicles Registered")
plt.ylabel("Make")
plt.tight_layout()
plt.show()


# In[19]:


# Now lets find out top sold models from the popular manufacturers
#Selecting the top 5 manufacturers based on the number of vehicles registered


# In[20]:


Top_5_manufacturers = Top_manufacturers.head(5).index
Top_5_manufacturers


# In[21]:


Top_5_Productions_df = EVdata[EVdata['Make'].isin(Top_5_manufacturers)]
Top_5_Productions_df


# In[22]:


Top_models = Top_5_Productions_df.groupby(['Make','Model']).size().sort_values(ascending = False).reset_index(name = 'Count').head(10)
Top_models


# In[23]:


plt.figure(figsize = (12,8))
sns.barplot(x = 'Count', y = 'Model', hue = 'Make',data = Top_models, palette = "viridis")
plt.xlabel('Number of vehicles registered')
plt.ylabel('Model')
plt.title('Top models by top 5 manufacturers')

plt.show()


# In[24]:


plt.figure(figsize =(12,6))
sns.histplot(EVdata['Electric Range'],bins = 20, kde= True, color = 'royalblue')
plt.title('Distribution of Electric Vehicle Ranges')
plt.xlabel("Electric Range(miles)")
plt.ylabel("Number of vehicles") 
plt.axvline(EVdata['Electric Range'].mean(), color = 'red', linestyle ='--', label = f'Mean Range: {EVdata["Electric Range"].mean():.2f} miles')
plt.legend()
plt.show()


# In[25]:


#Calculate the average electric range by model year


# In[28]:


Avg_EV_range = EVdata.groupby('Model Year')['Electric Range'].mean().reset_index(name = 'Avg_range')
Avg_EV_range


# In[29]:


plt.figure(figsize = (12,8))
sns.lineplot(x = 'Model Year', y = 'Avg_range', data = Avg_EV_range, marker = 'o', color = 'Green')
plt.xlabel('Model Year')
plt.ylabel('Average EV range(miles)')
plt.title('Average EV Range by Model year')
plt.show()


# In[30]:


avg_range_by_manufacturers = Top_5_Productions_df.groupby(['Make','Model'])['Electric Range'].mean().sort_values(ascending = False).reset_index(name = 'Range in miles')
avg_range_by_manufacturers


# In[31]:


Top_range_models = avg_range_by_manufacturers.head(10)
Top_range_models 


# In[32]:


plt.figure(figsize = (10,6))
sns.barplot(x = 'Range in miles' , y = 'Model', hue = 'Make',data = Top_range_models, palette = "cool" )
plt.xlabel("Range (miles)")
plt.ylabel("Model name")
plt.title('Top range EV Models by Top Manufacturers')
plt.show()


# In[ ]:


#Estimated market size analysis of EV in US


# In[34]:


# calculate the number of EVs registered each year
EV_registration_counts = EVdata['Model Year'].value_counts().sort_index()
EV_registration_counts


# In[ ]:


#Let's estimate the EV registration vale for the year 2024 and further more 5 years from 2024


# In[36]:


from scipy.optimize import curve_fit


# In[70]:


# filter the dataset to include years with complete data, assuming 2023 is the last complete year
filtered_years = EV_registration_counts[EV_registration_counts.index < 2024]
filtered_years


# In[71]:


# define a function for exponential growth to fit the data
def exp_growth(x, a, b):
    return a * np.exp(b * x)

# prepare the data for curve fitting
# here the curve_fit function uses the non-linear least squares to fit a function, f, to data.
x_data = filtered_years.index - filtered_years.index.min()
y_data = filtered_years.values


#Params -> This is an array of the optimized parameters (in this case, a and b) that best fit the data according to the model you provided (exp_growth).
params, covariance = curve_fit(exp_growth, x_data, y_data)
#The covariance matrix is used to assess the accuracy and precision of the fitted parameters obtained from the curve fitting process. 
#It provides valuable information about the potential errors and the correlation between parameters, which is crucial for interpreting the results of the curve fitting and understanding the reliability of the model.
#If the diagonal values are small, it suggests that the fitted parameters are precise; if large, the parameters might have significant uncertainty.
print(params)



# In[72]:


# use the fitted function to forecast the number of EVs for 2024 and the next five years
forecasted_years = np.arange(2024, 2024+6) - filtered_years.index.min()
forecasted_values = exp_growth(forecasted_years, *params)

# create a dictionary to display the forecasted values for easier interpretation
forecasted_growth = dict(zip(forecasted_years + filtered_years.index.min(), forecasted_values))
forecasted_growth


# In[73]:


#let's plot the graph for the above data
years = np.arange(filtered_years.index.min(), 2029+1)
actual_years = filtered_years.index
forecasted_years_full = np.arange(2024, 2029+1)

actual_values = filtered_years.values
forecasted_values_full = [forecasted_growth[year] for year in forecasted_years_full]

plt.figure(figsize = (12,6))
plt.plot(actual_years, actual_values, 'bo-', label = 'Actual Registrations')
plt.plot(forecasted_years_full, forecasted_values_full, 'ro--', label = 'Forecasted Registrations')

plt.title('Current and estimated EV market size')
plt.xlabel("Year")
plt.ylabel("Number of registrations")
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:


#From the above graph, we can see:

#The number of actual EV registrations remained relatively low and stable until around 2010, after which there was a consistent and steep upward trend, suggesting a significant increase in EV adoption.
#The forecasted EV registrations predict an even more dramatic increase in the near future, with the number of registrations expected to rise sharply in the coming years.

