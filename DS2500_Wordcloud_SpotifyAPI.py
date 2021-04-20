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
import plotly.express as px
import altair as alt
from plotnine import *




PLAYLISTID = ['37i9dQZF1DXcBWIGoYBM5M', '37i9dQZEVXbMDoHDwVN2tF', '37i9dQZF1DX0XUsuxWHRQd', '37i9dQZF1DX10zKzsJ2jva', '37i9dQZF1DWY7IeIP1cdjF',
              '37i9dQZF1DWWMOmoXKqHTD', '37i9dQZF1DX4o1oenSJRJd', '37i9dQZF1DWXRqgorJj26U', '37i9dQZF1DX4UtSsGT1Sbe', '37i9dQZF1DX76Wlfdnj7AP',
              ]

def CleanFile(file):
    
    GenreData = file[['Month','Artist', 'Genre 1', 'Genre 2', 'Genre 3', 'Genre 4']]
    
    return GenreData

def TopArtist(df):
    
    Sort_Artist = df.groupby(['Month']).Artist.value_counts().sort_values(ascending=False)
    ArtistperMo = Sort_Artist.rename('Count')
    ArtistperMo = ArtistperMo.groupby('Month').head(3)
    ArtistperMo = ArtistperMo.to_frame().reset_index()
    ArtistperMo = ArtistperMo.sort_values('Month')
    
    return ArtistperMo

if __name__ == "__main__":
    
    Compilation2019 = pd.read_csv('TopGenres2019.csv', header = 0)
    Compilation2020 = pd.read_csv('TopGenres2020.csv', header = 0) 
    
    # Clean data
    Genre2019 = CleanFile(Compilation2019)
    mo_2019 = ['Nov18','Dec18', 'Jan19', 'Feb19', 'Mar19', 'Apr19', 'May19','Jun19', 'Jul19', 
               'Aug19', 'Sep19','Oct19','Nov19','Dec19']
    Genre2020 = CleanFile(Compilation2020)
    mo_2020 = ['Jan20', 'Feb20', 'Mar20', 'Apr20', 'May20','Jun20', 'Jul20', 
               'Aug20', 'Sep20','Oct20','Nov20','Dec20','Jan21','Feb21']
    
    # Visualise Top 3 Artists 
    Top3_2019 = TopArtist(Genre2019)    
    # g <- ggplot(Top3_2019, aes(x='Month', fill='Artist', weight='Count')) + geom_bar() + theme_bw() 
    # g + scale_x_continuous(limits = (0,15), breaks = (1,2,3,4,5,6,7,8,9,10,11,12,13,14),labels = mo_2019) + theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))
    # print(g)
    
    # Top3_2020 = TopArtist(Genre2020)    
    # h = ggplot(Top3_2020, aes(x='Month', fill='Artist', weight='Count')) + geom_bar() + theme_bw() + + scale_x_continuous(limits = (0,15), breaks = (1,2,3,4,5,6,7,8,9,10,11,12,13,14),labels = mo_2020)
    # print(h)
    
    #Get Top Genres 
    gen = []
    
    if Top3_2019['Artist'].reset_index(drop=True) == Genre2019['Artist'].reset_index(drop=True):    
        gen.append(Genre2019['Genre 1'])

    
    # for col in Top3_2019['Artist']:
    #     for all_col in Genre2019:
    #         if col == Genre2019['Artist']:
    #             gen.append(Genre2019['Genre 1'])
            