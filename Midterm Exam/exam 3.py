import re


def is_valid_url(url):
    # Define a regular expression pattern for matching URLs
    url_pattern = re.compile(
        r'^(https?://)?'  # Optional scheme (http:// or https://)
        r'([a-zA-Z0-9-]+\.)*'  # Optional subdomains
        r'[a-zA-Z0-9-]+\.'  # Main domain
        r'([a-zA-Z]{2,})(:[0-9]+)?'  # Top-level domain and optional port
        r'(/.*)?$'  # Optional path
    )

    # Check if the provided URL matches the pattern
    if re.match(url_pattern, url):
        return True
    else:
        return False


def days_since_birthday(birthday):
    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))

    # Calculate the number of days passed in the birth year
    days_in_birth_year = 365 - sum(month_days[:month - 1]) - day

    # Calculate the number of days passed in the years between birth year and current year (excluding both)
    days_between_years = (current_year - year - 1) * 365

    # Calculate the number of days passed in the current year up to the current date
    days_in_current_year = sum(month_days[:current_month - 1]) + current_day

    # Calculate the total number of days passed since birth (excluding birth year and current year)
    total_days_passed = days_in_birth_year + days_between_years + days_in_current_year

    return total_days_passed


# Current date
current_date = "01-03-2024"
current_day, current_month, current_year = map(int, current_date.split('-'))

# Days in each month (non-leap year)
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Your birthday
birthday = "26-09-2004"

# Calculate the number of days since your birthday
days_passed = days_since_birthday(birthday)
print("Days passed since your birthday (excluding birth year and current year):", days_passed)

