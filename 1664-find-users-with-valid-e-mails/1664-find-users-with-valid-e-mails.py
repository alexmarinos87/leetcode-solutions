import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # Define regex for a valid email:
    # - Starts with a letter: [a-zA-Z]
    # - Followed by any number of letters, digits, underscores, dots, or dashes: [\w\.-]*
    # - Ends with @leetcode.com
    valid_email_regex = r"^[a-zA-Z][\w\.-]*@leetcode\.com$"
    
    # Filter rows where 'mail' matches the regex pattern
    valid_users = users[users["mail"].str.match(valid_email_regex)]
    
    return valid_users
