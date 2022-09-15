# import pandas
import pandas as pd
import matplotlib.pyplot as plt

# Carpentries link for gapminder data
data_url = 'http://bit.ly/2cLzoxH'
#load gapminder data from url as pandas dataframe
gapminder = pd.read_csv(data_url)
# print in console first 10 data in csv
print(gapminder.head(10))

	
gapminder_us = gapminder[gapminder.country=="United Kingdom"]
# gapminder_us = gapminder[gapminder.country=="Albania"]


# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot
ax.plot(gapminder_us.year,
        gapminder_us.lifeExp,
        color="red", 
        marker="o")
# set x-axis label
ax.set_xlabel("year", fontsize = 14)
# set y-axis label
ax.set_ylabel("Life Exp",
              color="red",
              fontsize=14)

# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(gapminder_us.year, gapminder_us["gdpPercap"],color="blue",marker="o")
ax2.set_ylabel("GDP Percap",color="blue",fontsize=14)
plt.title('GDP and Life Exp Report', fontsize = 20)
plt.show()

# save the plot as a file
fig.savefig('result.jpg',
            format='jpeg',
            dpi=100,
            bbox_inches='tight')