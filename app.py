import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("NetFlix Project")
st.header('FIRST PART')

# preparing the dataset
df = pd.read_csv('https://gist.githubusercontent.com/Ainuralmm/3bd1ebbaac091981f031ea47e7b18b61/raw/3132d3a22bdaa9edec8a639a3eae9987d25730bd/gistfile1.txt')
my_df = pd.DataFrame(df)
# showing first 5 rows of netflix dataframe
st.subheader("Df head")
st.dataframe(my_df.head())

# showing last 5 rows of netflix dataframe
st.subheader("Df tail")
st.dataframe(my_df.tail())

# showing the size of dataframe (rows, columns)
# netflix_df.shape
st.subheader('The size of dataframe (rows, columns)')
st.text(f'Data has {my_df.shape[1]} columns & {my_df.shape[0]} rows.')

# getting information like min,max and mean about numeric columns in netflix dataframe
st.subheader('Information about min,max and mean numeric columns in netflix dataframe')
st.dataframe(my_df.describe(include='all'))

# Transposed description like above
st.subheader('Transposed description')
st.dataframe(my_df.describe(include='all').T)

#To get the list of column headers in the netflix dataframe
st.subheader('The list of column headers')
st.text(my_df.columns)

#to clean the dataset I remove a few unnecessary columns 
st.subheader('Removing a few unnecessary columns with below code')

with st.echo():
    my_df.drop(['show_id','date_added','rating'], axis=1, inplace=True)

#my_df.drop(['show_id','date_added','rating'], axis=1, inplace=True)

#let's return to see the result
st.subheader ('Let`s return the dataframe to see the result by clicking the button')
if st.button('Get a result'):
    st.dataframe(my_df.head(10))

#so I removed unneseccery columns and now I want to rename some columns 
st.subheader('Renaming "type","title" columns with rename method')
my_df.rename(columns={'type':'genre', 'title':'movie_title'}, inplace=True)
st.text(my_df.columns)

#now I want to change headings' letters to capital letters
st.subheader('Changing columns` headings to capital letters')
my_df.columns = map(str.upper, my_df.columns)
st.text(my_df.columns)

# before moving to next cleaning part, I want to show how much the number of missing values in dataset
st.subheader('Before moving next cleaning part, let`s see how many the numbers of missing values ')
if st.button('Get missing values'):
    st.text(my_df.isnull().sum())



#THIRD PART. DATA CLEANING
st.header('SECOND PART. DATA CLEANING')
# Cleaning "DIRECTOR" column
#so now I show how much the number of null values of 'director' column
st.subheader('Cleaning "DIRECTOR" column')
st.text("Initially the number of null values of 'director' column")
st.text(my_df['DIRECTOR'].isnull().sum())

#here is removing rows containing null values of 'director' column 
st.subheader('Dropping null values and filling with the string "Unknown"')
my_df.dropna(subset=['DIRECTOR'], inplace=True)
#filling missing values as 'Unknown'
my_df['DIRECTOR'] = my_df['DIRECTOR'].fillna('Unknown')

#returning a final result of null values in column
st.text("After cleaning the number of null values in'director' column")
st.text(my_df['DIRECTOR'].isnull().sum())

#returning a final result of notnull values in column
st.text('Returning a final result of notnull values in column')
st.text(my_df['DIRECTOR'].notnull().sum())

#checking null values with .info method
st.text('Checking null values with .info method')
st.text(my_df.info())
#summing up null values with  .isnull method in all dataset
st.text('Summing null values up with  .isnull method in all dataset')
st.text(my_df.isnull().sum())
st.text('So the cleaning of left columns will be same')

#Cleaning "CAST" column
#removing rows containing null values of 'director' column 
my_df.dropna(subset=['CAST'], inplace=True)
#filling missing values as 'Unknown'
my_df['CAST'] = my_df['CAST'].fillna('unknown')
#returning a final result of null values in column

#Cleaning "COUNTRY" column
#so I will do same actions like above
my_df.dropna(subset=['COUNTRY'], inplace=True)
my_df['COUNTRY'] = my_df['COUNTRY'].fillna('unknown')

#Cleaning "DURATION" column
#THe Cleaning of "DURATION" column will be little bit different. I will fill null values with mean values in duration columns
#as usually next I will drop null values
my_df.dropna(subset=['DURATION'], inplace=True)
#and now before fill with mean values i should remove all strings in "duratiom"column
my_df['DURATION'] = my_df['DURATION'].str.replace(r'\D', '')
#so finally filling with mean values
my_df['DURATION'].fillna(my_df['DURATION'].mean(), inplace=True)

st.subheader('Click a button to get a final result')
if st.button('Get final numbers of null values in dataframe'):
    st.text(my_df.isnull().sum())

#FOURTH PART. MORE EXPLORATION for Data Vizualiziotion
#to show correlation I should change a type of 'duration' column to float
netflix_df = my_df.copy()

netflix_df['DURATION']=np.float64(netflix_df['DURATION'])
#correlation only between 2 columns, bcs other columns are strings
print(netflix_df.corr())

#top 10 directors who create content
top_10_directors = netflix_df['DIRECTOR'].value_counts()[0:10]

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

#FIFTH PART.DATA VISUALIZATION
#so first I will show a correlation between 2 columns
netflix_df = my_df.copy()
netflix_df['DURATION']=np.float64(netflix_df['DURATION'])

#correlation only between 2 columns, bcs other columns are strings
st.subheader('Correlation Matrix between 2 columns')
st.caption('Because other columns are string')
fig, ax = plt.subplots(figsize=(10,6)) # show what happens when you change sizes
sns.heatmap(netflix_df.corr(), annot=True, ax=ax)
st.write(fig)
st.text("As you understand the correlation between 2 colums is very weak")

#another important to provide is number of movies and tv-shows in dataset
st.subheader('Number of movies and tv-shows in dataset')
labels = ['Movie', 'TV-Shows']
fig1, ax1 = plt.subplots(figsize=(8,6))
ax1.pie(netflix_df['GENRE'].value_counts(), labels=labels, autopct='%.2f%%', startangle=90, shadow=True)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

#top 10 contries which create contets
top_10_countries = netflix_df['COUNTRY'].value_counts()[0:10]

st.subheader('Top 10 content creating countries')
fig1, ax1 = plt.subplots(figsize=(10,6))
st.bar_chart(top_10_countries)

#the amount of content was created first 15 years
st.subheader('Amount of content for first 15 years')
fig1, ax1 = plt.subplots(figsize=(12,10))
sns.set(style="whitegrid")
ax = sns.countplot(y="RELEASE_YEAR", data=netflix_df, palette="Set2", order=netflix_df['RELEASE_YEAR'].value_counts().index[0:15])
st.write(fig1)

#the amount of content was created last 15 years
st.subheader('Amount of content for last 15 years')
fig1, ax1 = plt.subplots(figsize=(12,10))
sns.set(style="dark")
ax = sns.countplot(y="RELEASE_YEAR", data=netflix_df, palette="mako", order=netflix_df.RELEASE_YEAR.value_counts().index[-15:])
st.write(fig1)

#top 10 directors who create content
st.subheader('Top 10 directors who create contents')
fig, ax = plt.subplots(figsize=(10,6))
st.bar_chart(top_10_directors)