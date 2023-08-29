# job_salary_project
Repo for my data science project on job salary predictions for data scientists. 

# Resources
## Glassdoor Selenium Web-scraper:



# Salary Estimations for Data Science Jobs - Project Overview:

- Create a tool that estimates the salaries for data scientists (mean squared error of around 10,000 dollars) that can be used for salary negotiation.
- Used selenium to scrape data from Glassdoor
- Used Multiple Linear Regression, Lasso and Random Forest Regression techniques for my MLMs

## Packages and resources used:
**Python Version:**3.7
**Packages:** pandas, numpy, matplotlib, seaborn, sklearn, selenium, pickle
** Glassdoor Selenium Webscraper:** https://mersakarya.medium.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905.

## Web Scraping:
The web scraping using the Selenium scraper linked above resulted in a .csv with the following columns:
- Job title
- Salary Estimate
- Job Description
- Rating
- Company Name
- Location
- Headquarters location
- Size
- Founded
- Type of industry
- Sector
- Revenue
- Competitors


## Data Cleaning:
I performed a couple of main data-cleaning tasks. All the code for these steps can be found in 'data_cleaning.py'
### Salary Parsing:
- Create a column to identify job postings with an hourly pay given
- Remove invalid entries
- Remove '(Glassdoor est)'
- Remove dollar sign and 'K'
- Find minimum salary of position and store in a new column
- Find maximum salary of position and store in a new column
- Find average salary of position and store in a new column

  ### Company Name:
  Looking at the data, all companies that have ratings follow the same format. The last three characters of the company name make up the rating. We can use this knowledge to read up to the last 3 characters.

  ### Separate State Field:
  The state is located in the Location column. There are two parts to this (city name / location) and state. 
  The state always comes second so we just need to split the column after the comma.



  
