import pandas as pd

def replace_employee_id(employees: pd.DataFrame,
                        employee_uni: pd.DataFrame) -> pd.DataFrame:
    """
    Return a table with each employee’s `unique_id` alongside their `name`.
    If an employee has no matching entry in `employee_uni`, the `unique_id`
    column should contain NaN (shown as `null` in LeetCode’s output).

    Parameters
    ----------
    employees : pd.DataFrame
        Columns: id (int), name (str)
    employee_uni : pd.DataFrame
        Columns: id (int), unique_id (int)

    Returns
    -------
    pd.DataFrame
        Columns: unique_id, name
        Row order follows the original `employees` table.
    """

    # ① Left‑join: keep every row from `employees`, add `unique_id` where available
    merged = employees.merge(employee_uni, on="id", how="left")

    # ② Select the required columns in the required order
    result = merged[["unique_id", "name"]]

    return result
