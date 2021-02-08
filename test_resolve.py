import resolve
import pandas as pd
def test_number_of_customers():
    test_cust = resolve.read_customers()['customer_id'].count()
    print(test_cust)
    assert test_cust==137

def test_number_of_products():
    product_count = resolve.read_products()['product_id'].count()
    print(product_count)
    assert product_count == 64

def test_products_for_c1():
    product_count = resolve.get_final_result()
    # print(product_count)
    c1_df = product_count.loc[product_count['customer_id']=='C1']['customer_id'].count()
    print(c1_df)
    assert c1_df == 14

def test_total_purchases_for_c10():
    product_count = resolve.get_final_result()
    # print(product_count)
    c1_df = product_count.loc[product_count['customer_id']=='C10']['purchase_count'].sum()
    print(c1_df)
    assert c1_df == 24

