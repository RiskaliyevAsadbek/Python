# 1 Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
from datetime import date

today = date.today()

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

birth_date = date(birth_year, birth_month, birth_day)

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    last_month = today.month - 1 or 12
    last_year = today.year if today.month != 1 else today.year - 1
    days_in_last_month = (date(today.year, today.month, 1) - date(last_year, last_month, 1)).days
    days += days_in_last_month

if months < 0:
    years -= 1
    months += 12


print(f"\nYou are {years} years, {months} months, and {days} days old.")

# 2 Days Until Next Birthday:
# Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

import datetime
today = datetime.date.today()

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

birth_date = datetime.date(birth_year, birth_month, birth_day)

if birth_date < today:
    birth_date = datetime.date(today.year + 1, birth_month, birth_day)

days_left = (birth_date - today).days
print(days_left)


# 3 Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes.
# Calculate and print the date and time when the meeting will end.
import datetime
current_year = int(input('enter current year:'))
current_month = int(input('enter the current month(1-12):'))
current_day = int(input('enter the current day(1-31): '))
current_hour = int(input('enter the current hour:(0-23)'))
current_minute = int(input('enter the current minute:(0-59)'))
duration_of_meeeting_hour = int(input('enter the current hour:'))
duration_of_meeting_minute = int(input('enter the current minute:'))
today = datetime.datetime(current_year,current_month,current_day,current_hour,current_minute)
delta = datetime.timedelta(hours=duration_of_meeeting_hour,minutes=duration_of_meeting_minute)
end = today + delta
print(f'the meeting will end {end}')

# 4 Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone,
#  and then convert and print the date and time in another timezone of their choice.
import datetime
current_year = int(input('enter current year:'))
current_month = int(input('enter the current month(1-12):'))
current_day = int(input('enter the current day(1-31): '))
current_hour = int(input('enter the current hour:(0-23)'))
current_minute = int(input('enter the current minute:(0-59)'))
current_timezone = int(input('enter teh your current tiemzone:'))
today = datetime.datetime(current_year,current_month,current_day,current_hour,current_minute)
c= today.replace(tzinfo=datetime.timezone.utc)
d = datetime.timezone(datetime.timedelta(hours=current_timezone))
converted = c.astimezone(d)
print(converted)

# 5 Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, 
# and then continuously print the time remaining until that point in regular intervals (e.g., every second).
import datetime
future_year = int(input('enter current year:'))
future_month = int(input('enter the current month(1-12):'))
future_day = int(input('enter the current day(1-31): '))
future_hour = int(input('enter the current hour:(0-23)'))
future_minute = int(input('enter the current minute:(0-59)'))
now = datetime.datetime.now()
future = datetime.datetime(future_year,future_month,future_day,future_hour,future_minute)

# 6 Email Validator: Write a program that validates email addresses. 
# Ask the user to input an email address, and check if it follows a valid email format.
import re
email = input('Please enter your email: ')
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern,email):
    print('valid email')
else:
    print('not valid email')


# 7 Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. 
# For example, convert "1234567890" to "(123) 456-7890".
phone_number = input('enter a 10-digit phone number(e.g 1234567890)')
phone = ''.join(filter(str.isdigit,phone_number))
if len(phone) == 10:
    formatted = f'({phone[ : 3]}) {phone[ 3: 6]}-{phone[ 6 :]}'
    print('formatted phone number:',formatted)
else:
    print('Invalid phone number')    

# 8 Password Strength Checker: Implement a password strength checker. 
# Ask the user to input a password and check if it meets 
# certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
import re
pasword = input('Please, enter your password: ')
pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@%&#+=!]).{8,}'
if re.match(pattern,pasword):
    print('Valid password')
else:
    print('not valid password')    

# 9 Word Finder: Develop a program that finds all occurrences of a specific word in a given text. 
# Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
import re
text = input('enter the text: ')
word = input('enter the word you want to search: ')
pattern = r'\b' + re.escape(word) + r'\b'
matches = list(re.finditer(pattern, text, re.IGNORECASE))
if matches:
    print(f"\n The word '{word}' was found {len(matches)} time(s):")
    for match in matches:
        print(f" - Position: {match.start()} to {match.end()}")
else:
    print(f"\n The word '{word}' was not found in the text.")

# 10 Date Extractor: Write a program that extracts dates from a given text.
# Ask the user to input a text, and then identify and print all the dates present in the text.
import re
text = input('enter the text: ')
pattern = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2}|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{1,2},\s\d{4})\b'
dates = re.findall(pattern, text)
if dates:
    print("\n Dates found in the text:")
    for d in dates:
        print(" -", d)
else:
    print("\n No dates found in the text.")
