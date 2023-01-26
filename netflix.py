# FIRST PART. Import libries and creating the netflix dataframe 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

netflix_df = pd.read_csv('https://gist.githubusercontent.com/Ainuralmm/3bd1ebbaac091981f031ea47e7b18b61/raw/3132d3a22bdaa9edec8a639a3eae9987d25730bd/gistfile1.txt')
print(netflix_df.head(5))

# SECOND PART. DATA EXPLORATION

# showing netflix dataframe values
print(netflix_df)

# showing first 5 rows of netflix dataframe
print(netflix_df.head())

# showing last 5 rows of netflix dataframe
print(netflix_df.tail())

# showing the size of dataframe (rows, columns)
# netflix_df.shape
print(f'Data has {netflix_df.shape[1]} columns & {netflix_df.shape[0]} rows.')

# getting information like min,max and mean about numeric columns in netflix dataframe
print(netflix_df.describe(include='all'))

#same action like above but transposed
print(netflix_df.describe(include='all').T)

#To get the list of column headers in the netflix dataframe
print(netflix_df.columns)

#to clean the data set to remove a few unnecessary columns 
netflix_df.drop(['show_id','date_added','rating'], axis=1, inplace=True)

#let's return to see the result
print(netflix_df)

#so I removed unneseccery columns and now I want to rename some columns 
netflix_df.rename(columns={'type':'genre', 'title':'movie_title'}, inplace=True)
print(netflix_df.columns)

#now I want to change headings' letters to capital letters
netflix_df.columns = map(str.upper,netflix_df.columns)
print(netflix_df.columns)

# before moving to next cleaning part, I want to show how much the number of missing values in dataset
print(netflix_df.isnull().sum())