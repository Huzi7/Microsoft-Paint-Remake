import tkinter as tk
from tkinter import Toplevel

def start_draw(event):
    """Start drawing when the left mouse button is pressed."""
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def draw(event):
    """Draw lines when the mouse is moved with the left button held down."""
    global prev_x, prev_y
    if brush_type == 'highlighter':  # makes rectangles, which have like 50% opacity
        canvas.create_rectangle(prev_x, prev_y, event.x, event.y, fill=color, outline='', width=0, stipple='gray50')
    elif brush_type == 'eraser':  # erase by drawing with the background color
        canvas.create_rectangle(prev_x, prev_y, event.x, event.y, fill='white', outline='', width=brush_size)
    else:
        canvas.create_line(prev_x, prev_y, event.x, event.y, fill=color, width=brush_size)
    prev_x, prev_y = event.x, event.y

def change_color(new_color):
    """Change the brush color."""
    global color
    color = new_color

def change_brush_size(new_size):
    """Change the brush size."""
    global brush_size
    brush_size = new_size

def change_brush_type(new_type):
    """Change the brush type, for example 'pencil', 'marker', or 'eraser'."""
    global brush_type
    brush_type = new_type

def show_eraser_popup():
    """Show a popup for choosing the eraser size."""
    popup = Toplevel(root)
    popup.title("Choose Eraser Size")

    # Create buttons for selecting the eraser size
    small_button = tk.Button(popup, text="Small", command=lambda: change_brush_size(2))
    medium_button = tk.Button(popup, text="Medium", command=lambda: change_brush_size(4))
    large_button = tk.Button(popup, text="Large", command=lambda: change_brush_size(8))

    small_button.pack(padx=10, pady=5)
    medium_button.pack(padx=10, pady=5)
    large_button.pack(padx=10, pady=5)

    popup.mainloop()

def start_drawing_interface():
    """Start the drawing interface after loading."""
    loading_label.pack_forget()
    color_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    brush_size_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    brush_type_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    canvas.pack()

# Create the main window/app
root = tk.Tk()
root.title('Microsoft Paint Remake')

# Create a canvas for drawing
canvas = tk.Canvas(root, width=600, height=400, bg='white')

# Loading label and show loading for 2 seconds
loading_label = tk.Label(root, text="Loading...", font=("Helvetica", 24))
loading_label.pack()
root.after(2000, start_drawing_interface)

# Frames for organizing the layout
color_frame = tk.Frame(root)
brush_size_frame = tk.Frame(root)
brush_type_frame = tk.Frame(root)

# Default settings
color = 'black'
brush_size = 4
brush_type = 'pencil'

# Color buttons
red_button = tk.Button(color_frame, text='Red', command=lambda: change_color('red'))
green_button = tk.Button(color_frame, text='Green', command=lambda: change_color('green'))
blue_button = tk.Button(color_frame, text='Blue', command=lambda: change_color('blue'))
yellow_button = tk.Button(color_frame, text='Yellow', command=lambda: change_color('yellow'))
black_button = tk.Button(color_frame, text='Black', command=lambda: change_color('gray1'))

# Brush size buttons
small_button = tk.Button(brush_size_frame, text='Small', command=lambda: change_brush_size(2))
medium_button = tk.Button(brush_size_frame, text='Medium', command=lambda: change_brush_size(4))
large_button = tk.Button(brush_size_frame, text='Large', command=lambda: change_brush_size(8))

# Brush type buttons
pencil_button = tk.Button(brush_type_frame, text='Pencil', command=lambda: change_brush_type('pencil'))
marker_button = tk.Button(brush_type_frame, text='Marker', command=lambda: change_brush_type('marker'))
highlighter_button = tk.Button(brush_type_frame, text='Highlighter', command=lambda: change_brush_type('highlighter'))
eraser_button = tk.Button(brush_type_frame, text='Eraser', command=show_eraser_popup)  # Modified to show popup

# Labels for buttons
color_label = tk.Label(color_frame, text='Color:')
brush_size_label = tk.Label(brush_size_frame, text='Brush Size:')
brush_type_label = tk.Label(brush_type_frame, text='Brush Type:')

# Layout and styling
color_label.pack(side=tk.LEFT, padx=5)
red_button.pack(side=tk.LEFT, padx=5)
green_button.pack(side=tk.LEFT, padx=5)
blue_button.pack(side=tk.LEFT, padx=5)
yellow_button.pack(side=tk.LEFT, padx=5)
black_button.pack(side=tk.LEFT, padx=5)

brush_size_label.pack(side=tk.LEFT, padx=5)
small_button.pack(side=tk.LEFT, padx=5)
medium_button.pack(side=tk.LEFT, padx=5)
large_button.pack(side=tk.LEFT, padx=5)

brush_type_label.pack(side=tk.LEFT, padx=5)
pencil_button.pack(side=tk.LEFT, padx=5)
marker_button.pack(side=tk.LEFT, padx=5)
highlighter_button.pack(side=tk.LEFT, padx=5)
eraser_button.pack(side=tk.LEFT, padx=5)

# Bind mouse events for drawing
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

# Start the Tkinter event loop
root.mainloop()
