def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    Return a DataFrame of customer names who never placed an order.
    Output column must be named 'Customers'.
    """
    # Boolean mask: customers whose id does NOT appear in orders.customerId
    no_orders = ~customers['id'].isin(orders['customerId'].values)

    return (
        customers.loc[no_orders, ['name']]
                 .rename(columns={'name': 'Customers'})
    )
