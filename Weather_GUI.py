'''
Name: Eric and Sanvi
Last modified: May 21, 2025
Program details: An application that provides weather monitoring with a GUI from tkinter package.
                 It will read weather data from a file, automatically updates conditions at set intervals, and
                 dynamically display weather conditions (e.g., Sunny, Rainy, or Snowy).
'''
import tkinter as tk
from PIL import Image, ImageTk
import Weather_App_Data
from Determine_Weather_Condition import Determine_Weather_Condition
from Weather_Animation import create_weather_animation

class Weather_Gui(Weather_App_Data.Weather_Calculations):
    """
    Creates and manages a Tkinter-based GUI for a weather monitoring application.
    Inherits from Weather_App_Data.Weather_Calculations to access weather data and calculations.
    Displays weather conditions, a 5-day forecast, and animations, with automatic data updates.
    """
    def __init__(self):
        """
        Initializes the Weather_Gui, setting up the main window, frames, and initial display.
        Starts the Tkinter main loop and schedules periodic data refresh.
        """
        #Initializes the parent class for weather calculations
        Weather_App_Data.Weather_Calculations.__init__(self)
        #Creates the main Tkinter window
        self.main_window = tk.Tk()
        #Sets the window title
        self.main_window.title("WeatherApp")
        #Disables window resizing
        self.main_window.resizable(False, False)

        #Initializes the GUI frames
        self.init_frames()
        #Sets up the top screen canvas
        self.init_top_screen()
        #Sets up the sidebar canvas
        self.init_side_bar()
        #Initializes the bottom buttons and forecast
        self.init_bottom_buttons()
        #Sets the current info to None initially
        self.__current_info = None
        #Schedules periodic data refresh
        self.schedule_refresh()
        #Sets the warning text to None initially
        self.warning = None
        #Displays info for the first day if data exists
        if len(self.get_list()) > 0:
            self.show_info(self.get_list()[0])

        #Starts the Tkinter main loop
        self.main_window.mainloop()
   
    def determine_condition(self, day_index):
        """
        Determines the weather condition and description for a specified day.

        Parameters:
            day_index: The index of the day in the weather data list (int).

        Returns:
            condition, description: A tuple containing the weather condition (str) and description (str).
        """
        #Creates a weather condition object for the specified day
        weather_info = Determine_Weather_Condition(self, day_index)
        #Determines the weather condition
        weather_info.condition()
        #Gets the weather condition string
        condition = weather_info.get_weather_condition()
        #Gets the weather description
        description = weather_info.get_weather_description()

        #Defines valid weather conditions
        valid_conditions = [
            "Sunny!", "Rainy!", "Snowy!", "Windy!", "Stormy!",
            "Tornado!", "Severe Windstorm!", "Hurricane!",
            "Extreme Cold!", "Extreme Heat!", "Dew Point!"
        ]
       
        #Checks if the condition is valid
        contains_valid = False
        for valid in valid_conditions:
            if valid in condition:
                contains_valid = True
                break

        #Sets a default condition if invalid or empty
        if not condition or not contains_valid:
            condition = "Surprise!"

        #Updates the condition in the data list
        self.get_list()[day_index]["Condition"] = condition
        #Returns the condition and description
        return condition, description
   
    def load_and_place_image(self, canvas, image_path, x, y, size=(50, 50), bg_color="#FFFBF1"):
        """
        Loads an image and places it on a Tkinter canvas at specified coordinates.

        Parameters:
            canvas: The Tkinter canvas to place the image on (tk.Canvas).
            image_path: The name of the image to load (str).
            x: The x-coordinate for placing the image (int).
            y: The y-coordinate for placing the image (int).
            size: The size to resize the image to, default is (50, 50) (tuple).
            bg_color: The background color of the label, default is "#FFFBF1" (str).

        Returns:
            success: True if the image was loaded and placed successfully, False otherwise (bool).
        """
        try:
            #Loads and resizes the image
            img = Image.open(image_path).resize(size)

            #Converts the image to a Tkinter-compatible format
            photo_img = ImageTk.PhotoImage(img)
           
            #Initializes the image references list if not present
            if not hasattr(self, 'image_references'):
                self.__image_references = []
            #Stores the image reference to prevent garbage collection
            self.__image_references.append(photo_img)

            #Creates a label to display the image
            label = tk.Label(canvas, image=photo_img, bg=bg_color)
            #Stores the image reference in the label
            label.image = photo_img
            #Places the label on the canvas
            label.place(x=x, y=y)
            #Indicates successful image loading
            return True
        except:
            #Indicates failed image loading
            return False

    def place_weather_images(self, canvas, condition, start_x, y, weather_images):
        """
        Places weather-related images on a canvas based on the weather condition.

        Parameters:
            canvas: The Tkinter canvas to place images on (tk.Canvas).
            condition: The weather condition to determine which images to display (str).
            start_x: The starting x-coordinate for placing images (int).
            y: The y-coordinate for placing images (int).
            weather_images: A dictionary mapping conditions to image names (dict).
        """
        #Sets the initial x-coordinate for image placement
        x_offset = start_x
        #Iterates through weather images to find matching conditions
        for tag in weather_images:
            if tag in condition:
                #Loads and places the matching image
                self.load_and_place_image(canvas, weather_images[tag], x_offset, y)
                #Increments the x-coordinate for the next image
                x_offset += 80

    def get_square_coords(self):
        """
        Provides coordinates for five rectangular areas in the 5-day forecast display.

        Returns:
            coords: A list of tuples containing (x1, y1, x2, y2) coordinates for each rectangle (list).
        """
        #Returns predefined coordinates for forecast rectangles
        return [
            (30, 60, 234, 270),
            (264, 60, 468, 270),
            (498, 60, 702, 270),
            (732, 60, 936, 270),
            (966, 60, 1170, 270)
        ]

    def simple_click_handler(self, event):
        """
        Handles mouse click events on the forecast canvas to display the selected day's information.

        Parameters:
            event: The Tkinter event object containing click coordinates (tk.Event).
        """
        #Gets the x and y coordinates of the click
        x_click = event.x
        y_click = event.y

        #Checks if the click is within any forecast rectangle
        for rect in self.__squares:
            x1, y1, x2, y2, info = rect
            if x1 <= x_click <= x2 and y1 <= y_click <= y2:
                #Displays info for the clicked day
                self.show_info(info)
                break

    def create_data_rectangle(self, canvas, x1, y1, x2, y2, title, value, icon=None):
        """
        Creates a rectangular box on a canvas to display weather data with an optional icon.

        Parameters:
            canvas: The Tkinter canvas to draw the rectangle on (tk.Canvas).
            x1: The x-coordinate of the top-left corner (int).
            y1: The y-coordinate of the top-left corner (int).
            x2: The x-coordinate of the bottom-right corner (int).
            y2: The y-coordinate of the bottom-right corner (int).
            title: The title of the data to display (str).
            value: The value of the data to display (str).
            icon: The name of an icon image, default is None (str).
        """
        #Draws a rectangle for the data box
        canvas.create_rectangle(
            x1, y1, x2, y2,
            fill="#edf2fb", outline="#5FA8D3", width=2
        )
       
        #Calculates the center x-coordinate and text positions
        center_x = (x1 + x2) // 2
        text_y = y1 + 30
        value_y = y1 + 60
        icon_y = y1 + 90
       
        #Adds the title text to the rectangle
        canvas.create_text(
            center_x, text_y, text=title, font=("Tahoma", 14, "underline"), fill="#2B5876"
        )
        #Adds the value text to the rectangle
        canvas.create_text(
            center_x, value_y, text=value, font=("Tahoma", 14), fill="#2B5876"
        )
   
        #Adds an icon to the rectangle if provided
        if icon:
            icon_x = center_x - 20
            self.load_and_place_image(canvas, icon, icon_x, icon_y, size=(40, 40), bg_color="#edf2fb")

    def weather_warning_bar(self, condition):
        """
        Displays a weather warning bar at the top of the GUI based on the condition.

        Parameters:
            condition: The weather condition to determine the warning message and color (str).
        """
        #Cancels any existing text animation
        if hasattr(self, 'anim_id'):
            self.top_canvas.after_cancel(self.anim_id)
        #Clears the top canvas
        self.top_canvas.delete("all")
       
        #Displays a warning or no-warning message based on condition
        if ("Extreme" not in condition) and ("Severe" not in condition):
            self.top_canvas.create_rectangle(0, 0, 900, 50, fill='#007ea7', outline='#007ea7')
            self.warning = self.top_canvas.create_text(450, 25, text="No Weather Warning Today!", font=("Tahoma", 15, "bold"), fill="#FFFBF1")
        else:
            self.top_canvas.create_rectangle(0, 0, 900, 50, fill='#e63946', outline='#e63946')
            self.warning = self.top_canvas.create_text(450, 25, text="Severe Weather Today!", font=("Tahoma", 15, "bold"), fill="#FFFBF1")

        #Sets the initial text movement direction
        self.__dx = 2
        #Starts the text animation
        self.animate_text()

    def animate_text(self):
        """
        Animates the warning text by moving it horizontally across the top canvas.
        """
        #Moves the warning text
        self.top_canvas.move(self.warning, self.__dx, 0)
        #Gets the current position of the text
        pos = self.top_canvas.coords(self.warning)

        #Reverses the text direction at canvas boundaries
        x = pos[0]
        if x <= 140 or x >= 760:
            self.__dx = -self.__dx
        #Schedules the next animation frame
        self.anim_id = self.top_canvas.after(10, self.animate_text)
   
    def init_bottom_buttons(self):
        """
        Initializes the bottom section of the GUI with the 5-day forecast.
        """
        #Sets up the bottom canvas
        self.setup_bottom_canvas()
        #Gets the weather images dictionary
        weather_images = self.get_weather_images()
        #Creates the forecast day displays
        self.create_forecast_days(weather_images)
        #Sets up the click handler for the forecast
        self.setup_click_handler()

    def setup_bottom_canvas(self):
        """
        Sets up the bottom canvas for the 5-day forecast display.
        """
        #Destroys the existing bottom canvas if it exists
        if hasattr(self, 'bottom_canvas'):
            self.bottom_canvas.destroy()
        #Creates a new bottom canvas
        self.bottom_canvas = tk.Canvas(self.bottom_frame, width=1200, height=300, bg="#5FA8D3")
        #Packs the bottom canvas
        self.bottom_canvas.pack()
        #Draws the canvas background
        self.draw_canvas_background()
        #Adds the forecast title
        self.add_forecast_title()

    def draw_canvas_background(self):
        """
        Draws the background rectangle for the bottom canvas.
        """
        #Creates a filled rectangle for the bottom canvas background
        self.bottom_canvas.create_rectangle(0, 0, 1200, 300, fill='#cae9ff', outline='#cae9ff')

    def add_forecast_title(self):
        """
        Adds the "5 Day Forecast" title to the bottom canvas.
        """
        #Creates the forecast title text
        self.bottom_canvas.create_text(600, 30, text="5 Day Forecast",
                                     font=("Tahoma", 16, "underline"), fill="#2B5876")

    def get_weather_images(self):
        """
        Provides a dictionary mapping weather conditions to their corresponding images.

        Returns:
            weather_images: A dictionary with weather conditions as keys and image names as values (dict).
        """
        #Defines and returns the weather images dictionary
        return {
            "Sunny!": "sunny.png",
            "Rainy!": "rainy.png",
            "Snowy!": "snowy.png",
            "Windy!": "windy.png",
            "Stormy!": "stormy.png",
            "Tornado!": "tornado.png",
            "Severe Windstorm!": "severe_windstorm.png",
            "Hurricane!": "hurricane.png",
            "Extreme Cold!": "extreme_cold.png",
            "Extreme Heat!": "extreme_heat.png",
            "Dew Point!": "extremely_humid.png",
            "Surprise!": "surprise.png"
        }

    def create_forecast_days(self, weather_images):
        """
        Creates the display for the 5-day forecast on the bottom canvas.

        Parameters:
            weather_images: A dictionary mapping conditions to image names (dict).
        """
        #Gets the coordinates for forecast rectangles
        square_coords = self.get_square_coords()
        #Initializes the squares list for storing rectangle info
        self.__squares = []
       
        #Creates a display for each forecast day
        for day_index in range(5):
            self.create_single_day(day_index, square_coords[day_index], weather_images)

    def create_single_day(self, day_index, coords, weather_images):
        """
        Creates the display for a single day in the 5-day forecast.

        Parameters:
            day_index: The index of the day in the weather data list (int).
            coords: The coordinates (x1, y1, x2, y2) for the day's rectangle (tuple).
            weather_images: A dictionary mapping conditions to image names (dict).
        """
        #Unpacks the rectangle coordinates
        x1, y1, x2, y2 = coords
        #Gets the weather info for the day
        info = self.get_day_info(day_index)
        #Gets the weather condition for the day
        condition = self.get_day_condition(day_index, info)
       
        #Draws the day box
        self.draw_day_box(x1, y1, x2, y2)
        #Adds text for the day
        self.add_day_text(x1, y1, x2, y2, day_index, condition)
        #Adds the weather image
        self.add_weather_image(x1, y1, condition, weather_images)
       
        #Stores the rectangle info
        self.store_square_info(x1, y1, x2, y2, info)

    def get_day_info(self, day_index):
        """
        Retrieves weather information for a specific day.

        Parameters:
            day_index: The index of the day in the weather data list (int).

        Returns:
            info: A dictionary containing weather data for the specified day (dict).
        """
        #Returns the weather data for the specified day
        return self.get_list()[day_index]

    def get_day_condition(self, day_index, info):
        """
        Gets the weather condition for a specific day, updating the info if necessary.

        Parameters:
            day_index: The index of the day in the weather data list (int).
            info: The weather data dictionary for the day (dict).

        Returns:
            condition: The weather condition for the day (str).
        """
        #Determines the weather condition
        condition, _ = self.determine_condition(day_index)
        #Updates the condition in the info dictionary if missing
        if "Condition" not in info:
            info["Condition"] = condition
        #Returns the condition
        return condition

    def draw_day_box(self, x1, y1, x2, y2):
        """
        Draws a rectangular box for a single day in the forecast.

        Parameters:
            x1: The x-coordinate of the top-left corner (int).
            y1: The y-coordinate of the top-left corner (int).
            x2: The x-coordinate of the bottom-right corner (int).
            y2: The y-coordinate of the bottom-right corner (int).
        """
        #Creates a rectangle for the day box
        self.bottom_canvas.create_rectangle(x1, y1, x2, y2, fill="#FFFBF1", outline="#FFFBF1")

    def add_day_text(self, x1, y1, x2, y2, day_index, condition):
        """
        Adds text to a day's forecast box, including date, condition, and temperatures.

        Parameters:
            x1: The x-coordinate of the top-left corner (int).
            y1: The y-coordinate of the top-left corner (int).
            x2: The x-coordinate of the bottom-right corner (int).
            y2: The y-coordinate of the bottom-right corner (int).
            day_index: The index of the day in the weather data list (int).
            condition: The weather condition for the day (str).
        """
        #Calculates the center coordinates for text placement
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
       
        #Gets the weather data for the day
        day_data = self.get_list()[day_index]
        #Defines the text elements to display
        texts = [
            ("Day " + str(day_index + 1) + ": " + day_data.get("Date"), center_y - 70, ("Tahoma", 14, "underline")),
            (condition, center_y - 38, ("Tahoma", 13)),
            ("Min Temp: " + str(day_data.get("Min Temperature")) + "°C", center_y - 13, ("Tahoma", 13)),
            ("Max Temp: " + str(day_data.get("Max Temperature")) + "°C", center_y + 12, ("Tahoma", 13))
        ]
       
        #Adds each text element to the canvas
        for text, y_pos, font in texts:
            self.bottom_canvas.create_text(center_x, y_pos, text=text, font=font, fill="black")

    def add_weather_image(self, x, y, condition, weather_images):
        """
        Adds a weather image to a day's forecast box.

        Parameters:
            x: The x-coordinate for image placement (int).
            y: The y-coordinate for image placement (int).
            condition: The weather condition to determine the image (str).
            weather_images: A dictionary mapping conditions to image names (dict).
        """
        #Places the weather image for the condition
        self.place_weather_images(self.bottom_canvas, condition, x + 40, y + 140, weather_images)

    def store_square_info(self, x1, y1, x2, y2, info):
        """
        Stores information about a forecast rectangle for click handling.

        Parameters:
            x1: The x-coordinate of the top-left corner (int).
            y1: The y-coordinate of the top-left corner (int).
            x2: The x-coordinate of the bottom-right corner (int).
            y2: The y-coordinate of the bottom-right corner (int).
            info: The weather data for the day (dict).
        """
        #Appends the rectangle coordinates and info to the squares list
        self.__squares.append((x1, y1, x2, y2, info))

    def setup_click_handler(self):
        """
        Sets up the click handler for the bottom canvas to handle forecast day selection.
        """
        #Binds the click event to the click handler
        self.bottom_canvas.bind("<Button>", self.simple_click_handler)
   
    def close(self):
        """
        Closes the main window and terminates the application.
        """
        #Stops the Tkinter main loop
        self.main_window.quit()
        #Destroys the main window
        self.main_window.destroy()
   
    def setup_sidebar_content(self, day_index, condition, description):
        """
        Sets up the sidebar content with the date, condition, animation, and description.

        Parameters:
            day_index: The index of the day in the weather data list (int).
            condition: The weather condition for the day (str).
            description: The description of the weather condition (str).
        """
        #Clears the sidebar canvas
        self.side_canvas.delete("all")
        #Creates a weather animation for the condition
        self.weather_animation = create_weather_animation(condition, self.side_canvas, 150, 250)
        #Adds the date text to the sidebar
        self.side_canvas.create_text(150, 60, text=(self.get_list()[day_index].get("Date")),
                                    font=("Tahoma", 23), fill="black")
        #Adds the condition text to the sidebar
        self.side_canvas.create_text(150, 130, text=condition,
                                    font=("Tahoma", 19), fill="black")
        #Adds the description text to the sidebar
        self.side_canvas.create_text(150, 385, text=description,
                                    font=("Tahoma", 16), fill="black", width=260, justify="center")

    def create_quit_button(self):
        """
        Creates a quit button on the top canvas to close the application.
        """
        #Creates a quit button
        quit_button = tk.Button(self.top_canvas, text="Quit", command=self.close,
                               bg="#e63946", font=("Tahoma", 10, "bold"))
        #Places the quit button on the canvas
        self.top_canvas.create_window(800, 100, window=quit_button)

    def create_forecast_title(self):
        """
        Adds the "Today's Forecast" title to the top canvas.
        """
        #Creates the forecast title text
        self.top_canvas.create_text(450, 100, text="Today's Forecast:",
                                  font=("Tahoma", 18, "bold"), fill="#edf2fb")

    def get_data_icons(self):
        """
        Provides a dictionary mapping weather data types to their corresponding icons.

        Returns:
            data_icons: A dictionary with data types as keys and icon names as values (dict).
        """
        #Defines and returns the data icons dictionary
        data_icons = {
            "Min Temperature": "minimum_temperature.png",
            "Max Temperature": "maximum_temperature.png",
            "Wind Speed": "wind_speed.png",
            "Humidity": "humidity.png",
            "Wind Direction": "wind_direction.png",
            "Heat Index": "heat_index.png",
            "Wind Chill": "wind_chill.png",
            "Dew Point": "dew_point.png"}
        return data_icons
   
    def setup_data_rectangles(self, info, day_index):
        """
        Sets up data rectangles on the top canvas to display weather information.

        Parameters:
            info: The weather data for the day (dict).
            day_index: The index of the day in the weather data list (int).
        """
        #Sets the dimensions for data rectangles
        box_width = 180
        box_height = 150
        start_x = 60
        start_y = 140
       
        #Creates a rectangle for min temperature
        self.create_data_rectangle(
            self.top_canvas, start_x, start_y, start_x+box_width, start_y+box_height,
            "Min Temperature", str(info.get("Min Temperature")) + "°C", self.get_data_icons()["Min Temperature"])
        #Creates a rectangle for max temperature
        self.create_data_rectangle(
            self.top_canvas, start_x+box_width+20, start_y, start_x+2*box_width+20, start_y+box_height,
            "Max Temperature", str(info.get("Max Temperature")) + "°C", self.get_data_icons()["Max Temperature"])
        #Creates a rectangle for wind speed
        self.create_data_rectangle(
            self.top_canvas, start_x+2*box_width+40, start_y, start_x+3*box_width+40, start_y+box_height,
            "Wind Speed", str(info.get("Wind Speed")) + " km/h", self.get_data_icons()["Wind Speed"])
        #Creates a rectangle for humidity
        self.create_data_rectangle(
            self.top_canvas, start_x+3*box_width+60, start_y, start_x+4*box_width+60, start_y+box_height,
            "Humidity", str(info.get("Humidity")) + "%", self.get_data_icons()["Humidity"])
        #Creates a rectangle for wind direction
        self.create_data_rectangle(
            self.top_canvas, start_x, start_y+box_height+20, start_x+box_width, start_y+2*box_height+20,
            "Wind Direction", info.get("Wind Direction"), self.get_data_icons()["Wind Direction"])
        #Creates a rectangle for heat index
        self.create_data_rectangle(
            self.top_canvas, start_x+box_width+20, start_y+box_height+20, start_x+2*box_width+20, start_y+2*box_height+20,
            "Heat Index", "%.2f°C" % self.get_heat_index()[day_index], self.get_data_icons()["Heat Index"])
        #Creates a rectangle for wind chill
        self.create_data_rectangle(
            self.top_canvas, start_x+2*box_width+40, start_y+box_height+20, start_x+3*box_width+40, start_y+2*box_height+20,
            "Wind Chill", "%.2f°C" % self.get_wind_chill()[day_index], self.get_data_icons()["Wind Chill"])
        #Creates a rectangle for dew point
        self.create_data_rectangle(
            self.top_canvas, start_x+3*box_width+60, start_y+box_height+20, start_x+4*box_width+60, start_y+2*box_height+20,
            "Dew Point", "%.2f°C" % self.get_dew_point()[day_index], self.get_data_icons()["Dew Point"])

    def show_info(self, info):
        """
        Displays detailed weather information for a selected day.

        Parameters:
            info: The weather data for the day to display (dict).
        """
        #Stores the current day's info
        self.__current_info = info
        #Clears the top canvas
        self.top_canvas.delete("all")
        #Gets the index of the current day
        day_index = self.get_list().index(info)
       
        #Determines the weather condition and description
        condition, description = self.determine_condition(day_index)
        #Updates the weather warning bar
        self.weather_warning_bar(condition)
       
        #Sets up the sidebar content
        self.setup_sidebar_content(day_index, condition, description)
        #Creates the quit button
        self.create_quit_button()
        #Adds the forecast title
        self.create_forecast_title()
        #Sets up the data rectangles
        self.setup_data_rectangles(info, day_index)
   
    def init_top_screen(self):
        """
        Initializes the top canvas for displaying weather information.
        """
        #Creates the top canvas
        self.top_canvas = tk.Canvas(self.top_frame, width=900, height=500, bg="#5FA8D3")
        #Packs the top canvas
        self.top_canvas.pack(side='left')
       
    def init_side_bar(self):
        """
        Initializes the sidebar canvas for displaying animations and details.
        """
        #Creates the sidebar canvas
        self.side_canvas = tk.Canvas(self.top_subframe, width=300, height=500, bg="#A8DCF6")
        #Packs the sidebar canvas
        self.side_canvas.pack(side='left')
   
    def init_frames(self):
        """
        Initializes the main frames for the GUI layout.
        """
        #Creates the top frame
        self.top_frame = tk.Frame(self.main_window)
        #Creates the top subframe
        self.top_subframe = tk.Frame(self.top_frame)
        #Creates the bottom frame
        self.bottom_frame = tk.Frame(self.main_window)
       
        #Packs the top frame
        self.top_frame.pack()
        #Packs the top subframe
        self.top_subframe.pack(side='left')
        #Packs the bottom frame
        self.bottom_frame.pack()

    def refresh_data(self):
        """
        Refreshes the weather data and updates the GUI display.
        """
        #Reads new weather data
        self.read_data()
        #Clears the heat index list
        self.get_heat_index().clear()
        #Clears the wind chill list
        self.get_wind_chill().clear()
        #Clears the dew point list
        self.get_dew_point().clear()
   
        #Recalculates the heat index
        self.heat_index()
        #Recalculates the wind chill
        self.wind_chill()
        #Recalculates the dew point
        self.dew_point()
       
        #Updates the display with current or first day's info
        if hasattr(self, "current_info") and self.__current_info in self.get_list():
            self.show_info(self.__current_info)
        else:
            self.show_info(self.get_list()[0])
        #Reinitializes the bottom buttons
        self.init_bottom_buttons()
   
    def schedule_refresh(self):
        """
        Schedules a periodic refresh of the weather data every minute.
        """
        #Schedules the refresh every 60 seconds
        self.main_window.after(60000, self.refresh_every_minute)

    def refresh_every_minute(self):
        """
        Refreshes the data and reschedules the next refresh.
        """
        #Refreshes the weather data
        self.refresh_data()
        #Reschedules the next refresh
        self.schedule_refresh()
         
#Creates an instance of the Weather_Gui class to run the application
Weather_Gui()