# -*- coding: utf-8 -*-
"""
File: my_script.py
Author: Srividhya L
Created: January 5, 2024
Description: This script scrapes the Boots website – sleep product page filters
and extract all the products on the page including title, price, price_units ,short_desc, filters and
extract all the products on the page including title, rating, price, and median price,rating and product page size in KB.
"""

import json
import time
import requests
import time

from bs4 import BeautifulSoup
from selenium import webdriver

# Capture the start time of the code for future metrics purpose
start_time = time.time()

# Initialize an empty list to store product details
products_list = []

local_html_path = 'D:/Downloads/Sleep Aid Clone/Sleep Aid.html'

#webdriver to scrape the Main page
driver = webdriver.Chrome()
driver.get(f'file:///{local_html_path}')
driver.implicitly_wait(300)

page_content = driver.page_source
# print(page_content)

main_soup = BeautifulSoup(page_content, 'html.parser')

# Extract necessary product details
title_elements = main_soup.find_all('h3', class_='oct-text oct-text--standard oct-text--size_m oct-aem-text '
                                                 'oct-aem-text--h3--variant-2 oct-teaser__title '
                                                 'oct-teaser-with-listers')

price_elements = main_soup.find_all('p',
                                    class_='oct-text oct-text--standard oct-text--size_m oct-aem-text '
                                           'oct-aem-text--p--variant-subtext oct-teaser__productPrice')
desc_elements = main_soup.find_all('p',
                                   class_='oct-text oct-text--standard oct-text--size_m oct-aem-text '
                                          'oct-aem-text--p--variant-subtext oct-teaser__productPriceDetail')
product_page = main_soup.find_all('a',
                                  class_='oct-link oct-link--theme-text oct-color--boots-blue oct-teaser__title-link')
product_href_list = main_soup.find_all('a',
                                       class_='oct-link oct-link--theme-text oct-color--boots-blue '
                                              'oct-teaser__title-link',
                                       href=True)

products = []
price_list = []
product_review = 0
if len(title_elements) == len(price_elements):
    for i in range(len(title_elements)):
        title = title_elements[i].text.strip()
        price_withUnits = price_elements[i].text.strip()
        price = price_withUnits[1:]
        price_list.append(price)
        units = price_withUnits[0]
        Short_Desc = desc_elements[i].text.strip()
        product_href = product_href_list[i]['href']
        product_html_path = 'D:/Downloads/Sleep Aid Clone'
        constructed_path = product_html_path + product_href[1:]

        #creating webdriver to scrape into the product page to retrieve the Rating and html page size details
        driver1 = webdriver.Chrome()
        driver1.get(f'file:///{constructed_path}')
        driver1.implicitly_wait(100)

        product_content = driver1.page_source

        product_soup = BeautifulSoup(product_content, 'html.parser')
        #print(product_soup)
        page_size = len(product_soup.text)
        page_size_kb = page_size / 1024  # Convert bytes to kilobytes
        product_review = product_soup.find('div', class_='bv_avgRating_component_container',
                                           itemprop='ratingValue')
        rating_value = product_review.text.strip() if product_review else 'Rating not found'
        products.append(
            {"Title": title, "Price": price, "Price_Unit": units, "Short_Desc": Short_Desc, "Rating": rating_value, "Page_size": page_size_kb})

#Logic to calculate the Median price of the retrieved price list
sorted_prices = sorted([float(price) for price in price_list])
n = len(sorted_prices)
if n % 2 == 0:
    # If the number of prices is even, average the middle two prices
    median_price = (sorted_prices[n // 2 - 1] + sorted_prices[n // 2]) / 2
else:
    # If the number of prices is odd, take the middle price
    median_price = sorted_prices[n // 2]

# Create the final JSON structure
output_data = {
    'Products': products,
    'Median': median_price
}

# Save the data as JSON in the specified format
with open('D:/data/output.json', 'w') as output_file:
    json.dump(output_data, output_file, ensure_ascii=False, indent=4)

# Capture the end time of the code for future metrics purpose
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.2f} seconds")
