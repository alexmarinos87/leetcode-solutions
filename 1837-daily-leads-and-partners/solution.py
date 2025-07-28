import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    """
    For every (date_id, make_name) pair compute:
        • unique_leads     : how many distinct lead_id values
        • unique_partners  : how many distinct partner_id values

    Parameters
    ----------
    daily_sales : pd.DataFrame
        Columns
        --------
        • date_id    : date (or string) – the day of the sale
        • make_name  : str              – product name / brand
        • lead_id    : int              – ID of the lead
        • partner_id : int              – ID of the partner

    Returns
    -------
    pd.DataFrame
        Columns
        --------
        • date_id
        • make_name
        • unique_leads
        • unique_partners
        Row order does not matter (LeetCode accepts any order).
    """
    # 1) Group by date and make
    grouped = daily_sales.groupby(['date_id', 'make_name'])

    # 2) Count distinct lead_id and partner_id
    result = (
        grouped.agg(
            unique_leads     = ('lead_id',    'nunique'),
            unique_partners  = ('partner_id', 'nunique')
        )
        .reset_index()  # back to a regular DataFrame
    )

    return result

