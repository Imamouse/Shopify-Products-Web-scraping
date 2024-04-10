# Shopify-Products-Web-scraping
Shopify Products Web scraping  Source: https://www.youtube.com/watch?v=jPjxWC7zV2s

## Introduction
This Python script retrieves product data from multiple APIs, processes the data, and saves it to a CSV file. It is designed to work with JSON-formatted API responses containing product information.

## Requirements
- Python 3.x
- Requests library (`pip install requests`)
- Pandas library (`pip install pandas`)

## Usage
1. Replace the `url` list variable with the URLs of the APIs you want to fetch data from.
2. Run the script.

## Functionality
- Fetches JSON data from each URL in the `url` list.
- Extracts product details from the JSON responses, including title, handle, SKU, availability, old price, and new price.
- Saves the extracted data to a CSV file named "title.csv".

## Script Details
- The script iterates through each URL in the `url` list.
- For each URL, it retrieves JSON data using the Requests library.
- It then processes the JSON data, extracting product details and storing them in a list of dictionaries.
- After processing all URLs, it converts the list of dictionaries into a pandas DataFrame.
- Finally, it saves the DataFrame to a CSV file using the `to_csv` method.

## Additional Notes
- This script assumes that each API response contains a "products" key, which holds a list of product objects.
- It further assumes that each product object contains attributes such as title, handle, variants, etc.

