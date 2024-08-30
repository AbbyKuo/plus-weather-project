import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """

    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    # step 1: parse the ISO string to a datetime object
    dt = datetime.fromisoformat(iso_string)
    # step 2: Format the datetime object to the desired string format
    formatted_date = dt.strftime("%A %d %B %Y") 
    return formatted_date

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    
    # step 1: convert temp_in_fahrenheit into float 
    # step 2: convert fahrenheit to celsius
    # step 3: return temperature in celsius with rounding to 1 decimal place
    temp_in_celsius = (float(temp_in_fahrenheit) - 32) * 5 / 9 
    rounded_temp_in_celsius = round(temp_in_celsius, 1)
    return rounded_temp_in_celsius

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0                                  # set counter to 0
    for weather in weather_data:             # loop through each element in weather_data list
        float(weather)                       # convert weather into float
        sum = sum + float(weather)           # add each element to counter for sum
    mean_temp =  sum / len(weather_data)     # divide sum by the number of the element to get mean value
    return mean_temp

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_list = []

    with open(csv_file, encoding='utf8') as file:
        reader = csv.reader(file)  # create a csv object 
        next(reader) #  exclude head
        
        for row in reader:
            if row != []:  # exclude empty row and head
                weather_list.append([row[0], int(row[1]), int(row[2])])  # run_tests.py expect returning [['', int, int]]
        return weather_list

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # step 1: handle empty list
    if weather_data == []:
        return ()
    # step 2: change weather data to float
    updated_weather_data = [float(weather) for weather in weather_data]

    # step 3: set first element as the staring point to compare with the other elements in the list, and find out the minium vale and the minium's last position 
    min_value = updated_weather_data[0]
    last_index = -1

    # step 5: compare each element in the list and find the last position of the minimum vale  
    for index, value in enumerate(updated_weather_data):
        if min_value > value:
            min_value = value
        if value == min_value:
            last_index = index
    return (min_value, last_index) #run_tests.py expects returning tuple

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # step 1: handle empty list
    if weather_data == []:
        return ()
    
    # step 2: change the weather data to float date
    updated_weather_data = [float(weather) for weather in weather_data]

    # step 3: check how many elements in the list
    total_elements = len(updated_weather_data)

    # step 4: set first element as the staring point to compare with the other elements in the list, and find out the maximum vale 
    max_value = updated_weather_data[0]

    # step 5: compare each element in the list to find the max value in the list
    for i in range(total_elements):
        if updated_weather_data[i] > max_value:
            max_value = updated_weather_data[i]

    # step 6: find the last index of the maximum vale
    last_index = -1    
    for key, value in enumerate(updated_weather_data):
        if value == max_value:
            last_index = key
    return (max_value, last_index)  #run_tests.py expects returning tuple

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # data required: min temp, max temp, average low , average high, day and date, number of days in weather data
    # find minium and maximum temperature 
    # convert minium and maximum temperature from fahrenheit to celsius 
    # format minium and maximum temperature to include °C
    # find day and data data for minium and maximum temperature
    # check how many days in weather data
    # find average low and high temperature 
    # convert average low and high temperature from fahrenheit to celsius 
    # format average low and high temperature to include °C
    # return formate data

    min_list = []
    max_list = []
    day_list = []
    for list in weather_data:
        min_list.append(list[1])
        max_list.append(list[2])
        day_list.append(list[0])

    min_f = find_min(min_list)
    min_c = convert_f_to_c(min_f[0])
    format_min_c = format_temperature(min_c)

    min_day = convert_date(day_list[min_f[1]])

    max_f = find_max(max_list)
    max_c = convert_f_to_c(max_f[0])
    format_max_c = format_temperature(max_c)

    max_day = convert_date(day_list[max_f[1]])

    avg_min_f = calculate_mean(min_list)
    avg_min_c = convert_f_to_c(avg_min_f)
    format_avg_min_c = format_temperature(avg_min_c)
    
    avg_max_f = calculate_mean(max_list)
    avg_max_c = convert_f_to_c(avg_max_f)
    format_avg_max_c = format_temperature(avg_max_c)
    
    num_days = len(day_list)
    
    return f"{num_days} Day Overview\n" \
           f"  The lowest temperature will be {format_min_c}, and will occur on {min_day}.\n" \
           f"  The highest temperature will be {format_max_c}, and will occur on {max_day}.\n" \
           f"  The average low this week is {format_avg_min_c}.\n" \
           f"  The average high this week is {format_avg_max_c}.\n"


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # check how may days in the weather data lis
    # convert iso string
    # convert min temp from f to c
    # convert max temp from f to c
    # format summary information  
    
    num_0f_data = len(weather_data)

    day_list = []
    min_c_list = []
    max_c_list = []
    output = ""

    for i in range(num_0f_data):
        day = convert_date(weather_data[i][0])
        day_list.append(day)
        min_c = convert_f_to_c(weather_data[i][1])
        format_min_c = format_temperature(min_c)
        min_c_list.append(format_min_c)
        max_c = convert_f_to_c(weather_data[i][2])
        format_max_c = format_temperature(max_c)
        max_c_list.append(format_max_c)
        output += f"---- {day_list[i]} ----\n  Minimum Temperature: {min_c_list[i].strip()}\n  Maximum Temperature: {max_c_list[i].strip()}\n\n" 
    return output
