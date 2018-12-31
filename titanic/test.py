import numpy as np 
import pandas as pd 
import sklearn as sk 

df = pd.read_csv("titanic.csv") # reads in CSV
print(df.head(5), "\n\n\n") # prints first 5 elements of the dataframe
print(df.tail(6), "\n\n\n") # prints the last 6 elements of the dataframe -- good to figure out total number of entries
print(df.describe(), "\n\n\n") # summary statistics of numerical colums -- non- numerical data ignored
print(df.columns, "\n\n\n") # column labels

print(df['sex'], "\n\n\n") # prints the entire sex column
print(df['sex'][:5], "\n\n\n") # prints first 5 of sex column
print(df['sex'][20:40], "\n\n\n") # prints the sex of subjects 20-40

