#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:51:10 2023

@author: mac
"""

import matplotlib.pyplot as plt
import pandas as pd


def pieplot(data, title, labels, figure_size=None):
    """ Function to create a pie_plot. Arguments:
        "data": Data to be used to create a plot
        "title": "Title of the pie plot",
        Optional "figure_size" argument to change the sixe of plot.
        It can be a source of hard to find errors.
    """

    plt.figure(figsize=figure_size)

    plt.title(title)

    plt.pie(data, autopct='%1.1f%%', labels=labels)

    plt.legend(loc="best")

    # save as png
    plt.savefig("pie_plot.png")
    plt.show()
    return


plot_title = "Population of world with respect to continents"
df = pd.read_csv('world_population.csv')

total_population = df['2022 Population'].sum()

pop_by_continent = df.groupby(
    'Continent')['2022 Population'].sum().reset_index()

pieplot(pop_by_continent['2022 Population'],
        plot_title, pop_by_continent['Continent'], (12, 12))
