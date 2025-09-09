'''
Name: Eric and Sanvi
Last modified: May 21, 2025
Program details: An application that provides weather monitoring with a GUI from tkinter package.
                 It will read weather data from a file, automatically updates conditions at set intervals, and
                 dynamically display weather conditions (e.g., Sunny, Rainy, or Snowy).
'''
class Determine_Weather_Condition():
    """
    Allows the system to identify the weather condition based upon the values retrieved from the 
    text file. After identifying the weather condition, it initalizes get methods which will return the encapsulated
    strings.  
    """
    def __init__(self, weather_data, day):
        """
        Gets information by calling the get methods of get_weather_values, get_heat_index, get_wind_chill, and
        get_dew_point. Then, initalizes 8 variables to easily call these methods throughout the class.

        Parameters:
            weather_data: creates an object that is used to call the get methods (object)
            day: tells the system which day's information it should access (int)
        """
        self.__data = weather_data
        print("Day argument type:", day) #logs day information for easy tracking
        #object calls get methods from their respective classes and then stores the info in these variables
        self.__min, self.__max, self.__humidity, self.__speed, _, _ = self.__data.get_weather_values(day) 
        self.__heat_index = self.__data.get_heat_index()[day]
        self.__wind_chill = self.__data.get_wind_chill()[day]
        self.__dew_point = self.__data.get_dew_point()[day]

    def condition(self):
        """
        Checks to see if the if statements below are true so they can get added to 
        the weather and weather_description strings.
        Does not accept any parameters (other than self) and does not return anything.
        """
        weather = "" #empty string so that info can be added
        weather_description = "" #empty string so that info can be added
        if (self.__min >= 10) and (self.__max <= 20):
            weather += "Sunny!" + " "
            weather_description += "Clear skies, bright weather." + " "
        if (self.__speed <= 39) and (self.__humidity >= 60):
            weather += "Rainy!" + " "
            weather_description += "Overcast skies with percipitation." + " "
        if (self.__min <= 0) and (self.__humidity >= 50):
            weather += "Snowy!" + " "
            weather_description += "Snowfall and cold temperatures." + " "
        if (25<= self.__speed <= 39):
            weather += "Windy!" + " "
            weather_description+= "Strong wind without storms." + " "
        if (40<= self.__speed <= 88):
            weather += "Stormy!" + " "
            weather_description += "Thunderstorms with heavy rain." + " "
        if (89 <= self.__speed <= 118):
            weather += "Severe Windstorm!" + " "
            weather_description += "Violent wind conditions."
        if (119 <= self.__speed <= 176):
            weather += "Hurricane!" + " "
            weather_description += "Extremely high winds and storms." + " "
        if (self.__speed>=177):
            weather += "Tornado!" + " "
            weather_description += "Destructive swirling winds." + " "
        if (self.__min >= 40) or (self.__heat_index >= 41):
            weather += "Extreme Heat!" + " "
            weather_description += "Scorching hot temperatures." + " "
        if (self.__min <= -20) or (self.__wind_chill <= -30):
            weather += "Extreme Cold!" + " "
            weather_description += "Freezing and dangerously cold." + " "
        if (self.__dew_point >= 24):
            weather += "Dew Point!" + " "
            weather_description += "High moisture in the air." + " "
        if weather == "":
            weather += "Surprise!"
            weather_description += "Be prepared for anything!"
        
        #Removes extra space taht was added at the end
        self.__weather = weather.strip()
        self.__weather_description = weather_description.strip()

    def get_weather_condition(self):
        """
        Accessor method that retrieves and returns the self.__weather so that it can be
        accessed and used in other classes.
        Does not accept any parameters (other than self)

        Returns:
            self.__weather: instance variable that contains info about the condition (str)
        """
        return self.__weather
    
    def get_weather_description(self):
        """
        Accessor method that retrieves and returns the self.__weather_description 
        so that it can be accessed and used in other classes.
        Does not accept any parameters (other than self)

        Returns:
            self.__weather_description: instance variable that contains info 
            about the description of the weather (str)
        """
        return self.__weather_description