#Giovani Martins
#I believe the only thing that isn't perfect in this project is the y axis labels
#code bellow imports arcade library
import arcade
import math
#code bellow opens the text file
country_data = open("nationsPop.txt", "r")
#code bellow reads all the files in the text file
lines_from_country_data = country_data.readlines()
xValue = 39
#code bellow opens a window for the drawing
window = arcade.open_window(1536,860, "Graph paper")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
#code bellow draws a title
arcade.draw_text("Population of the largest pop Nations in Earth", 650, 800, arcade.color.WHITE)
#the code bellow draws the y-axis
arcade.draw_line(115,90,115,850, arcade.color.WHITE,2)
#the code bellow draws the x-axis
arcade.draw_line(115,90,1350,90, arcade.color.WHITE,2)

#code bellow makes each word in the text file a value in a list and then assigns it into a dictionary
for line in lines_from_country_data:
    line = line.split(",")
    countryDictionary = {"country" : line[0], "Population" : line[1], "Percentage" : line[2]}
    print(countryDictionary['country'] + " has a population of",countryDictionary['Population'] + " and a a growth rate in the last year of",countryDictionary['Percentage'],)
    #the code bellow makes a stores a increasing value to use as pixels to label the countries in the x-axis
    xValue += 90
    arcade.draw_text(countryDictionary["country"],xValue,50,arcade.color.WHITE,10)
    #bar height math
    barHeight = (int(countryDictionary['Population'])-100_000_000)/1_000_000
    print('The y-value of the bar height for this country is', + math.floor(barHeight))
    #code bellow checks if the growth rate is negative or negative and then assigns the proper color for the graph
    if float(countryDictionary['Percentage']) >0:
        color = arcade.color.GREEN
    else:
        color = arcade.color.RED
    arcade.draw_xywh_rectangle_filled(xValue,91,50, barHeight, color)

#code bellow writes the population numbers
arcade.draw_text("1400M", 50, 840,arcade.color.WHITE,11)
arcade.draw_text("1300M", 50, 800,arcade.color.WHITE,11)
arcade.draw_text("1200M", 50, 750,arcade.color.WHITE,11)
arcade.draw_text("1100M", 50, 700,arcade.color.WHITE,11)
arcade.draw_text("1000M", 50, 650,arcade.color.WHITE,11)
arcade.draw_text("900M", 50, 600,arcade.color.WHITE,11)
arcade.draw_text("800M", 50, 550,arcade.color.WHITE,11)
arcade.draw_text("700M", 50, 500,arcade.color.WHITE,11)
arcade.draw_text("600M", 50, 450,arcade.color.WHITE,11)
arcade.draw_text("500M", 50, 400,arcade.color.WHITE,11)
arcade.draw_text("400M", 50, 350,arcade.color.WHITE,11)
arcade.draw_text("300M", 50, 290,arcade.color.WHITE,11)
arcade.draw_text("200M", 50, 195,arcade.color.WHITE,11)
arcade.draw_text("100M", 50, 100,arcade.color.WHITE,11)


arcade.finish_render()
arcade.run()

