import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Convert wide → long: one row per (product_id, store, price)
    out = (
        products.melt(id_vars='product_id',
                      value_vars=['store1', 'store2', 'store3'],
                      var_name='store',
                      value_name='price')
               .dropna(subset=['price'])          # remove stores where product is unavailable
    )
    return out

