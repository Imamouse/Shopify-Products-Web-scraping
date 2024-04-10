# src: https://www.youtube.com/watch?v=jPjxWC7zV2s
import requests
import pandas as pd
from url import url
from pprint import pprint

product_list = []

for y, link in enumerate(url):
    r = requests.get(url[y])
    data = r.json()
    for x, item in enumerate(data["products"]):
        title = item["title"]
        handle = item["handle"]
        for variant in item["variants"]:
            try:
                sku = variant["title"]
                available = variant["available"]
                new_price = variant["price"]
                original_price = variant["compare_at_price"]
            except:
                sku = None
                available = None
                new_price = None
                original_price = None

            product = {
                "title": title,
                "handle": handle,
                "sku": sku,
                "available": available,
                "old price": original_price,
                "new price": new_price
            }

            product_list.append(product)

    df = pd.DataFrame(product_list)
    df.to_csv("title.csv", index=False)
    print(f"{link} - saved to file!")
