#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd


def lineplot(df, headers, figure_size=None, x_label="x", y_label="y"):
    """ Function to create a lineplot. Arguments:
        A dataframe with a column "x" and other columns to be taken as y.
        Optional "figure_size" argument to change the sixe of plot.
        Optional "x_label" argument having default value of "x",
        to customise the label of x-axis.
        Optional "y_label" argument, having default value of "y",
        to customise the label of y-axis
        A list containing the headers of the columns to plot.
        It can be a source of hard to find errors.
    """

    if (figure_size is None):
        plt.figure()
    else:
        plt.figure(figsize=figure_size)

    for head in headers:
        plt.plot(df["x"], df[head], label=head)

    # labelling
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # removing white space left and right. Both standard and pandas min/max
    # can be used
    plt.xlim(min(df["x"]), df["x"].max())

    plt.legend()
    # save as png
    plt.savefig("linplot.png")
    plt.show()
    return


df = pd.read_csv(
    'property-type-pac-england-from-2000-01-01-to-2023-01-01.csv')

df['Period'] = pd.to_datetime(df['Period'], format='%Y-%m-%d')

period = df.iloc[:, 3]
headers = df.columns.values[7:11]
df['x'] = df['Period']

lineplot(df, headers, (18, 6), "Period", "Change in %age")


