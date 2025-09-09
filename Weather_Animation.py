'''
Name: Eric and Sanvi
Last modified: May 21, 2025
Program details: An application that provides weather monitoring with a GUI from tkinter package.
                 It will read weather data from a file, automatically updates conditions at set intervals, and
                 dynamically display weather conditions (e.g., Sunny, Rainy, or Snowy).
'''
import tkinter as tk
from PIL import Image, ImageTk
from Determine_Weather_Condition import Determine_Weather_Condition

class WeatherAnimation:
    """
    Creates a default weather animation with a rotating image on a Tkinter canvas.
    Used as a fallback when specific weather condition animations are unavailable.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the WeatherAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0        
        self.__direction = 1  
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads default weather image
        try:
            img = Image.open("surprise.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
        except:
            self.__original_image = None
           
        #Starts animation
        self.animate()
   
    def animate(self):
        """
        Rotates the image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
       
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1  

        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
       
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class SunnyAnimation:
    """
    Creates an animation for sunny weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the SunnyAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads sunny weather image
        try:
            img = Image.open("sunny.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the sunny image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class RainyAnimation:
    """
    Creates an animation for rainy weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the RainyAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads rainy weather image
        try:
            img = Image.open("rainy.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the rainy image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class SnowyAnimation:
    """
    Creates an animation for snowy weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the SnowyAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads snowy weather image
        try:
            img = Image.open("snowy.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the snowy image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class WindyAnimation:
    """
    Creates an animation for windy weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the WindyAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads windy weather image
        try:
            img = Image.open("windy.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the windy image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class StormyAnimation:
    """
    Creates an animation for stormy weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the StormyAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads stormy weather image
        try:
            img = Image.open("stormy.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the stormy image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class TornadoAnimation:
    """
    Creates an animation for tornado weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the TornadoAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads tornado weather image
        try:
            img = Image.open("tornado.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the tornado image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class SevereWindstormAnimation:
    """
    Creates an animation for severe windstorm weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the SevereWindstormAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads severe windstorm image
        try:
            img = Image.open("severe_windstorm.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the severe windstorm image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class HurricaneAnimation:
    """
    Creates an animation for hurricane weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the HurricaneAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads hurricane weather image
        try:
            img = Image.open("hurricane.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the hurricane image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class ExtremeColdAnimation:
    """
    Creates an animation for extreme cold weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the ExtremeColdAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads extreme cold image
        try:
            img = Image.open("extreme_cold.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the extreme cold image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class ExtremeHeatAnimation:
    """
    Creates an animation for extreme heat weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the ExtremeHeatAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads extreme heat image
        try:
            img = Image.open("extreme_heat.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the extreme heat image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


class ExtremelyHumidAnimation:
    """
    Creates an animation for extremely humid weather with a rotating image on a Tkinter canvas.
    """
    def __init__(self, canvas, x, y):
        """
        Initializes the ExtremelyHumidAnimation with a canvas and position.

        Parameters:
            canvas: The Tkinter canvas to display the animation (tk.Canvas).
            x: The x-coordinate for the image center (int).
            y: The y-coordinate for the image center (int).
        """
        #Stores canvas and position
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        #Initializes animation parameters
        self.__angle = 0
        self.__direction = 1
        self.__animation_speed = 200
        self.__image_item = None
        self.__tk_image = None
       
        #Loads extremely humid image
        try:
            img = Image.open("extremely_humid.png").resize((120, 120))
            self.__original_image = img
            self.__tk_image = ImageTk.PhotoImage(img)
            self.__image_item = canvas.create_image(x, y, image=self.__tk_image)
            self.animate()
        except:
            #Falls back to default animation
            WeatherAnimation(canvas, x, y)
   
    def animate(self):
        """
        Rotates the extremely humid image back and forth between -15 and 15 degrees.
        """
        #Exits if no image is loaded
        if self.__original_image is None:
            return
           
        #Updates rotation angle
        self.__angle += 5 * self.__direction
        #Reverses direction at angle limits
        if self.__angle >= 15:
            self.__direction = -1
        elif self.__angle <= -15:
            self.__direction = 1
           
        #Applies rotation and updates canvas
        rotated_img = self.__original_image.rotate(self.__angle)
        self.__tk_image = ImageTk.PhotoImage(rotated_img)
        self.__canvas.itemconfig(self.__image_item, image=self.__tk_image)
        #Schedules next animation frame
        self.__canvas.after(self.__animation_speed, self.animate)

    def get_canvas(self):
        """
        Retrieves the canvas used for the animation.

        Returns:
            __canvas: The Tkinter canvas (tk.Canvas).
        """
        return self.__canvas
       
    def get_position(self):
        """
        Retrieves the image position.

        Returns:
            __x, __y: A tuple of x and y coordinates (tuple).
        """
        return (self.__x, self.__y)
       
    def get_angle(self):
        """
        Retrieves the current rotation angle.

        Returns:
            __angle: The rotation angle in degrees (int).
        """
        return self.__angle
       
    def get_image_item(self):
        """
        Retrieves the canvas image item.

        Returns:
            __image_item: The canvas image item identifier (int).
        """
        return self.__image_item


def create_weather_animation(condition, canvas, x=150, y=250):
    """
    Creates an animation object based on the specified weather condition.

    Parameters:
        condition: The weather condition to determine the animation type (str).
        canvas: The Tkinter canvas to display the animation (tk.Canvas).
        x: The x-coordinate for the image center, default is 150 (int).
        y: The y-coordinate for the image center, default is 250 (int).

    Returns:
        animation: An instance of the appropriate animation class (object).
    """
    #Logs the animation condition
    print("Animation condition:", condition)
    #Selects animation based on condition
    if "Sunny!" in condition:
        return SunnyAnimation(canvas, x, y)
    elif "Rainy!" in condition:
        return RainyAnimation(canvas, x, y)
    elif "Snowy!" in condition:
        return SnowyAnimation(canvas, x, y)
    elif "Windy!" in condition:
        return WindyAnimation(canvas, x, y)
    elif "Stormy!" in condition:
        return StormyAnimation(canvas, x, y)
    elif "Tornado!" in condition:
        return TornadoAnimation(canvas, x, y)
    elif "Severe Windstorm!" in condition:
        return SevereWindstormAnimation(canvas, x, y)
    elif "Hurricane!" in condition:
        return HurricaneAnimation(canvas, x, y)
    elif "Extreme Cold!" in condition:
        return ExtremeColdAnimation(canvas, x, y)
    elif "Extreme Heat!" in condition:
        return ExtremeHeatAnimation(canvas, x, y)
    elif "Dew Point!" in condition:
        return ExtremelyHumidAnimation(canvas, x, y)
    else:
        #Falls back to default animation
        return WeatherAnimation(canvas, x, y)