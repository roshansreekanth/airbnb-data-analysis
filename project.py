#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Created on Thu Nov 19 14:18:40 2020

@Student name: Roshan Sreekanth

@Student ID: R00170592

@Student Course Name: SDH3-B Bsc(Hons) Software Development

"""

def task1():
    df = pd.read_csv('us-Hotel.csv')

    average = df['price'].mean()
    group_one = df[df['price'] <= average]
    group_two = df[df['price'] > average]
    
    group_one_average = group_one['price'].mean()
    group_a = group_one[group_one['price'] <= group_one_average]
    group_b = group_one[group_one['price'] > group_one_average]

    group_two_average = group_two['price'].mean()
    group_c = group_two[group_two['price'] <= group_two_average]
    group_d = group_two[group_two['price'] > group_two_average]

    groups = ["Group A", "Group B", "Group C", "Group D"]
    sizes = [len(group_a), len(group_b), len(group_c), len(group_d)]
    
    bar = plt.bar(groups, sizes)

    for i, value in enumerate(sizes):
        percentage = round((value/sum(sizes))*100, 2)
        plt.text(i, value/2, str(percentage) + "%", ha="center")
    
    smallest_bar =  bar[sizes.index(min(sizes))]
    smallest_bar.set_color("red")
    plt.annotate("Smallest Value", (smallest_bar.get_x(), smallest_bar.get_height() * 1.5))

    plt.title("Group Sizes Based on Average Price")
    plt.xlabel("Group Name")
    plt.ylabel("Group Size")
    plt.show()

'''
Group A has the largest number of accomodations, and Group D has the smallest number of accomodations.

76.84% of accomodations are above the average price and 23.15% of accomodations are lesser than or equal to the average price.
This tells us that there are more houses with above average prices than there are houses with below average prices.

In the costlier bracket, more houses are priced at an above-average premium. In the budget bracket, less houses are present 
in the below-average bracket.

We can infer that hosts prefer to charge more for their accomodations.
'''
def task2():
    df = pd.read_csv('us-Hotel.csv')

    host_details = df.groupby("host_id")["host_name"].value_counts().nlargest(20)
    no_of_accomodations = host_details.values

    plt.bar([str(x[0]) + "\n" + x[1] for x in host_details.keys()], no_of_accomodations) # Where x[0] is the host_id and x[1] is the host_name
    
    for i, value in enumerate(no_of_accomodations):
        percentage = round((value/sum(no_of_accomodations)) * 100, 2)
        plt.text(i, value/2, str(percentage) + "%", ha="center")

    plt.title("Hosts that own the highest number of accomodation")
    plt.xlabel("Host ID and Name")
    plt.ylabel("Accomodations owned")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
'''
Zeus has the most number of listings, followed by Blueground.
The top two hosts own more property than the bottom 10 (31.27% vs 30.28%).
The top 5 hosts own more than half (51.08%) of popular listings.
There is an unequal distribution in regards to the number of accomodations owned.
'''
def task3():
    df = pd.read_csv('us-Hotel.csv')
    cheaper_price = df[df['price'] < 500]
    price_list = cheaper_price['price'].tolist()

    plt.hist(price_list, 35, ec="black")
    plt.title("Frequency distribution of accomodation prices cheaper than 500")
    plt.xlabel("Prices")
    plt.ylabel("Frequency")
    plt.show()
'''
The prices cluster towards the lower range. The most common price is $100, and 
the lowest occuring price is around $9. Prices appear to cluster around the $90 to $150 range.
The histogram is right-skewed, as the frequency goes down as the price gets higher. 
'''
def task4():
    df = pd.read_csv('us-Hotel.csv')

    cheaper_price = df[(150 <= df['price']) & (df['price'] <= 500)]
    price_list = cheaper_price['price'].value_counts()

    plt.plot(price_list.keys(), price_list.values, 'ro')
    plt.title("Visualizing outliers in the price range")
    plt.xlabel("Prices")
    plt.ylabel("Frequency")
    plt.show()

'''
The biggest outlier lies at $150, with almost 5700 values.
At the upper ranges, $500 is an outlier that occurs more frequently.
There are spikes in batches of $50, so we can infer that it is the preferred pricing range ($150 - $200 - $250) 
'''
def task5():
    df = pd.read_csv('us-Hotel.csv')
    rooms = df.groupby("room_type")
    price_means = rooms["price"].mean()
    
    means = price_means.values
    means = [round(x, 2) for x in means]

    explode = [0.0] * len(price_means)
    explode[means.index(min(means))] = 0.3

    pie = plt.pie(price_means, labels= price_means.keys(), autopct = "%1.2f%%", explode = explode)

    plt.title("Average Price of Each Accomodation Type")
    plt.annotate("Lowest Average Price", pie[0][means.index(min(means))].center, weight="bold") # Places comment above the smallest wedge
    plt.legend(means, title="Average Price")
    plt.show()
'''
Hotel rooms are the room type with the highest average price of $281.10.
Shared rooms are the room type with the lowest average price of $73.98.
An entire home/apt is on average 3.6% cheaper than a hotel room but costlier than a private room,
which in itself is 30.7% cheaper than a shared room.
'''

if __name__ == "__main__":
    task5()