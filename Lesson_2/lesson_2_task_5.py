month = input('Введите номер месяца (1-12): ')
month_as_number = int(month)


def month_to_season(month):
    if month in [12, 1, 2]:
        return 'winter'
    elif 3 <= month <= 5:
        return 'spring'
    elif 6 <= month <= 8:
        return 'summer'
    elif 9 <= month <= 11:
        return 'autumn'
    else:
        return 'Некорректный номер месяца'


print(month_to_season(month_as_number))
