# Data Engineering Capstone Project

## Step 1: Project Summary

Identify the data (see below) you'll be using for your project (at least two sources from below and more than 1 million rows).
The objective of this project is explained in the following summary
sections, Step 2 to 5: 

* I94 Immigration Data: This data comes from the US National Tourism and Trade Office. A data dictionary is included in the workspace. This is where the data comes from, https://www.trade.gov/national-travel-and-tourism-office. There's a sample file so you can take a look at the data in csv format before reading it all in. You do not have to use the entire dataset, just use what you need to accomplish the goal you set at the beginning of the project.

* World Temperature Data: This dataset came from Kaggle. You can read more about it here, https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data. 

* U.S. City Demographic Data: This data comes from OpenSoft. You can read more about here, https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/

* Airport Code Table: This is a simple table of airport codes and corresponding cities. It comes from here, https://datahub.io/core/airport-codes#data

 
Here are the modeling steps: 

## Step 2: Explore and assess the data 
    * Explore the data to identify data quality issues, like missing values, duplicate data, etc.
    * Document steps necessary to clean the data
    
## Step 3: Define the Data Model
    * Map out the conceptual data model and explain why you chose that model
    * List the steps necessary to pipeline the data into the chosen data model
    
## Step 4: Run ETL to Model the Data
    * Create the data pipelines and the data model
    * Include a data dictionary
    * Run data quality checks to ensure the pipeline ran as expected
    * Integrity constraints on the relational database (e.g., unique key, data type, etc.)
    * Unit tests for the scripts to ensure they are doing the right thing
    * Source/count checks to ensure completeness

## Step 5: Complete Project Write Up
    * What's the goal? 
    * What queries will you want to run? 
    * How would Spark or Airflow be incorporated? Why did you choose the model you chose?
    * Clearly state the rationale for the choice of tools and technologies for the project.
    * Document the steps of the process.
    * Propose how often the data should be updated and why.
    * (optional) Post your write-up and final data model in a GitHub repo.
    * Include a description of how you would approach the problem differently under the following scenarios:
        * If the data was increased by 100x.
        * If the pipelines were run on a daily basis by 7am.
        * If the database needed to be accessed by 100+ people.

## Data and Code
Still working on the text

## Prerequisites
* AWS EMR cluster
* Apache Spark
* configparser
python 3 is needed to run the python scripts.

## Acknowledgements: 
* Udacity mentors and instructors
