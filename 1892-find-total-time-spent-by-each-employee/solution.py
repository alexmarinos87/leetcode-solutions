import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    # 1) Time spent for each entry
    employees = employees.assign(duration=employees['out_time'] - employees['in_time'])
    
    # 2) Sum durations per (day, emp)
    result = (
        employees.groupby(['event_day', 'emp_id'], as_index=False)['duration']
                 .sum()
                 .rename(columns={'event_day': 'day',
                                  'duration':   'total_time'})
    )
    
    return result

