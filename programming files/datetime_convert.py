from datetime import datetime

# Define string containing date and time in compatible format with date time object, BUG FIXED: missing apostrophe
date_str = "2022-03-17 10:45:30"

# Create date time object by parsing the string, BUG FIXED missing comma
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

# Convert the date time object to a string, BUG FIXED: missing modulus'
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

# Print date time object
print(formatted_date)
