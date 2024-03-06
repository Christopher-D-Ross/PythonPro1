# Functions with Outputs

def output_function():
    return 6 * 6


print(output_function())
result = output_function()
print(output_function() * result)


def format_name(first, last):
    """Take a first and last name and format it
    to return the title case version of the name."""
    first = first.title()
    last = last.title()
    return f"{first} {last}"


print(format_name("somba", "kalen"))


# Days In Month - Exercise
def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


def days_in_month(year_val, month_val):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not is_leap(year_val):
        return month_days[month_val - 1]
    elif is_leap(year_val) and month_val == 2:
        return 29


year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)