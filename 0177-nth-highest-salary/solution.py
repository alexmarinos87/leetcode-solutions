import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Step 1: Get distinct salaries
    distinct_salaries = employee['salary'].drop_duplicates()
    
    # Step 2: Sort in descending order
    sorted_salaries = distinct_salaries.sort_values(ascending=False).reset_index(drop=True)
    
    # Step 3: Validate index and fetch the result safely
    if N > 0 and N <= len(sorted_salaries):
        result = sorted_salaries.iloc[N - 1]
    else:
        result = None  # Return None if N is invalid or too large
    
    # Step 4: Return result in expected DataFrame format
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})

