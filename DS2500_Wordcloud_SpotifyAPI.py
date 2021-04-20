# -*- coding: utf-8 -*-
"""
DS2500
April 9th 
Joselyn Huaman
"""
import sys
import wordcloud as wc
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import seaborn as sns
import math

PLAYLISTID = ['37i9dQZF1DXcBWIGoYBM5M', '37i9dQZEVXbMDoHDwVN2tF', '37i9dQZF1DX0XUsuxWHRQd', '37i9dQZF1DX10zKzsJ2jva', '37i9dQZF1DWY7IeIP1cdjF',
              '37i9dQZF1DWWMOmoXKqHTD', '37i9dQZF1DX4o1oenSJRJd', '37i9dQZF1DWXRqgorJj26U', '37i9dQZF1DX4UtSsGT1Sbe', '37i9dQZF1DX76Wlfdnj7AP',
              ]

def CleanFile(file):
    
    GenreData = file[['Month','Artist', 'Genre 1', 'Genre 2', 'Genre 3', 'Genre 4']]
    
    return GenreData

def VisualiseTopArtist(df):
    
    Sort_Artist = df.groupby(['Month']).Artist.value_counts().sort_values(ascending=False)
    ArtistperMo = Sort_Artist.rename('Count')
    ArtistperMo = ArtistperMo.groupby('Month').head(3)
    ArtistperMo = ArtistperMo.to_frame()
    ArtistperMo = ArtistperMo.reset_index()
    #ArtistperMo = ArtistperMo.reset_index(0)
    
   # fig, ax = plt.subplots()
    fg = sns.barplot(data= ArtistperMo, x = ArtistperMo.Month , y='Count', 
                     hue= ArtistperMo.Artist, width = 1)

    return ArtistperMo

if __name__ == "__main__":
    
    Compilation2019 = pd.read_csv('TopGenres2019.csv', header = 0)
    Compilation2020 = pd.read_csv('TopGenres2020.csv', header = 0) 
    
    # Clean data
    Genre2019 = CleanFile(Compilation2019)
    Genre2020 = CleanFile(Compilation2020)
    
    # Visualise Top 3 Artists
    VisualiseTopArtist(Genre2019)

    
    
    # Mean by month of all song attributes
 #   Mean_by_month = Top200Songs.groupby(by = ['Month']).mean()
    # Mean_by_month = Mean_by_month.reset_index()
    
    # Visualisation of Top 200 attributes
    # Monthly = sns.barplot(data=Top200Songs, x="Month", y="Instrumentalness")
    # Monthly = sns.displot(data=Top200Songs, x="Acousticness")
#    Heatmap = sns.heatmap(Mean_by_month.corr(), cmap="coolwarm")

    