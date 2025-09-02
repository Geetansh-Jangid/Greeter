import time
import os

{
    # Example entry:
    # "John": {"date": "2024-06-15", "email": os.environ.get("JOHN_EMAIL")},
}


def add_birthday(name, date, email_env_var):
    bdates[name] = {
        "date": date,
        "email": os.environ.get(email_env_var)
    }