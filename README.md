# US Economic Indicators Data Cleaning & Visualization
*To embed and display my Tableau dashboard, I followed the instructions and used the code of dinkwiz. [Here is a link to the (super useful and well documented) repo!](https://github.com/dinkwiz/tableau_embed/tree/master)*

<iframe align = "center" width = "1000" height = "1000" src="https://public.tableau.com/app/profile/rohan.krishnan4713/viz/USEconomicIndicators_17221171521810/Dashboard1"/>

## Table of Contents
1. [Introduction](#introduction)
2. [Data Collection](#data-collection)
3. [Data Cleaning](#data-cleaning)
4. [Data Visualization](#data-visualization)

## Introduction
The US economy is a large and complex web of indicators, applications, measures, and more. Using data from the St. Louis Federal Reserve (FRED) and the US Census Bureau, I created a Tableau Dashboard to visualize some key economic indicators as well as how they compare to the previous year.

![Dashboard Image](/assets/Dashboard-image.png)

## Data Collection
As I was collecting data, I started with a base economic indicator data set downloaded from the U.S. Census Bureau's [website](https://www.census.gov/economic-indicators/). This data set contained values for indicators like the number of new orders of durable goods, wholesale inventory, retail inventory, etc. I supplemented that information with several key indices and macroeconomic measures downloaded from the St. Louis Federal Reserve's [website](https://fred.stlouisfed.org/). I added measures including Real GDP, unemployment, and median CPI. All data except Real GDP was measured monthly. 

## Data Cleaning
I used python to load in and join each data set. The data from the US Census Bureau only went back to 2004 while the data from the St. Louis Federal Reserve went back to varying dates in the 90's. I decided to left-join all of the FRED data onto my original census data. This resulted in a dataframe starting from July 2004 and running until July 2024. Since GDP was measured quarterly, it contained several null values. However, since I was planning on using Tableau to visualize the data, I decided to leave the null values as is.

## Data Visualization
Using Tableau, I made 4 KPI cards to display the selected year's mean real GDP, federal funds rate, median cpi, and unemployment rate. I used means instead of medians because any outlier values in a year provide important information about the economy that I wanted the average measure to capture. I also created two charts to visualize durable goods and business applications in the selected year. For styling, I used Figma to create a dashboard background including cards with rounded edges. All assets used in the dashboard can be found in the `assets` folder. Finally, I hosted the dashboard using github pages by following [dinkwiz's instructions on github](https://github.com/dinkwiz/tableau_embed/tree/master). You can view the dashboard on GitHub Pages [here](https://r0hankrishnan.github.io/economic-indicators/) or on Tableau Public [here](https://public.tableau.com/app/profile/rohan.krishnan4713/viz/USEconomicIndicators_17221171521810/Dashboard1).
