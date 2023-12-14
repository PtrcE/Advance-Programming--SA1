#Exersice 1

import tkinter as tk
from tkinter import font

def change_font_style():
    # Change the label's font style
    new_font = font.Font(framelabel, framewelcome.cget("font"))
    new_font.config(weight="bold", size=16)
    framewelcome.config(font=new_font)

# Create the main window
root = tk.Tk()
root.title("Welcome Window")

# Set the default window size
root.geometry("400x200")

# Disable resizing the window
root.resizable(False, False)

# Add background color to the window
root.configure(bg="#e6e6e6")

# Create a frame to hold the label
framelabel = tk.Frame(root, bg="#e6e6e6")
framelabel.pack(pady=20)

# Create a label to display the welcome message
framewelcome = tk.Label(framelabel, text="Welcome to the GUI Program!", font=("Arial", 12), bg="#e6e6e6")
framewelcome.pack()

# Create a button to change the font style
change_font_button = tk.Button(root, text="Change Font Style", command=change_font_style)
change_font_button.pack(pady=10)

# Start the main loop
root.mainloop()
