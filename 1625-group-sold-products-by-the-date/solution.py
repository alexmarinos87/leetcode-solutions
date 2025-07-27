import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    """
    Return, for every distinct sell_date, the number of different products sold
    and a comma‑separated list of those product names in lexicographic order.

    Parameters
    ----------
    activities : pd.DataFrame
        Columns
        ----------
        • sell_date : date‑like (str or datetime) — the day a sale happened  
        • product   : str                     — the product that was sold

    Returns
    -------
    pd.DataFrame
        Columns
        ----------
        • sell_date : date                     — same as input
        • num_sold  : int                      — count of distinct products
        • products  : str                      — comma‑joined product names
        The rows are ordered by sell_date ascending.
    """
    # ---------------------------------------------------------------
    # 1️⃣  Group by date and collect DISTINCT product names
    #     * x.unique()  removes duplicates
    #     * sorted(...) puts them in alphabetical order
    # ---------------------------------------------------------------
    grouped = (
        activities.groupby('sell_date')['product']
                  .agg(lambda x: sorted(x.unique()))       # list[str]
                  .reset_index(name='product_list')        # keep date + list
    )

    # ---------------------------------------------------------------
    # 2️⃣  Derive the two output columns from the list:
    #     • num_sold  : length of the list
    #     • products  : comma‑joined string (no spaces)
    # ---------------------------------------------------------------
    grouped['num_sold'] = grouped['product_list'].str.len()
    grouped['products'] = grouped['product_list'].apply(','.join)

    # ---------------------------------------------------------------
    # 3️⃣  Select the required columns and sort by date
    # ---------------------------------------------------------------
    result = (grouped
              .loc[:, ['sell_date', 'num_sold', 'products']]
              .sort_values('sell_date')     # LeetCode expects any order; we sort for clarity
              .reset_index(drop=True))

    return result

