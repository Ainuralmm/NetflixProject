import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# creating the netflix dataframe 
netflix_df = pd.read_csv('https://gist.githubusercontent.com/Ainuralmm/3bd1ebbaac091981f031ea47e7b18b61/raw/3132d3a22bdaa9edec8a639a3eae9987d25730bd/gistfile1.txt')
print(netflix_df.head(5))

# Data Exploration and Cleaning
# returning netflix dataframe values
print(netflix_df)

# returning first 5 rows of netflix dataframe
print(netflix_df.head())

# returning last 5 rows of netflix dataframe
print(netflix_df.tail())

# returning the size of dataframe (rows, columns)
# netflix_df.shape
print(f'Data has {netflix_df.shape[1]} columns & {netflix_df.shape[0]} rows.')

# getting information like min,max and mean about numeric columns in netflix dataframe
print(netflix_df.describe(include='all'))
