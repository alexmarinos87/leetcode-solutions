import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    Return the customer_number of the customer who placed the
    largest number of orders.  The problem guarantees that exactly
    one customer is the winner.

    Parameters
    ----------
    orders : pd.DataFrame
        Columns:
        - order_number    : int
        - customer_number : int

    Returns
    -------
    pd.DataFrame with one column, `customer_number`, and exactly one row.
    """
    if orders.empty:
        # Edge‑case safeguard (not expected in LeetCode test‑cases)
        return pd.DataFrame(columns=['customer_number'])

    # Count orders per customer and take the index with the max count
    top_customer_id = orders['customer_number'].value_counts().index[0]

    return pd.DataFrame({'customer_number': [top_customer_id]})

