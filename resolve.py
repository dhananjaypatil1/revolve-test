# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
from pathlib import Path
from tabulate import tabulate
import json

def read_customers():
    customers = pd.DataFrame(pd.read_csv("data/customers.csv"))
    return customers

def read_products():
    products = pd.DataFrame(pd.read_csv("data/products.csv"))
    return products

def read_transactions():

    files = Path("data/transactions").glob("**/*.json")
    temp = pd.DataFrame()
    for file in files:
        df = pd.read_json(file, lines=True)
        temp = temp.append(df)

    exploded_temp = temp.explode('basket')
    json_temp = json.loads(exploded_temp.to_json(orient="records"))
    flat_transactions = pd.json_normalize(json_temp)
    return flat_transactions

def get_final_result():
    transactions = read_transactions()
    products = read_products()
    customers = read_customers()

    # print(customers.head())
    # print(products.head())
    # print(transactions.head())

    prod_trans = products.merge(transactions, left_on='product_id', right_on='basket.product_id')
    all_data = customers.merge(prod_trans, left_on='customer_id', right_on='customer_id')

    # print(all_data.head())
    # print(tabulate(pd.DataFrame(all_data.head()), headers='keys', tablefmt='psql'))
    result = all_data.groupby(['customer_id', 'loyalty_score', 'product_id', 'product_category'])\
            .size().reset_index(name='purchase_count')
    sorted_result = result.sort_values(by=['customer_id', 'loyalty_score', 'purchase_count'], ascending=[1, 1, 0])

    sorted_result.to_csv('data/result.csv')
    # print(tabulate(pd.DataFrame(sorted_result.head()), headers='keys', tablefmt='psql'))
    return sorted_result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_final_result()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
