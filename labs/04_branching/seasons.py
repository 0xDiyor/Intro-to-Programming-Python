month = input()
day = int(input())

days_in_month = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30,
    'May': 31, 'June': 30, 'July': 31, 'August': 31,
    'September': 30, 'October': 31, 'November': 30, 'December': 31
}

if month not in days_in_month or day < 1 or day > days_in_month[month]:
    print('Invalid')
else:
    if (month == 'March' and day >= 20) or \
       (month in ['April', 'May']) or \
       (month == 'June' and day <= 20):
        print('Spring')
    elif (month == 'June' and day >= 21) or \
         (month in ['July', 'August']) or \
         (month == 'September' and day <= 21):
        print('Summer')
    elif (month == 'September' and day >= 22) or \
         (month in ['October', 'November']) or \
         (month == 'December' and day <= 20):
        print('Autumn')
    else:
        print('Winter')