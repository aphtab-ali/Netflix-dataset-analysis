import pandas as pd

df = pd.read_csv("dataset/netflix_titles.csv")
print(df.columns.tolist())
print(df.head())

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.duplicated().sum())

df.fillna("Unknown", inplace=True)

df.drop_duplicates(inplace=True)

movies = df[df["type"]=="Movie"]

print(len(movies))

shows = df[df["type"]=="TV Show"]

print(len(shows))

print(df["rating"].value_counts())

print(df["country"].value_counts().head(10))

print(df["director"].value_counts().head(10))

print(df["release_year"].value_counts().head(10))

print(df["listed_in"].value_counts().head(10))

import matplotlib.pyplot as plt

df["type"].value_counts().plot(kind="bar")

plt.title("Movies vs TV Shows")

plt.show()

df["rating"].value_counts().plot(kind="bar")
plt.show()

df["country"].value_counts().head(10).plot(kind="bar")
plt.show()

df["release_year"].value_counts().head(10).plot(kind="bar")
plt.show()

import seaborn as sns

sns.countplot(data=df,x="type")

plt.show()

df.to_csv("Netflix_Cleaned.csv", index=False)
print("Clean dataset saved successfully!")
