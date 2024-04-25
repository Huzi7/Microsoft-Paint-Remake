import tkinter as tk

def start_draw(event):
    """Start drawing when the left mouse button is pressed."""
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def draw(event):
    """Draw lines when the mouse is moved with the left button held down."""
    global prev_x, prev_y
    if brush_type == 'highlighter':
        # Draw semi-transparent rectangles to simulate highlighter effect
        canvas.create_rectangle(prev_x, prev_y, event.x, event.y, fill=color, outline='', width=0, stipple='gray50')
    else:
        canvas.create_line(prev_x, prev_y, event.x, event.y, fill=color, width=brush_size)
    prev_x, prev_y = event.x, event.y

# Function to change the brush color
def change_color(new_color):
    global color
    color = new_color

# Function to change the brush size
def change_brush_size(new_size):
    global brush_size
    brush_size = new_size

# Function to change the brush type
def change_brush_type(new_type):
    global brush_type
    brush_type = new_type

# Function to start the drawing interface
def start_drawing_interface():
    loading_label.pack_forget()
    color_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    brush_size_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    brush_type_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    canvas.pack()
    # Bind mouse events to canvas
    canvas.bind("<Button-1>", start_draw)
    canvas.bind("<B1-Motion>", draw)

# Create the main window
root = tk.Tk()
root.title('Enhanced Drawing App')

# Create a canvas for the loading animation
canvas = tk.Canvas(root, width=600, height=400, bg='white')

# Display a loading label
loading_label = tk.Label(root, text="Loading...", font=("Helvetica", 24))
loading_label.pack()

# Simulate loading time (2 seconds)
root.after(2000, start_drawing_interface)

# Create frames for organizing the layout
color_frame = tk.Frame(root)
brush_size_frame = tk.Frame(root)
brush_type_frame = tk.Frame(root)

# Set default brush color to black
color = 'black'

# Set default brush size to medium
brush_size = 4

# Set default brush type to pencil
brush_type = 'pencil'

# Create color buttons
red_button = tk.Button(color_frame, text='Red', command=lambda: change_color('red'))
green_button = tk.Button(color_frame, text='Green', command=lambda: change_color('green'))
blue_button = tk.Button(color_frame, text='Blue', command=lambda: change_color('blue'))

# Create brush size buttons
small_button = tk.Button(brush_size_frame, text='Small', command=lambda: change_brush_size(2))
medium_button = tk.Button(brush_size_frame, text='Medium', command=lambda: change_brush_size(4))
large_button = tk.Button(brush_size_frame, text='Large', command=lambda: change_brush_size(8))

# Create brush type buttons
pencil_button = tk.Button(brush_type_frame, text='Pencil', command=lambda: change_brush_type('pencil'))
marker_button = tk.Button(brush_type_frame, text='Marker', command=lambda: change_brush_type('marker'))
highlighter_button = tk.Button(brush_type_frame, text='Highlighter', command=lambda: change_brush_type('highlighter'))

# Create labels for buttons
color_label = tk.Label(color_frame, text='Color:')
brush_size_label = tk.Label(brush_size_frame, text='Brush Size:')
brush_type_label = tk.Label(brush_type_frame, text='Brush Type:')

# Pack buttons and labels
color_label.pack(side=tk.LEFT, padx=5)
red_button.pack(side=tk.LEFT, padx=5)
green_button.pack(side=tk.LEFT, padx=5)
blue_button.pack(side=tk.LEFT, padx=5)

brush_size_label.pack(side=tk.LEFT, padx=5)
small_button.pack(side=tk.LEFT, padx=5)
medium_button.pack(side=tk.LEFT, padx=5)
large_button.pack(side=tk.LEFT, padx=5)

brush_type_label.pack(side=tk.LEFT, padx=5)
pencil_button.pack(side=tk.LEFT, padx=5)
marker_button.pack(side=tk.LEFT, padx=5)
highlighter_button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
root.mainloop()
