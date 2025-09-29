import tkinter as tk
from tkinter import ttk  # Import themed widgets for a slightly better look

def button_click():
    """
    Function to be called when the button is pressed.
    It gets the text from the input box and updates the output label.
    """
    user_input = input_box.get()  # Get the text from the Entry widget
    
    if user_input:
        # Update the text of the output_label
        output_label.config(text=f"Hello, {user_input}! Thanks for clicking.")
        # Clear the input box after reading
        input_box.delete(0, tk.END) 
    else:
        output_label.config(text="Please enter your name first!")


# 1. Setup the main window (the root object)
root = tk.Tk()
root.title("Tkinter Basic App") # Set the title of the window
root.geometry("400x200")       # Set the initial size of the window (Width x Height)

# 2. Create the GUI Widgets

# A label for instructions
instruction_label = ttk.Label(root, text="Enter your name below:")
instruction_label.pack(pady=5) # pack() is a basic layout manager that places the widget

# The Text Box (Entry widget) for user input
input_box = ttk.Entry(root, width=40)
input_box.pack(pady=5, padx=20) # padx/pady adds some padding around the widget

# The Button that calls the function when clicked
action_button = ttk.Button(root, text="Greet Me!", command=button_click)
action_button.pack(pady=10)

# The Output Display (Label widget)
# This label will start with some default text and be updated by the button_click function.
output_label = ttk.Label(root, text="Waiting for input...")
output_label.pack(pady=5)


# 3. Start the Tkinter event loop
# This line is essential! It keeps the window open and responsive to user actions.
root.mainloop()