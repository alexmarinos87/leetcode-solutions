import pandas as pd

def sales_person(sales_person: pd.DataFrame,
                 company: pd.DataFrame,
                 orders: pd.DataFrame) -> pd.DataFrame:
    """
    Return the names of salespeople who have **no** orders with the
    company whose name is "RED".

    Parameters
    ----------
    sales_person : pd.DataFrame
        Columns: sales_id, name, salary, commission_rate, hire_date
    company : pd.DataFrame
        Columns: com_id, name, city
    orders : pd.DataFrame
        Columns: order_id, order_date, com_id, sales_id, amount

    Returns
    -------
    pd.DataFrame
        Single column `name` containing all salespeople that never sold to
        company "RED".  Row order is irrelevant.
    """

    # ------------------------------------------------------------
    # 1️⃣  Find the company IDs whose name is "RED"
    # ------------------------------------------------------------
    red_com_ids = company.loc[company['name'] == 'RED', 'com_id']

    # ------------------------------------------------------------
    # 2️⃣  Gather all sales_id that have at least one order to "RED"
    # ------------------------------------------------------------
    red_sales_ids = (
        orders.loc[orders['com_id'].isin(red_com_ids), 'sales_id']
              .unique()                       # distinct salesperson IDs
    )

    # ------------------------------------------------------------
    # 3️⃣  Select salespeople whose ID is **not** in that list
    # ------------------------------------------------------------
    result = (
        sales_person.loc[~sales_person['sales_id'].isin(red_sales_ids),
                         ['name']]            # keep only the 'name' column
    )

    return result
