import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # Build a Boolean mask for the rows we care about
    mask = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')

    # Filter the rows and keep only the product_id column
    return products.loc[mask, ['product_id']]