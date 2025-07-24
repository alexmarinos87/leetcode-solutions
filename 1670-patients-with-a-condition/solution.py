import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Split the 'conditions' by whitespace, then check if any condition starts with 'DIAB1'
    def has_diab1(conds):
        if not isinstance(conds, str):
            return False
        return any(code.startswith('DIAB1') for code in conds.split())

    diabetic_patients = patients[patients['conditions'].apply(has_diab1)]
    return diabetic_patients[['patient_id', 'patient_name', 'conditions']]

