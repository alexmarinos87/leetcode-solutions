import pandas as pd
import numpy as np

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    # 1. Assign each income to a salary category
    #    (-∞, 19999] → Low
    #    [20000, 50000] → Average
    #    (50000, ∞)  → High

    bins   = [-np.inf, 19999, 50000, np.inf]
    labels = ['Low Salary', 'Average Salary', 'High Salary']
    
    categories = pd.cut(accounts['income'],
                        bins=bins,
                        labels=labels,
                        right=True)


    # 2. Count accounts in each category

    counts = (categories
              .value_counts()               # may miss 0‑count buckets
              .reindex(labels, fill_value=0)  # ensure all three rows
              .reset_index())

    counts.columns = ['category', 'accounts_count']
    
    return counts

