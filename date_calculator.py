import datetime # Importing the datetime module


def difference_between_dates(date1, date2): # function to calculate the number of days between two given given dates
    """
    Calculate the number of days between two dates.

    Parameters:
    date1 (str): The first date in 'YYYY-MM-DD' format.
    date2 (str): The second date in 'YYYY-MM-DD' format.

    Returns:
    int: The number of days between these two  dates.
    """
    try:
        # Convert string dates to datetime objects
        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(date2,"%Y-%m-%d" )
        
        # Calculate the difference in days
        difference = abs((date2 - date1).days)
        return difference
    
    except ValueError:
        print(f"Error:  Please enter the dates in this format 'YYYY-MM-DD'.")
        return None


variable1 = difference_between_dates("2025-01-01", "2025-05-02") # example to find number of days from january
print(f"The number of days we last in this year are {variable1} days")
variable2 = difference_between_dates("2004-10-30", "2025-05-02") # example to find number of days from my birth date
print(f"The number of days i last  from my birth date up to now are {variable2} days")


   