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
    formatted_date = dt.strftime("%A %d %B %Y") # https://www.w3schools.com/python/python_datetime.asp https://stackoverflow.com/questions/65362378/extract-day-of-the-week-and-hour-from-iso-datetime-stamp-in-python
    return formatted_date

# print(convert_date("2021-07-02T07:00:00+08:00"))  # ISO sting 2021-07-02T07:00:00+08:00

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
    return round(temp_in_celsius, 1)

# print(convert_f_to_c(-10))

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0                            # set counter to 0
    for weather in weather_data:       # loop through each element in weather_data list
        float(weather)                 # convert weather into float
        sum = sum + float(weather)     # add each element to counter for sum 
        
    return sum / len(weather_data)     # divide sum by the number of the element to get mean value  

# print(calculate_mean(["51", "58", "59", "52", "52", "48", "47", "53"]))

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
                # print(row)
                weather_list.append([row[0], int(row[1]), int(row[2])])  # run_tests.py expect returning [['', int, int]]
        return weather_list

# print(load_data_from_csv("tests/data/example_one.csv"))

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # handle empty list
    if weather_data == []:
        return ()
    # change weather data to float
    updated_weather_data = [float(weather) for weather in weather_data]
    # step 1: check how many elements in the list
    total_elements = len(updated_weather_data)
    # step 2: set first element as the staring point to compare with the other elements in the list, and find out the minium vale 
    min_value = updated_weather_data[0]
    # step 4: compare each element in the list 
    # for i in range(total_elements):
    #     if min_value > updated_weather_data[i]:
    #         min_value = updated_weather_data[i]
    #         min_index = i
    # # print(min_value)
    # # step 5: find the last index of the minimum vale  
    last_index = -1
    for index, value in enumerate(updated_weather_data):  # https://stackoverflow.com/questions/24816669/find-the-minimum-value-in-a-python-list
        if min_value > value:
            min_value = value
        # print(index, value)
        if value == min_value:
            last_index = index
    # print(last_index)
    # print(f"The minimum value is {min_value} and the last position in the list is {last_index}")
    return (min_value, last_index) #run_tests.py expects returning tuple

# print(find_min([49, 57, 56, 55, 53, 49]))

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
    # print(max_value)

    # step 6: find the last index of the maximum vale
    last_index = -1    
    for key, value in enumerate(updated_weather_data):
        # print(key, value)
        if value == max_value:
            last_index = key
    # print(last_index)
    return (max_value, last_index)  #run_tests.py expects returning tuple

# print(find_max([49, 57, 56, 55, 53]))

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
        # print(list[0])
    # print(min_list)
    min_f = find_min(min_list)
    # print(min_f)
    min_c = convert_f_to_c(min_f[0])
    format_min_c = format_temperature(min_c)
    # print(min_c)
    min_day = convert_date(day_list[min_f[1]])
    # print(min_day)
    # print(max_list)
    max_f = find_max(max_list)
    max_c = convert_f_to_c(max_f[0])
    format_max_c = format_temperature(max_c)
    # print(max_c)
    max_day = convert_date(day_list[max_f[1]])
    # print(max_day)
    avg_min_f = calculate_mean(min_list)
    avg_min_c = convert_f_to_c(avg_min_f)
    format_avg_min_c = format_temperature(avg_min_c)
    # print(avg_min_c)
    avg_max_f = calculate_mean(max_list)
    avg_max_c = convert_f_to_c(avg_max_f)
    format_avg_max_c = format_temperature(avg_max_c)
    # print(avg_max_c)
    num_days = len(day_list)
    return f"{num_days} Day Overview\n  The lowest temperature will be {format_min_c}, and will occur on {min_day}.\n  The highest temperature will be {format_max_c}, and will occur on {max_day}.\n  The average low this week is {format_avg_min_c}.\n  The average high this week is {format_avg_max_c}.\n"


example = [
            ["2020-06-19T07:00:00+08:00", 47, 46],
            ["2020-06-20T07:00:00+08:00", 51, 67],
            ["2020-06-21T07:00:00+08:00", 58, 72],
            ["2020-06-22T07:00:00+08:00", 59, 71],
            ["2020-06-23T07:00:00+08:00", 52, 71],
            ["2020-06-24T07:00:00+08:00", 52, 67],
            ["2020-06-25T07:00:00+08:00", 48, 66],
            ["2020-06-26T07:00:00+08:00", 53, 66]
        ]

# print(generate_summary(example)) 

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # # convert iso string
    # print(convert_date(weather_data[0][0]))
    # # convert min temp from f to c
    # print(convert_f_to_c(weather_data[0][1]))
    # # convert max temp from f to c
    # print(convert_f_to_c(weather_data[0][2]))
    # # format summary information  
    num_0f_data = len(weather_data)
    # print(num_0f_data)

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


example = [
            ["2020-06-19T07:00:00+08:00", 47, 46],
            ["2020-06-20T07:00:00+08:00", 51, 67],
            ["2020-06-21T07:00:00+08:00", 58, 72],
            ["2020-06-22T07:00:00+08:00", 59, 71],
            ["2020-06-23T07:00:00+08:00", 52, 71],
            ["2020-06-24T07:00:00+08:00", 52, 67],
            ["2020-06-25T07:00:00+08:00", 48, 66],
            ["2020-06-26T07:00:00+08:00", 53, 66]
        ]
# print(generate_daily_summary(example))




    