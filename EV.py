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
#For this analysis, I used the public dataset "Electric_Vehicle_Title_and_Registration_Activity" available on DATA.GOV, which contains 10,79,230 records. The dataset includes information such as Clean Alternative Fuel Vehicle Type, DOL Vehicle Type, Model Year, Make, Model, Electric Range, County, City, Sales Date, and Sales Price. These data points provide a comprehensive view of electric vehicle registrations and characteristics, offering valuable insights to inform market growth forecasts and strategic planning for the EV industry.


#prepare phase

'''Data Storage

The data is stored locally on my computer, organized into a CSV file where all the information is merged in 1 set of file.

Data Organization

The data is organized in wide format, making it easy to work with different variables.'''

'''Bias and Credibility Issues

The data meets the ROCCC criteria—Reliable, Original, Cited, Comprehensive, and Current—making it ideal for exploratory analysis and for predicting the next five years of EV market growth. However, while it provides a strong foundation for forecasting, definitive conclusions should be approached with caution given the evolving nature of the market.'''

#The dataset is publicly accessible and intended for open use, governed by the Open Data Commons Open Database License (ODbL) v1.0. This license allows users to freely share, modify, and utilize the data while ensuring that the same freedoms are preserved for others. The dataset is non-federal, meaning it is subject to different Terms of Use than Data.gov, and it comes with no warranties or legal guarantees. Although the data is provided 'as is' and Open Data Commons disclaims any resulting damages, the dataset is securely hosted and accessible to anyone. 

#I ensured the data’s accuracy by checking for missing values, duplicates, and any inconsistencies. Additionally, I ran basic statistical checks to confirm that the vehicle types, model years, and sales prices were within expected ranges and distributions. This process helped validate the reliability of the data for accurate analysis in the EV market size assessment.

'''Problems with the Data

The data presented significant challenges due to its large size, with over 1,079,229 records. Handling such a massive dataset in Excel was cumbersome, and I faced difficulties loading the entire dataset at once in Colab, leading to potential processing errors and misleading outputs. Additionally, managing and analyzing this extensive data required considerable computational resources, which posed further challenges in ensuring accurate and efficient analysis.
It also had missing values'''

#process phase

'''In this phase, I concentrated on identifying and eliminating inaccuracies through data cleaning and manipulation, including the removal of outliers and converting the data into a more usable format.

I chose Python for data processing and analysis due to its robust statistical and visualization capabilities, extensive libraries for various data tasks, and flexibility in handling large datasets. For this project, I used Jupyter Notebook, which offers a powerful environment for in-depth analysis and clear presentation of insights.

I utilized libraries such as Pandas and NumPy for efficient data manipulation, Matplotlib for plotting graphs, and Seaborn for creating visually appealing and understandable visualizations through bar plots, histograms, and line plots. Additionally, I used curve_fit from the scipy.optimize module to forecast EV registration values, providing a predictive model for the market size analysis.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:

# Next we import the 
EVdata = pd.read_csv('Electric_Vehicle_Title_and_Registration_Activity.csv')


# In[6]:
#So, this data is based on the EV population in the United States. Now, let’s clean the dataset before moving forward:

EVdata.info()


# In[7]:


EVdata.isnull().sum()


# In[8]:


EVdata.dropna(inplace = True)


# In[9]:


EVdata.isnull().sum()


# In[75]:
#Analysis

'''For the task of market size of electric vehicles analysis, we can explore the following areas:

EV Adoption Over Time: Analyze the growth of the EV population by model year.
Geographical Distribution: Understand where EVs are most commonly registered (e.g., by county or city).
EV Types: Breakdown of the dataset by electric vehicle type (BEV, etc.).
Make and Model Popularity: Identify the most popular makes and models among the registered EVs.
Electric Range Analysis: Analyze the electric range of vehicles to see how EV technology is progressing.
Estimated Growth in Market Size: Analyze and find the estimated growth in the market size of electric vehicles.
Let’s start with analyzing the EV Adoption Over Time by visualizing the number of EVs registered by model year. It will give us an insight into how the EV population has grown over the years:'''

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

#Overall, the graph indicates that EV adoption is not uniform across the cities and is more concentrated in certain areas, particularly in King County.
# In[13]:

'''Next, let’s explore the types of electric vehicles represented in this dataset. Understanding the breakdown between different EV types, such as Battery Electric Vehicles (BEV) and Plug-in Hybrid Electric Vehicles (PHEV), can provide insights into consumer preferences and the adoption patterns of purely electric vs. hybrid electric solutions. So, let’s visualize the distribution of electric vehicle types to see which categories are most popular among the registered vehicles:'''

Vehicle_type = EVdata['Clean Alternative Fuel Vehicle Type'].value_counts()
print(Vehicle_type)
EVdata['Clean Alternative Fuel Vehicle Type'].unique()

#Analysis of Electric Vehicle Types

'''The above graph illustrates that Battery Electric Vehicles (BEVs) are significantly more popular than Plug-in Hybrid Electric Vehicles (PHEVs) among the electric vehicles registered in the United States, with BEVs comprising 77.7% of the market compared to 22.3% for PHEVs. Hydrogen Powered Vehicles (HPVs) represent a minimal fraction of the market at 0.0%.'''



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
'''Next, we will examine the popularity of electric vehicle manufacturers and models within this dataset. This analysis aims to identify the leading manufacturers and specific models dominating the EV market. Understanding these preferences can provide insights into consumer behavior, brand loyalty, and the effectiveness of various manufacturers' strategies in advancing electric mobility.'''

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

'''TESLA leads by a substantial margin with the highest number of vehicles registered.
NISSAN is the second most popular manufacturer, followed by CHEVROLET, though both have significantly fewer registrations than TESLA.
FORD, BMW, KIA, TOYOTA, VOLKSWAGEN, HYUNDAI and JEEP follow in decreasing order of the number of registered vehicles.'''

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
'''Next, let’s drill down into the most popular models within these top manufacturers to get a more detailed understanding of consumer preferences at the model level:'''

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
'''Next, we’ll explore the electric range of vehicles, which is a critical factor for analyzing the market size of electric vehicles. The electric range indicates how far an EV can travel on a single charge, and advancements in battery technology have been steadily increasing these ranges over the years. So, let’s look at the distribution of electric ranges in the dataset and identify any notable trends, such as improvements over time or variations between different vehicle types or manufacturers:'''

plt.figure(figsize =(12,6))
sns.histplot(EVdata['Electric Range'],bins = 20, kde= True, color = 'royalblue')
plt.title('Distribution of Electric Vehicle Ranges')
plt.xlabel("Electric Range(miles)")
plt.ylabel("Number of vehicles") 
plt.axvline(EVdata['Electric Range'].mean(), color = 'red', linestyle ='--', label = f'Mean Range: {EVdata["Electric Range"].mean():.2f} miles')
plt.legend()
plt.show()

'''The above graph shows the mean electric range. Key observations from the graph include:

There is a high frequency of vehicles with a low electric range, with a significant peak occurring just before 50 miles.
The distribution is skewed to the right, with a long tail extending towards higher ranges, although the number of vehicles with higher ranges is much less frequent.
The mean electric range for this set of vehicles is marked at approximately 58.84 miles, which is relatively low compared to the highest ranges shown in the graph.
Despite the presence of electric vehicles with ranges that extend up to around 350 miles, the majority of the vehicles have a range below the mean.
It suggests that while there are EVs available with high electric ranges, the average range is skewed lower due to a substantial number of vehicles with shorter ranges.

Now, let’s delve into the trend of electric ranges over model years, which can provide insights into how advancements in battery technology and vehicle design have influenced the electric range capabilities of electric vehicles over time. A positive trend in this analysis would indicate continuous improvements, offering consumers EVs with longer driving ranges and potentially addressing one of the major concerns regarding the EV market (range anxiety):'''

# In[25]:


#Calculate the average electric range by model year


# In[28]:


Avg_EV_range = EVdata.groupby('Model Year')['Electric Range'].mean().reset_index(name = 'Avg_range')
Avg_EV_range


# In[29]:
'''#calculating the average electric range by model year'''

plt.figure(figsize = (12,8))
sns.lineplot(x = 'Model Year', y = 'Avg_range', data = Avg_EV_range, marker = 'o', color = 'Green')
plt.xlabel('Model Year')
plt.ylabel('Average EV range(miles)')
plt.title('Average EV Range by Model year')
plt.show()


# In[30]:
'''The above graph shows the progression of the average electric range of vehicles from around the year 2000 to 2024. Key findings from the graph:

There is a general upward trend in the average electric range of EVs over the years, indicating improvements in technology and battery efficiency.
There is a noticeable peak around the year 2020 when the average range reaches its highest point.
Following 2020, there’s a significant drop in the average range, which could indicate that data for the following years might be incomplete or reflect the introduction of several lower-range models.
After the sharp decline, there is a slight recovery in the average range in the most recent year shown on the graph.
The data suggest that while there have been fluctuations, the overall trend over the last two decades has been toward increasing the electric range of EVs.

Next, let’s explore how electric ranges vary among the top manufacturers and models. This analysis can reveal how different manufacturers are addressing the crucial aspect of electric range and highlight which models stand out for their superior range capabilities:'''

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

'''The TESLA ROADSTER has the highest average electric range among the models listed. TESLA’s models (ROADSTER, MODEL S, MODEL X, and MODEL 3) occupy the majority of the top positions, indicating that on average, TESLA’s vehicles have higher electric ranges. The CHEVROLET BOLT EV is an outlier among the CHEVROLET models, having a substantially higher range than the VOLT and S-10 PICKUP from the same maker. NISSAN’s LEAF and CHEVROLET’s SPARK are in the lower half of the chart, suggesting more modest average ranges.'''

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

'''The dataset provides the number of electric vehicles registered each year from 1997 through 2024. However, the data for 2024 is incomplete as it only contains the data till March. Here’s a summary of EV registrations for recent years:

In 2021, there were 19,063 EVs registered.
In 2022, the number increased to 27708 EVs.
In 2023, a significant jump to 57,519 EVs was observed.
For 2024, currently, 7,072 EVs are registered, which suggests partial data.
To forecast the total number of EVs expected to be registered in 2024, we can use a growth rate based approach from previous complete years.

We’ll calculate the Compound Annual Growth Rate (CAGR) between a recent year with complete data (2023) and an earlier year to project the 2024 figures. Additionally, using this growth rate, we can estimate the market size for the next five years. Let’s proceed with these calculations:'''
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

'''Given the growing trend in actual EV registrations and the projected acceleration as per the forecast data, we can conclude that the EV market size is expected to expand considerably. The steep increase in forecasted registrations suggests that consumer adoption of EVs is on the rise, and this trend is likely to continue. Overall, the data point towards a promising future for the EV industry, indicating a significant shift in consumer preferences and a potential increase in related investment and business opportunities.'''

#Share Phase:

'''So, market size analysis is a crucial aspect of market research that determines the potential sales volume within a given market. It helps businesses understand the magnitude of demand, assess market saturation levels, and identify growth opportunities. From our market size analysis of electric vehicles, we found a promising future for the EV industry, indicating a significant shift in consumer preferences and a potential increase in related investment and business opportunities.'''
