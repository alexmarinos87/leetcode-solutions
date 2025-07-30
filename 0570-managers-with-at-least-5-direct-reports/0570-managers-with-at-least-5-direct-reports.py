import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    """
    Return a DataFrame with the names of managers who have at least
    five direct reports.  Only managers that actually exist in the
    Employee table (i.e., whose id appears as an employee id) should
    be returned.
    """
    # 1️⃣ Count direct reports per managerId
    direct_counts = (
        employee.dropna(subset=['managerId'])       # rows that have a manager
                .groupby('managerId', as_index=False)
                .size()                             # new column 'size'
                .rename(columns={'size': 'reports'})
    )

    # 2️⃣ Keep managerIds with ≥ 5 reports
    qualified = direct_counts[direct_counts['reports'] >= 5]

    if qualified.empty:
        return pd.DataFrame(columns=['name'])

    # 3️⃣ Join to employee table to get the manager’s name
    result = (
        qualified.merge(employee[['id', 'name']],
                        left_on='managerId',
                        right_on='id',
                        how='inner')               # inner drop managers not in Employee
                .loc[:, ['name']]
    )

    return result
