import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 1️⃣  Find the max salary in each department
    max_by_dept = (
        employee.groupby('departmentId', as_index=False)['salary']
                .max()
                .rename(columns={'salary': 'max_salary'})
    )

    # 2️⃣  Keep only employees whose salary equals that department’s max
    top_earners = employee.merge(max_by_dept, on='departmentId')
    top_earners = top_earners[top_earners['salary'] == top_earners['max_salary']]

    # 3️⃣  Attach department names
    result = (
        top_earners.merge(department, left_on='departmentId', right_on='id')
                   .loc[:, ['name_y', 'name_x', 'salary']]          # select columns
                   .rename(columns={'name_y': 'Department',
                                    'name_x': 'Employee',
                                    'salary': 'Salary'})
    )

    return result

