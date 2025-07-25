import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Keep distinct salaries and get the two largest values
    top_two = employee['salary'].drop_duplicates().nlargest(2)
    
    # If there is no second‑highest, return None (maps to SQL NULL)
    second = top_two.iloc[1] if len(top_two) == 2 else None
    
    return pd.DataFrame({'SecondHighestSalary': [second]})
