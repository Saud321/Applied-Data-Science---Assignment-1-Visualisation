#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd


def barplot(x_axis_data, data, title, colors, figure_size=None,
            x_label="x", y_label="y",):
    """ Function to create a barplot. Arguments:
        "x_axis": Data to be represent along x-axis, also used as labels
        "data" argument is the arrays of numbers to show data vertically in
        the form of bar's.
        "title": "Title of the bar plot",
        Optional "figure_size" argument to change the sixe of plot.
        Optional "x_label" argument having default value of "x",
        to customise the label of x-axis.
        Optional "y_label" argument, having default value of "y",
        to customise the label of y-axis
        "x_axis" argument can also used as label 
        It can be a source of hard to find errors.
    """

    plt.figure(figsize=figure_size)

    plt.title(title)

    plt.bar(x_axis_data, data, label=x_axis_data, color=colors)

    # labelling
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.legend()
    
    # save as png
    plt.savefig("barplot.png")
    plt.show()
    return


plot_title = "Population density (people per sq. km of land area)"
df = pd.read_csv('population_data_2020.csv')

countries = df.iloc[:, 2]
colors = ['#B5CA92', '#A47D7C', '#92A8CD', '#DB843D', '#3D96AE',
          '#80699B', '#89A54E', '#AA4643', '#4572A7']

barplot(df.iloc[:, 2], df.iloc[:, 4], plot_title, colors, (20, 10),
        "Countries", "Population in trillions")
