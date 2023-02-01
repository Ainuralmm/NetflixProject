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


#THIRD PART. DATA CLEANING
# Cleaning "DIRECTOR" column
#so now I show how much the number of null values of 'director' column
print(netflix_df['DIRECTOR'].isnull().sum())
#here is removing rows containing null values of 'director' column 
netflix_df.dropna(subset=['DIRECTOR'], inplace=True)
#filling missing values as 'Unknown'
netflix_df['DIRECTOR'] = netflix_df['DIRECTOR'].fillna('Unknown')
#returning a final result of null values in coulmn
print(netflix_df['DIRECTOR'].isnull().sum())
#returning a final result of notnull values in column
print(netflix_df['DIRECTOR'].notnull().sum())
#checking null values with .info method
print(netflix_df.info())
#summing up null values with  .isnull method in all dataset
print(netflix_df.isnull().sum())


#Cleaning "CAST" column
#so now for cleaning "Cast" column I will do same actions like above
print(netflix_df['CAST'].isnull().sum())
#removing rows containing null values of 'director' column 
netflix_df.dropna(subset=['CAST'], inplace=True)
#filling missing values as 'Unknown'
netflix_df['CAST'] = netflix_df['CAST'].fillna('unknown')
#returning a final result of null values in column
print(netflix_df['CAST'].isnull().sum())
#checking null values with .info method
print(netflix_df.info())
#summing up null values with  .isnull method in all dataset
print(netflix_df.isnull().sum())


#Cleaning "COUNTRY" column
#so I will do same actions like above
print(netflix_df['COUNTRY'].isnull().sum())
netflix_df.dropna(subset=['COUNTRY'], inplace=True)
netflix_df['COUNTRY'] = netflix_df['COUNTRY'].fillna('unknown')
print(netflix_df['COUNTRY'].isnull().sum())
print(netflix_df['COUNTRY'].notnull().sum())
print(netflix_df.info())
print(netflix_df.isnull().sum())


#Cleaning "DURATION" column
#THe Cleaning of "DURATION" column will be little bit different. I will fill null values with mean values in duration columns
print(netflix_df['DURATION'].isnull().sum())
#as usually next I will drop null values
netflix_df.dropna(subset=['DURATION'], inplace=True)
#and now before fill with mean values i should remove all strings in "duratiom"column
netflix_df['DURATION'] = netflix_df['DURATION'].str.replace(r'\D', '')
#so finally filling with mean values
netflix_df['DURATION'].fillna(netflix_df['DURATION'].mean(), inplace=True)
#next steps are same like above
print(netflix_df['DURATION'].isnull().sum())
print(netflix_df['DURATION'].notnull().sum())
print(netflix_df.info())
print(netflix_df.isnull().sum())


#FOURTH PART. MORE EXPLORATION for Data Vizualiziotion
#to show correlation I should change a type of 'duration' column to float
netflix_df['DURATION']=np.float64(netflix_df['DURATION'])
print(netflix_df.head())
#correlation only between 2 columns, bcs other columns are strings
print(netflix_df.corr())
#number of movies and tv-shows in dataset
print(netflix_df.GENRE.value_counts())
#top 10 contries which create contets
top_10_countries = netflix_df['COUNTRY'].value_counts()[0:10]
print(top_10_countries)
#another way to show top 10 contries which create content
print(netflix_df.COUNTRY.value_counts().head(10))
#the last 10 countires which create content
print(netflix_df.COUNTRY.value_counts().tail(10))
#the amount of content was created first 15 years
print(netflix_df.RELEASE_YEAR.value_counts().head(15))
#the amount of content was created last 15 years
print(netflix_df.RELEASE_YEAR.value_counts().tail(15))
#top 10 directors who create content
top_10_directors = netflix_df['DIRECTOR'].value_counts()[0:10]
print(top_10_directors)
#the last 10 directors which create content
print(netflix_df.DIRECTOR.value_counts().tail(10))
#10 films of frequent duration in dataset
print(netflix_df.DURATION.value_counts().head(10))
#10 movies of rare duration
print(netflix_df.DURATION.value_counts().tail(10))
#the 10 most popular genres in dataset
print(netflix_df.LISTED_IN.value_counts().head(10))
#the most popular actors.but result is not correct bcs of comma in some rows
print(netflix_df.CAST.value_counts().head(10))
#so to get clear info about the 10 most popular i should to remove comma
most_popular_10_actors = pd.concat([pd.Series(i.split(',')) for i in netflix_df.CAST]).value_counts().head(10)
print(most_popular_10_actors)
#dataframe where are showed only movies
netflix_movie = netflix_df['GENRE']=='Movie'
print(netflix_df[netflix_movie])
#10 years with the highest total film releases
highest_movie_releases=netflix_df[netflix_movie]['RELEASE_YEAR'].value_counts()[0:10]
highest_movie_releases.name=None
print(highest_movie_releases)
#tv-shows dataframe 
netflix_tvshows = netflix_df['GENRE']=='TV Show'
print(netflix_df[netflix_tvshows])
#5 years with the highest total tv-shows releases
print(netflix_df[netflix_tvshows]['RELEASE_YEAR'].value_counts()[0:5])