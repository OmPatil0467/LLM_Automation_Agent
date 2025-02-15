# src/utils.py

def count_weekdays(dates):
    """Counts the number of weekdays in a given list of date strings."""
    from datetime import datetime

    weekdays = 0
    for date_str in dates:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        if dt.weekday() < 5:  # Monday to Friday are weekdays (0-4)
            weekdays += 1
    return weekdays


def sort_contacts(contacts):
    """Sorts contacts by their name alphabetically."""
    return sorted(contacts, key=lambda x: x['name'])