import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Build a Boolean mask:
    #    • customers['id'] gives the customer IDs column.
    #    • .isin(orders['customerId']) checks membership row-by-row.
    #    • ~  negates the Series, so True means “id not present in Orders”.
    mask = ~customers['id'].isin(orders['customerId'])

    # Apply the mask (row filter) and rename the surviving column.
    return (
        customers.loc[mask, ['name']]     # keep only rows flagged True
                .rename(columns={'name': 'Customers'})  # match expected header
    )
