import os
import csv
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
from datetime import datetime
import time 
import random 
import json



# Load configuration file
with open("config.json") as config_file:
    config = json.load(config_file)


# get the current date for prices 
current_date = datetime.now().strftime("%Y-%m-%d")

# create a directory to save the csv file 
output_dir = "scraping_results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# Generate a date-based filename 
filename = f"competitors_price_{current_date}.csv"
filepath = os.path.join(output_dir, filename)


# Function to scrape with Beautiful soup 
def scrape_with_beautifulsoup(url, selectors, referral):
    headers = {"Referer": referral}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    products = soup.select(selectors["product"])
    results = []

    for product in products:
        name_element = product.select_one(selectors["name"])
        name = name_element.text.strip() if name_element else "No title found"

        old_price = "N/A"
        current_price = "No price found"
        currency = "No currency"

        if 'price_container' in selectors:
            price_container = product.select_one(selectors['price_container'])
            if price_container:
                old_price_element = price_container.select_one(selectors['old_price'])
                old_price = old_price_element.text.strip() if old_price_element else ""

                current_price_element = price_container.select_one(selectors['current_price'])
                current_price = current_price_element.text.strip() if current_price_element else "No price found"

                currency_element = None
                currency = ""  # Assuming currency is part of the price text
            else:
                old_price = "No old price"
                current_price = "No current price"
                currency = "No currency"
        else:
            price_element = product.select_one(selectors['price'])
            if price_element:
                currency_element = price_element.select_one(selectors['currency']) if selectors['currency'] else None
                currency = currency_element.text.strip() if currency_element else ""
                current_price = price_element.text.strip().replace(currency, "").strip()
            else:
                currency = "No currency"
                current_price = "No price found"
                old_price = "N/A"

        results.append((name, old_price, current_price, currency))
    return results





# Open a csv file to write the results 
with open(filepath, mode="w", newline="") as file:
    writer = csv.writer(file)


    # Write the header row
    writer.writerow(["Date", "Source", "Referral Source", "Product Name", "Old Price", "Current Price", "Currency"])

    for website in config["websites"]:
        url = website["url"]
        selectors = website["selectors"]

        parsed_url = urlparse(url)
        source = parsed_url.netloc

        for referral in config["referral_sources"]:

            results = scrape_with_beautifulsoup(url, selectors, referral)
            if not results:
                raise ValueError("No products found")
                


                
        for name, old_price, current_price, currency in results:
                    
            #writing the data to the csv file
            writer.writerow([current_date, source, referral, name, old_price, current_price, currency])

            # handeling respectful scraping 
            time.sleep(random.uniform(1, 3))


print("Data has been written to {filepath}")
                


