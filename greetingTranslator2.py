import tkinter as tk
from tkinter import ttk

class HelloTranslatorApp:
    """
    A simple Tkinter application that allows the user to select a language 
    from a dropdown to see the translation of "Hello," demonstrating the 
    use of class structure and the Combobox widget.
    """
    def __init__(self, master):
        # 1. Initialize the main window (master)
        self.master = master
        master.title("The 'Hello' Translator")
        master.geometry("400x200") # Made the window slightly taller for the dropdown

        # Configure grid for better centering
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # Internal state for translations: Dictionary mapping Language Name to Translation
        self.translations = {
            "English": "Hello",
            "Spanish": "Hola",
            "French": "Bonjour",
            "German": "Guten Tag",
            "Italian": "Ciao",
            "Arabic": "مرحبا (Marhaba)",
            "Japanese": "Kon'nichiwa",
            "Korean": "안녕하세요 (Annyeonghaseyo)"
        }
        
        # Get the list of language names for the dropdown
        self.language_names = list(self.translations.keys())

        # 2. Setup the main frame for centering widgets
        main_frame = ttk.Frame(master, padding="10 10 10 10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=1)

        # 3. Create Widgets

        # Label for instructions
        instruction_label = ttk.Label(main_frame, text="Select a language:")
        instruction_label.grid(row=0, column=0, pady=(5, 0), padx=20, sticky='w')
        
        # The Dropdown (Combobox)
        self.language_selector = ttk.Combobox(
            main_frame,
            values=self.language_names,
            state="readonly" # Prevent users from typing arbitrary values
        )
        self.language_selector.grid(row=1, column=0, pady=(0, 15), padx=20, sticky='ew')
        
        # Set initial selection to the first language
        self.language_selector.set(self.language_names[0])
        
        # Bind the selection event to the method that updates the label
        # The <<ComboboxSelected>> event fires whenever the user chooses an option.
        self.language_selector.bind("<<ComboboxSelected>>", self.language_selected)


        # The Output Label
        initial_language = self.language_selector.get()
        initial_translation = self.translations[initial_language]
        
        self.output_label = ttk.Label(
            main_frame,
            text=initial_translation, # Initial text based on the default selection
            font=('Arial', 14, 'bold'),
            foreground='#005792'
        )
        self.output_label.grid(row=2, column=0, pady=10, padx=20)

    def language_selected(self, event):
        """
        Callback method fired when a new language is selected from the combobox.
        'event' argument is required by Tkinter binding mechanism, but not used here.
        """
        # 1. Get the currently selected language name
        selected_language = self.language_selector.get()
        
        # 2. Look up the translation in the dictionary
        new_text = self.translations.get(selected_language, "Translation not found.")
        
        # 3. Update the label's text
        self.output_label.config(text=new_text)

# 4. Main execution block
if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()
    
    # Create an instance of our application class, passing the root window as the master
    app = HelloTranslatorApp(root)
    
    # Start the Tkinter event loop
    root.mainloop()
