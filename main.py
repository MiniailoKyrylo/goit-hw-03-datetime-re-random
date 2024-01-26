import datetime as dtdt
from datetime import datetime as dt
import random
import re

# Task 1
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

def get_days_from_today(date: str) -> int:
    difference_date = 0 # Value to return function
    try: # Check input to the function 
        original_date = dt.strptime(date, '%Y-%m-%d').date() # Сut off the date -> datetime.date
    except ValueError: # Input is str, but is not format -> ValueError
        print(f'Log: ValueError - "{date}" is not format "YYYY-MM-DD"') # Print ValueError
    except TypeError: # Input is not str
        print(f'Log: TypeError - "{date}" is not string') # Print TypeError
    else: # Main code function
        local_date = dt.today().date() # Сut off the date -> datetime.date
        difference_date = (local_date - original_date).days # Difference date and cut off the days -> int
    finally: # Return function
        return difference_date

# Task 1 Example
# print('Answer: ', get_days_from_today('2020-10-22'))
# print('Answer: ', get_days_from_today(2020-11-22))
# print('Answer: ', get_days_from_today('2020-10-22f'))
    
# Task 2 
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
    
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    answer = set() # Value to return function
    try: # Check input to the function
        min = int(min)
        max = int(max)
        quantity = int(quantity)
    except ValueError:
        print(f'Log: ValueError - The specified values ​​are not int') # Print ValueError
    else: # Main code function
        if min >= 1 and max <= 1000 and quantity <= (max - min): # Check condition values
            while (len(answer) < quantity): # Fill the set unique values while len < quantity 
                answer.add(random.randint(min, max)) # Add a randon value to the set 
        else: # Print ValueError
            print(f'Log: ValueError - Expected MIN >= 1 and MAX <= 1000 and QUANTITY >= MIN - MAX')
    finally: # Sorted and convert to list and return function
        answer = list(sorted(answer))
        return answer

# Task 2 Example
# print('Answer: ', get_numbers_ticket(1, 20, 5))
# print('Answer: ', get_numbers_ticket(0, 1000, 5))
# print('Answer: ', get_numbers_ticket(10, 1001, 5))
# print('Answer: ', get_numbers_ticket(1, 10, 9))
# print('Answer: ', get_numbers_ticket(1, 10, 's'))

# Task 3
# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку.
    
def normalize_phone_not_regex(phone_number: list) -> list:
    answer = list() # Value to return function
    for number in phone_number: # Iteration of the passed list
        
        # answer.append('+380' + "".join(char for char in number if char.isdecimal())[-1:-10:-1][-1::-1])
        
        filtered_digits = filter(str.isdigit, number) # Filter only numbers
        cleaned_number = ''.join(filtered_digits) # Use method join
        last_digits = cleaned_number[-9:] # Cut 9 number
        formatted_number = '+380' + last_digits # Add values to normal number
        answer.append(formatted_number) # Add to the list

    return answer # Return function

def normalize_phone(phone_number: str):
    answer = list() # Value to return function
    raw_numbers = list() # List for parsing regex
    pattern = r"[\d\+]+" # Patter for parsin regex
    
    for raw_number in phone_number: # Loop parsing regex and add item to raw_numbers
        normal_number = ''.join(re.findall(pattern, raw_number)) # Use pattern in findall and use method join
        raw_numbers.append(normal_number) # Add normal number to the list
    print(raw_numbers)

    for raw_number in raw_numbers: # Loop sort and add start number
        if len(raw_number) == 10: 
            answer.append('+38' + raw_number) # Add if 10 number
        elif len(raw_number) == 11:
            answer.append('+3' + raw_number) # Add if 11 number
        elif len(raw_number) == 12:
            answer.append('+' + raw_number) # Add if 12 number
        else:
            answer.append(raw_number) # Add if normal number

    return answer # Return function

# Task 3 Example
# raw_numbers = ["067\\t123 4567", "(095) 234-5678\\n", "+380 44 123 4567",
#                "380501234567", "    +38(050)123-32-34", "     0503451234",
#                "(050)8889900", "38050-111-22-22", "38050 111 22 11   ",
#                "8050 111 77 15   "]

# print(normalize_phone(raw_numbers))
# print(normalize_phone_not_regex(raw_numbers))

# Task 4
# Потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати.

def get_upcoming_birthdays(users):
    birthday_week_list = list() # Value to return function

    local_date = dt.today().date() # Today date and cut off the date -> datetime.date
    local_weekdate_start = local_date - dtdt.timedelta(days=local_date.weekday() + 2) # Find last Suturday
    local_weekdate_finish = local_date + dtdt.timedelta(days=4 - local_date.weekday()) # Find end work week
    
    for user in users: 
        user['birthday'] = dt.strptime(user['birthday'], '%Y.%m.%d').date() # Pasrsing birthday
        
        if (local_date.month - user['birthday'].month) == 0: # If month local equals moth birthday
            if (local_weekdate_start.day <= user['birthday'].day <= local_weekdate_finish.day): # If equal week from Suturday to Friday
                birthday_week_list.append(user) # Append values to the list
    return birthday_week_list # Return function

# Task 4 Example
# users_list = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.26"},
#     {"name": "Anna Brook", "birthday": "1990.01.12"},
#     {"name": "Lil Smith", "birthday": "1990.02.22"},
#     {"name": "Bob Lolkin", "birthday": "1996.01.21"},
#     {"name": "Emma Dog", "birthday": "1999.01.20"},
#     {"name": "Kate Rabbit", "birthday": "2003.01.23"}]

# for user in get_upcoming_birthdays(users_list):
#     print(user)