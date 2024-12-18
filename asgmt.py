#!/usr/bin/env python
# coding: utf-8


import orjson
import re

# Step 1: Read the JSON file
with open('Python-task.json', 'r') as file:
    data = file.read()

# Parse the JSON data using orjson
json_data = orjson.loads(data)

# Step 2: Extract all prices and room types
prices = json_data['assignment_results'][0]['shown_price']
price_list = []  # List to store all prices
room_type = []   # List to store all room types

# Populate price_list and room_type
for room_name in prices:
    price = prices[room_name]
    price_list.append(price)
    room_type.append(room_name)

# Step 3: Find the lowest price
lowest_price = price_list[0]
for prc in price_list:
    prze = float(prc)
    if float(lowest_price) >= prze:
        lowest_price = prze

# Save the lowest price to the output file
with open('output_file.txt', 'a') as file:
    file.write("The Lowest Price is " + str(lowest_price))

# Step 4: Save all room types to the output file
all_room_types = '\n'.join(room_type)
with open('output_file.txt', 'a') as file:
    file.write("\n\nThe Types of rooms are \n" + str(all_room_types))

# Step 5: Extract the number of guests
no_of_guest = json_data['assignment_results'][0]['number_of_guests']

# Save the number of guests and lowest price to the output file
with open('output_file.txt', 'a') as file:
    file.write("\n\nThe no of Guests " + str(no_of_guest) + "  The Lowest Price is " + str(lowest_price))

# Step 6: Extract taxes from the JSON data
tax_data = json_data['assignment_results'][0]['ext_data']['taxes']
tax = re.findall('"TAX":"(.*?)"', str(tax_data))[0]  # Extract tax value
city_tax = re.findall('"TAX":"(.*?)"', str(tax_data))[0]  # Extract city tax value

# Step 7: Calculate total prices for all rooms
netprices = json_data['assignment_results'][0]['net_price']
room_with_prices = ""

for roomname in netprices:
    rprice = prices[roomname]
    final_price = float(rprice) + float(tax) + float(city_tax)
    room_with_prices += str(roomname) + ' ' + str(final_price) + ' \n'

# Save the total prices for all rooms to the output file
with open('output_file.txt', 'a') as file:
    file.write("\n\ntotal price (Net price + taxes) for all rooms along with the room type \n" + str(room_with_prices))
