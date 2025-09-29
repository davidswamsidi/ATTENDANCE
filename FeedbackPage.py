import tkinter as tk
from tkinter import ttk, messagebox

# --- Configuration and Setup ---

# Function to handle the submit action
def submit_feedback():
    """
    1. Retrieves the text from all fields.
    2. Prints the collected data to the console.
    3. Clears the input fields.
    """
    # 1. Retrieve data from the input fields
    name = name_entry.get()
    email = email_entry.get()
    
    # Text widgets use different indexing: "1.0" is line 1, character 0
    # "end-1c" means end of text minus the final newline character
    feedback = feedback_text.get("1.0", "end-1c") 
    
    # Check if the main feedback field is empty (ignoring potential whitespace)
    if not feedback.strip():
        messagebox.showerror("Error", "Please enter your feedback before submitting.")
        return

    # 2. Print the collected data to the console
    print("-" * 30)
    print("--- NEW FEEDBACK SUBMISSION ---")
    print(f"Name: {name if name.strip() else '[Not Provided]'}")
    print(f"Email: {email if email.strip() else '[Not Provided]'}")
    print(f"Feedback:")
    print(feedback)
    print("-" * 30)

    # 3. Clear the input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)
    
    # Show a confirmation to the user
    messagebox.showinfo("Success", "Thank you! Your feedback has been submitted (and printed to the console).")


# --- Main Application Window Setup ---
app = tk.Tk()
app.title("Customer Feedback Form")
app.geometry("500x450")
app.resizable(False, False)

# Configure style for better appearance (optional but recommended)
style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TLabel', background='#f0f0f0', font=('Inter', 10))
style.configure('TButton', font=('Inter', 10, 'bold'))

# Create a main frame to hold all widgets and center them
main_frame = ttk.Frame(app, padding="20 20 20 20")
main_frame.pack(fill='both', expand=True)

# Configure grid columns to allow centering
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=3)


# --- 1. Name Field ---
name_label = ttk.Label(main_frame, text="Your Name:")
name_label.grid(row=0, column=0, sticky='w', pady=5, padx=10)

name_entry = ttk.Entry(main_frame, width=40)
name_entry.grid(row=0, column=1, sticky='ew', pady=5, padx=10)


# --- 2. Email Field ---
email_label = ttk.Label(main_frame, text="Your Email:")
email_label.grid(row=1, column=0, sticky='w', pady=5, padx=10)

email_entry = ttk.Entry(main_frame, width=40)
email_entry.grid(row=1, column=1, sticky='ew', pady=5, padx=10)


# --- 3. Feedback Area ---
feedback_label = ttk.Label(main_frame, text="Feedback:")
# Span the label across both columns for better layout above the Text widget
feedback_label.grid(row=2, column=0, columnspan=2, sticky='w', pady=(15, 5), padx=10)

# Create a scrollbar for the Text widget
feedback_scrollbar = ttk.Scrollbar(main_frame)
feedback_scrollbar.grid(row=3, column=2, sticky='ns', padx=(0, 10), pady=10)

# Create the Text widget for multi-line input
feedback_text = tk.Text(main_frame, wrap='word', height=10, width=40, 
                        yscrollcommand=feedback_scrollbar.set, 
                        font=('Inter', 10), relief=tk.FLAT, bd=2, bg='white')
feedback_text.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=10, pady=5)

# Link the scrollbar to the Text widget
feedback_scrollbar.config(command=feedback_text.yview)

# Configure the row where the text widget is located to expand vertically
main_frame.rowconfigure(3, weight=1)


# --- 4. Submit Button ---
submit_button = ttk.Button(main_frame, text="Submit Feedback", command=submit_feedback)
# Center the button under the form by spanning both columns
submit_button.grid(row=4, column=0, columnspan=2, pady=20)


# Start the Tkinter event loop
if __name__ == "__main__":
    app.mainloop()
