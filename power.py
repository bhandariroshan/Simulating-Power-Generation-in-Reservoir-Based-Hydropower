# import math
import math


def get_fh(height):
    fh = 13557.8282850575 * math.pow(float(height), 2) - 23743654.1706026000 * float(height) + \
        10398688014.4791000000
    # print "fh:", fh
    return fh


def get_f1h(height):
    f1h = 2 * 13557.8282850575 * float(height) - 23743654.1706026000
    # print "f1h: ", f1h
    return f1h


def get_dh(height, power_need, inflow):
    # print "a, b, c: ", height, power_need, inflow
    height = float(height)
    power_need = float(power_need)
    inflow = float(inflow)

    ''' dh =  ((p/(9810*(h-800)) - i)/f1(h))*600 '''
    # print(get_f1h(height))
    differential_height_per_ten_minute = (
        power_need / (9810 * (height - 800)) - inflow
    ) / get_f1h(height) * 600

    precision = "%.5f"
    # print "dh:", precision % differential_height_per_ten_minute
    return float(precision % differential_height_per_ten_minute)


def quadratic(a, b, c):
    # quadratic equation precision
    precision = "%.4f"

    discRoot = math.sqrt((b * b) - 4 * a * c)

    # solving positive
    root1 = (-b + discRoot) / (2 * a)

    # solving negative
    root2 = (-b - discRoot) / (2 * a)
    if precision % root1 >= precision % root2:
        # print"root1:", float(precision % root1)
        return float(precision % root1)
    else:
        # print"root2:", float(precision % root2)
        return float(precision % root2)


def calculate_values():
    height = float(input('Please enter height: '))
    power_need = float(input('Please enter power to be generated: ')) * math.pow(10,6)

    for month in range(1, 13):
        DAYS_IN_MONTH = int(input('Please input number of days in month: '))
        inflow = float(input('Please enter river discharge: '))

        number_of_ten_minutes_in_peak_shift = float(
            input('Please enter 10 minutes in peak shift: ')
        )
        number_of_hours_in_non_peak_shift = float(
            input('Please input hours in non-peak shift: ')
        )
        for day in range(1, DAYS_IN_MONTH + 1):
            '''For first shift.'''
            i = 0
            while(i <= number_of_ten_minutes_in_peak_shift):
                i = i + 1
                height = height - get_dh(height, power_need, inflow)
                if(height < 885.695):
                    print "Insufficient Water Height: " + str(height) + " in month: " + str(month) + " day: " + str(day) + " shift: I " + " i value: " + str(i)

                    calculate_values()

            new_volume = get_fh(height) + inflow * number_of_hours_in_non_peak_shift * 3600
            # print("new volume:", new_volume)
            new_height = quadratic(
                13557.8282850575, -23743654.1706026000, 10398688014.4791000000 - float(new_volume)
            )

            '''For Second Shift.'''
            i = 0
            while(i <= number_of_hours_in_non_peak_shift):
                i = i + 1
                height = height - get_dh(height, power_need, inflow)
                if(height < 885.695):
                    print "Insufficient Water Height: " + str(height) + " in month: " + str(month) + " day: " + str(day) + " shift: II " + " i value: " + str(i)

                    calculate_values()
            print(i)

            new_volume = get_fh(height) + inflow * number_of_hours_in_non_peak_shift * 3600
            new_height = quadratic(
                13557.8282850575, -23743654.1706026000, 10398688014.4791000000 -float(new_volume)
            )

        print "Final height at the end of the month " + str(month) + ":: " + str(new_height)

    print "Final height at the end of the year: " + str(new_height)

calculate_values()