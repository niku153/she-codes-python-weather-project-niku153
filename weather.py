import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):

    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    dt = datetime.fromisoformat(iso_string)
    return dt.strftime("%A %d %B %Y")
    
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # pass


def convert_f_to_c(temp_in_farenheit):
    temperature_in_celsius = (float(temp_in_farenheit) - 32)*(5/9)
    rounded_temp_celsius = float(f"{temperature_in_celsius:.1f}")
    return rounded_temp_celsius

    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    # pass


def calculate_mean(weather_data):
    new_list = [float(item) for item in weather_data]
    return (sum(new_list))/len(new_list)

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # pass


def load_data_from_csv(csv_file):
    with open(csv_file) as file:
        next(file)
        reader = csv.reader(file)
        data = []
        for line in reader:
            if len(line) != 0:
                data.append([line[0], int(line[1]), int(line[2])])
    
    return data
    
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # pass


def find_min(weather_data):
    if len(weather_data) == 0:
        return ()
    min_value = float(weather_data[0])
    i = 0
    min_index = 0
    for value in weather_data:
        value_float = float(value)
        if value_float <= min_value:
            min_value = value_float
            min_index = i
        i += 1

    return min_value, min_index

    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    # pass


def find_max(weather_data):
    if len(weather_data) == 0:
        return ()
    max_value = float(weather_data[0])
    i = 0
    max_index = 0
    for value in weather_data:
        value_float = float(value)
        if value_float >= max_value:
            max_value = value_float
            max_index = i
        i += 1

    return max_value, max_index

    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):

    #create list of min values
    minimum_values = []
    for item in weather_data:
        minimum_values.append(item[1])
    #find and format min value
    min_value = (find_min(minimum_values))
    min_value_c = format_temperature(convert_f_to_c(min_value[0]))
    #find and format min value date
    index_min = min_value[1]
    min_date = weather_data[index_min]
    formatted_min_date = convert_date(min_date[0])
    #find and format mean min value
    mean_min_value_c = format_temperature(convert_f_to_c(calculate_mean(minimum_values)))
    
    #create list of max values
    maximum_values = []
    for item in weather_data:
        maximum_values.append(item[2])
    #find and format min value
    max_value = (find_max(maximum_values))
    max_value_c = format_temperature(convert_f_to_c(max_value[0]))
    #find and format min value date
    index_max = max_value[1]
    max_date = weather_data[index_max]
    formatted_max_date = convert_date(max_date[0])
    #find and format mean min value
    mean_max_value_c = format_temperature(convert_f_to_c(calculate_mean(maximum_values)))
    #number of days
    number_of_days = len(maximum_values)

    #final string
    summary_text = f"{number_of_days} Day Overview\n  The lowest temperature will be {min_value_c}, and will occur on {formatted_min_date}.\n  The highest temperature will be {max_value_c}, and will occur on {formatted_max_date}.\n  The average low this week is {mean_min_value_c}.\n  The average high this week is {mean_max_value_c}.\n"

    return summary_text

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # pass


def generate_daily_summary(weather_data):

    #create empty list and empty string
    daily_summary = []
    final_result = ''

    #loop through each list in weather_data to extract date, min, max and create separate lists for each day
    for item in weather_data:
        formatted_date = convert_date(item[0])
        min_temp = format_temperature(convert_f_to_c(item[1]))
        max_temp = format_temperature(convert_f_to_c(item[2]))
        daily_summary.append([formatted_date, min_temp, max_temp])

    #for each list in daily_summary, add formatted string on to existing string
    for individual_day in daily_summary:
        final_result += f"---- {individual_day[0]} ----\n  Minimum Temperature: {individual_day[1]}\n  Maximum Temperature: {individual_day[2]}\n\n"

    return final_result
    
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # pass
