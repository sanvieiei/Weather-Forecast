'''
Name: Eric and Sanvi
Last modified: May 21, 2025
Program details: An application that provides weather monitoring with a GUI from tkinter package.
                 It will read weather data from a file, automatically updates conditions at set intervals, and
                 dynamically display weather conditions (e.g., Sunny, Rainy, or Snowy).
'''
class Weather_App_Data():
    """
    Retrieves and validates data from a text file so that it can be used 
    and displayed inside of the weather app.
    """
    def __init__(self):
        """
        Initalizes the Weather_Animation by creating a list and defining the order 
        of certain methods.
        Does not accept any parameters (other than self) and does not return anything.
        """
        self.__list_info = [] #creates list where the data will be stored
        #tells the computer the order in which to access the methods
        self.set_default_data()
        self.read_data()

    def set_default_data(self):
         """
         Sets default data (dic) which is appened to the list when the program is first run
         in case all of the data in the file is bad.
         Does not accept any parameters (other than self) and does not return anything.
         """
         for i in range(5): #hardcodes 5 default data for 5 days
            day = str(i+1) 
            date_str = "May " + day + ", 2025" #Writes dates in specific format
            self.__list_info.append({
                "Date": date_str,
                "Min Temperature": 12.0,
                "Max Temperature": 18.0,
                "Humidity": 50.0,
                "Wind Speed": 10.0,
                "Wind Direction": "N"
        })
    
    def read_data(self):
        """
        Reads and processes lines from 'data.txt', validating each data set using 
        helper functions and replacing default data with valid values.
        Does not accept any parameters (other than self) and does not return anything.
        """
        data = open("data.txt", 'r') #opens the file in read mode
        #initalisizes local variables to be used in loop
        record_item = 0
        record = {}
        validSet = True #flag to be used
        day = 0
        
        for info in data:
            result = self.parse_line(info) #uses helper function parse line
            if result is None:
                continue #skips over line
            key, value = result #get key and value info
            stats = self.check_weather_type(key, value) #completes validation sorting
            
            if(stats == None):
                validSet = False #changes flag state
            record[key] = stats
            record_item += 1

            if record_item == 6: #checks if 6 items are in record
                if(validSet == True):
                    self.__list_info[day] = record #replaces default if all data is valid
                #resets values to be used again in loop
                record = {}
                record_item = 0
                validSet = True
                day += 1
                    
        data.close()

    def parse_line(self, info):
        """
        Parses a single line from the data file into key-value format.

        Parameters:
            info: a raw line of data that has come from the txt file (str)
        Returns:
            key: describes what the info is for. Will be refereneced in the dic's key-value pair (str)
            value: contains the actual information. Will be refereneced in the dic's key-value pair (str)
            None: returned if the line is empty/has no colon (nonetype)
        """
        line =  info.strip()
               
        if not line or ':' not in line:
            return None

        index_colon = line.find(":")
        key = line[:index_colon] #strips colon
        value = line[index_colon + 1:].strip('Â°C%km/h').strip() #strips extra special characters
        return key, value

    def check_weather_type(self, key, value):
        """
        Determines and calls the appropriate validation function based on the data key.
        
        Parameters:
            key: the type of data (str)
            value: the information itself (str)
        Returns:
            self.validate_direction(value): returns value that was returned in this method (str or None)
            self.validate_date(value): returns value that was returned in this method (str or None)
        """
        #sorts data into different data type validations
        if key == "Wind Direction":
            return self.validate_direction(value)  
        elif key == "Date":
            return self.validate_date(value)             
        else:
            return self.validate_int(value)

    def validate_direction(self, value):
        """
        Validates if the wind direction is one of the allowed compass directions.
    
        Parameters:
            value: wind direction string (str)
        Returns:
            value if valid (str) or None if invalid (None)
        """
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        if value in directions: #checks if wind direction is in list
            return value
        else:
            return None

    def validate_int(self, value):
        """
        Converts a string to a float for numeric weather data.
    
        Parameters:
            value: numeric string (str)
        Returns:
            value if valid (float), or None if conversion fails (None)
        """
        try:
            return (float(value)) #checks if it is a number, etc
        except ValueError:
            return None
        
    def convert_date(self, value):
        """
        Converts a date from YYYY-MM-DD format to a readable format (e.g., "May 21, 2025").
    
        Parameters:
            value: date string in the format YYYY-MM-DD (str)
        Returns:
            Converted date in readable format (str)
        """
        #creates dictionary to replace numbers into words for months
        months = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }
        if value[8:][0] == "0":
            day = value[9] #removes leading 0 if present
        else:
            day = value[8:]
        #rewrites date into proper format
        new_date = months[value[5:7]] + " " + day + ", " + value[:4]
        return new_date
    
    def validate_date(self, value):
        """
        Validates that a date is in the correct format and converts it if valid.
    
        Parameters:
            value: date string (str)
        Returns:
            Converted date string if valid (str) or None if invalid
        """
        #checks if date in file is in yyyy-mm-dd
        if len(value) == 10 and (
            (value [4] == "-" and value[7] == "-") and(
                value[:4].isdigit() and value[5:7].isdigit() and value[8:].isdigit())):
            date = self.convert_date(value) #uses helper method to reformat
            return date
        else:
            return None
    
    def get_weather_values(self, dic_index):
        """
        Retrieves weather values for a specific day.
    
        Parameters:
            dic_index: index of the day in the list (int)
        Returns:
            min (float), max (float), humidity (float), 
            speed (float), direction (str), date (str)
        """
        #gets specific date from the list based upon day
        dic = self.__list_info[dic_index]
        date = dic.get("Date")
        min = dic.get("Min Temperature")
        max = dic.get("Max Temperature")
        humidity = dic.get("Humidity")
        speed = dic.get("Wind Speed")
        direction = dic.get("Wind Direction")

        return min, max, humidity, speed, direction, date
    
    def get_list(self):
        """
        Returns the internal list of weather data dictionaries.
        Does not accept any parameters (other than self)
        Returns:
            self.__list_info: List of dictionaries containing weather data (list)
        """
        return self.__list_info
    
class Weather_Calculations(Weather_App_Data):
    """
    Calculates the heat index, wind chill, and wind speed so that
    future weather condition determinination can be more accurate.
    """
    def __init__(self):
        """
        Initializes Weather_Calculations by computing heat index, wind chill, and dew point for all days.
        Also calls necessary methods so the program is aware tasks need to be completed in them.
        Does not accept any parameters (other than self) and does not return anything.
        """
        Weather_App_Data.__init__(self) #calls the init method of superclass for inheritance
        #creates lists for data to be appended and stored in once calculated
        self.__heat_index_list = []
        self.__wind_chill_list = []
        self.__dew_point_list = []

        self.heat_index()
        self.wind_chill()
        self.dew_point()

    def convert_wind_speed(self, old_speed):
        """
        Converts wind speed from km/h to m/s.

        Parameters:
            old_speed: wind speed in km/h (float)
        Returns:
            new_speed:Wind speed in m/s (float)
        """
        new_speed = old_speed * (5/18) #speed now in m/s
        return new_speed
            
    def heat_index(self):
        """
        Calculates the heat index for each day and stores it in a list.
        Does not accept any parameters (other than self) and does not return anything.
        """
        for dic in range(len(self.get_list())):
            #gets needed variables from get method
            _, max_temp, humid, speed, _,_ = self.get_weather_values(dic)
            new_speed = self.convert_wind_speed(speed) #gets changed windspeed
            #calculates heat index and appends
            heat = max_temp + (0.33*humid) - (0.7*new_speed)
            self.__heat_index_list.append(heat)

    def get_heat_index(self):
        """
        Returns the list of calculated heat index values.
        Does not accept any parameters (other than self)
        Returns:
            self.__heat_index_list: List of heat index values (list)
        """
        return self.__heat_index_list

    def wind_chill(self):
        """
        Calculates wind chill for each day and stores it in a list.
        Does not accept any parameters (other than self) and does not return anything.
        """
        for dic in range(len(self.get_list())):
            #gets needed variables from get method
            min_temp, _, _, speed, _,_ = self.get_weather_values(dic)
            new_speed = self.convert_wind_speed(speed) #gets changed windspeed
            #calculates wind chill and appends
            chill = 13.12 + (0.6215*min_temp) - (new_speed**0.16)*(11.37-min_temp)
            self.__wind_chill_list.append(chill)

    def get_wind_chill(self):
        """
        Returns the list of calculated wind chill values.
        Does not accept any parameters (other than self)
        Returns:
            self.__wind_chill_list: List of wind chill values (list)
        """
        return self.__wind_chill_list

    def dew_point(self):
        """
        Calculates dew point for each day and stores it in a list.
        Does not accept any parameters (other than self) and does not return anything.
        """
        for dic in range(len(self.get_list())):
            #gets needed variables from get method
            min_temp, max_temp, humid, _, _,_ = self.get_weather_values(dic)
            #calculates dew point and appends
            average = (min_temp+max_temp)/2
            dew = average - ((100-humid)/5)
            self.__dew_point_list.append(dew)
       
    def get_dew_point(self):
        """
        Returns the list of calculated dew point values.
        Does not accept any parameters (other than self)
        Returns:
            List of dew point values (list of float)
        """
        return self.__dew_point_list