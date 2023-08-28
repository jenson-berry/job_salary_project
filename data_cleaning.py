# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:55:08 2023

@author: Jenson
"""


import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')
#Data cleaning tasks
#Location - separate state
#Company founded date to age
#Parse job description (skills/technologies etc)
#Check for missing / null values in salary column

#drop first unnamed column
df= df.drop(['r'], axis=1)

#--------- DATA CLEANING ----------------#

#1. SALARY PARSING

#Create a column to identify job postings with an hourly pay given
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
#Create a column to identify job postings with an 'employer provided salary'
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

#Remove invalid entries
df = df[df['Salary Estimate'] != '-1']
#Remove (Glassdoor est)
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
#Remove dollar sign and 'K@
remove_kd = salary.apply(lambda x: x.replace('K','').replace('$',""))

remove_hr = remove_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

#Get minimum salary of position and store to new column 'min_salary'
df['min_salary'] = remove_hr.apply(lambda x: int(x.split('-')[0]))
#Get maximum salary of position and store to new column 'max_salary'
df['max_salary'] = remove_hr.apply(lambda x: int(x.split('-')[1]))
#Get average salary of position and store to new column 'avg_salary'
df['avg_salary'] = (df.min_salary+df.max_salary) / 2


#2. COMPANY NAME
#Looking at the data, all companies that have ratings follow the same format. The last three characters of the company
#name make up the rating

df['company_text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)


#3. SEPARATE STATE FIELD
#The state is located in the Location column. There are two parts to this (city name / location) and state. 
#The state always comes second so we just need to split the column after the comma.

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])

df.job_state.value_counts()

#Check if job is at company HQ
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)

#4. AGE OF COMPANY
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2023-x)

#5. PARSE JOB DESCRIPTIONS
df['Job Description'][0]

#Tools:
#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['python_yn'].value_counts()


#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['excel_yn'].value_counts()


#r studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df['R_yn'].value_counts()


#spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['spark_yn'].value_counts()

#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['aws_yn'].value_counts()


df.to_csv('salary_data_cleaned.csv',index=False)

pd.read_csv('salary_data_cleaned.csv')
