import tkinter as tk
import math
import time

def create_clock_window():
    """
    Creates and manages a resizable analog clock window using Tkinter.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Analog Clock")
    # Set a minimum size for the window
    root.minsize(200, 200)

    # Create a canvas to draw the clock on
    canvas = tk.Canvas(root, bg="#ffffff")
    canvas.pack(expand=True, fill='both')

    # Global variables to store the clock items
    clock_face = None
    numbers = []
    hour_hand, minute_hand, second_hand = None, None, None
    center_dot = None
    
    def draw_clock(event=None):
        """
        Draws or redraws the clock elements, scaling them to the current canvas size.
        """
        # Clear the canvas of all previous drawings
        canvas.delete("all")
        
        # Get current canvas dimensions
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        
        # Determine the clock's size and center based on the smaller dimension
        size = min(width, height) - 20
        center_x = width / 2
        center_y = height / 2
        radius = size / 2

        # Draw the clock face
        canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            outline="#333333", width=8, fill="#ffffff"
        )
        
        # Draw numbers
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)
            x = center_x + (radius - 20) * math.cos(angle)
            y = center_y + (radius - 20) * math.sin(angle)
            canvas.create_text(x, y, text=str(i), font=("Helvetica", int(radius * 0.1), "bold"), fill="#555555")

        # Get current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Calculate angles for hands
        second_angle = (seconds / 60) * 360 - 90
        minute_angle = ((minutes + seconds / 60) / 60) * 360 - 90
        hour_angle = ((hours + minutes / 60) / 12) * 360 - 90

        # Hand lengths relative to radius
        second_length = radius * 0.85
        minute_length = radius * 0.7
        hour_length = radius * 0.55

        # Draw the second hand (red)
        second_x = center_x + second_length * math.cos(math.radians(second_angle))
        second_y = center_y + second_length * math.sin(math.radians(second_angle))
        canvas.create_line(center_x, center_y, second_x, second_y, fill="#ef4444", width=2, tags="hands")
        
        # Draw the minute hand
        minute_x = center_x + minute_length * math.cos(math.radians(minute_angle))
        minute_y = center_y + minute_length * math.sin(math.radians(minute_angle))
        canvas.create_line(center_x, center_y, minute_x, minute_y, fill="#555555", width=4, capstyle=tk.ROUND, tags="hands")

        # Draw the hour hand
        hour_x = center_x + hour_length * math.cos(math.radians(hour_angle))
        hour_y = center_y + hour_length * math.sin(math.radians(hour_angle))
        canvas.create_line(center_x, center_y, hour_x, hour_y, fill="#333333", width=6, capstyle=tk.ROUND, tags="hands")

        # Draw the center dot
        dot_radius = radius * 0.05
        canvas.create_oval(center_x - dot_radius, center_y - dot_radius, center_x + dot_radius, center_y + dot_radius, fill="#333333")

    def update_clock():
        """
        Updates only the hands of the clock.
        """
        # Get current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Get current canvas dimensions
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        
        # Determine the clock's center and radius based on the smaller dimension
        size = min(width, height) - 20
        center_x = width / 2
        center_y = height / 2
        radius = size / 2

        # Calculate angles for hands
        second_angle = (seconds / 60) * 360 - 90
        minute_angle = ((minutes + seconds / 60) / 60) * 360 - 90
        hour_angle = ((hours + minutes / 60) / 12) * 360 - 90

        # Hand lengths relative to radius
        second_length = radius * 0.85
        minute_length = radius * 0.7
        hour_length = radius * 0.55

        # Delete old hands
        canvas.delete("hands")

        # Draw the second hand (red)
        second_x = center_x + second_length * math.cos(math.radians(second_angle))
        second_y = center_y + second_length * math.sin(math.radians(second_angle))
        canvas.create_line(center_x, center_y, second_x, second_y, fill="#ef4444", width=2, tags="hands")
        
        # Draw the minute hand
        minute_x = center_x + minute_length * math.cos(math.radians(minute_angle))
        minute_y = center_y + minute_length * math.sin(math.radians(minute_angle))
        canvas.create_line(center_x, center_y, minute_x, minute_y, fill="#555555", width=4, capstyle=tk.ROUND, tags="hands")

        # Draw the hour hand
        hour_x = center_x + hour_length * math.cos(math.radians(hour_angle))
        hour_y = center_y + hour_length * math.sin(math.radians(hour_angle))
        canvas.create_line(center_x, center_y, hour_x, hour_y, fill="#333333", width=6, capstyle=tk.ROUND, tags="hands")
        
        # Schedule the next update after 1 second
        root.after(1000, update_clock)
        
    # Bind the draw_clock function to the <Configure> event, which is triggered on resize
    canvas.bind("<Configure>", draw_clock)
    
    # Start the continuous update loop for the hands
    update_clock()
    
    # Start the Tkinter event loop
    root.mainloop()

# Run the application
if __name__ == "__main__":
    create_clock_window()
