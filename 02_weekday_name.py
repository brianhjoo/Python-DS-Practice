def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """

    day_of_week = int(day_of_week)

    days = {
        1 : 'Sunday',
        2 : 'Monday',
        3 : 'Tuesday',
        4 : 'Wednesday',
        5 : 'Thursday',
        6 : 'Friday',
        7 : 'Saturday'
    }

    for day in days.keys():
        if day == day_of_week:
            return days[day]







    # if day == 1:
    #     return 'Sunday'
    # elif day == 7:
    #     return 'Saturday'
    # elif day not in range(1, 7 + 1):
    #     return