import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Condition: odd ID & name not starting with 'M'
    eligible = (employees["employee_id"] % 2 == 1) & ~employees["name"].str.startswith("M")
    
    # Assign bonus
    employees["bonus"] = employees["salary"].where(eligible, 0)
    
    # Select required columns and sort
    return employees[["employee_id", "bonus"]].sort_values("employee_id").reset_index(drop=True)

