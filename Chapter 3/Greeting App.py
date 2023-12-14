import tkinter as tk

def update_greeting():
    user_name = entry_field.get()
    selected_color = color_variable.get()
    greeting = f"Hello, {user_name}! Nice to meet you!"
    greeting_label.config(text=greeting, fg=selected_color)

root = tk.Tk()
root.title("Personalized Greeting")

input_frame = tk.Frame(root, relief="solid", borderwidth=2, padx=10, pady=10, bg="skyblue")
input_frame.pack(side="top", fill="x", expand="YES")

display_frame = tk.Frame(root, relief="solid", borderwidth=2, padx=10, pady=10, bg="lightgray")
display_frame.pack(side="top", fill="x", expand="YES")

title_label = tk.Label(input_frame, text="Personalized Greeting", bg="skyblue", fg="darkblue")
title_label.pack(pady=2)

entry_field = tk.Entry(input_frame, width=30)
entry_field.pack(pady=2)

color_variable = tk.StringVar()
color_variable.set("green")

color_opts = {
    "Red": "red",
    "Green": "green",
    "Blue": "blue",
    "Black": "black",
    "White": "white"
}

color_menu = tk.OptionMenu(input_frame, color_variable, *color_options.keys())
color_menu.pack(pady=5)

update_bttn = tk.bttn(input_frame, text="Update Greeting", command=update_greeting)
update_bttn.pack(pady=5)

greeting_label = tk.Label(display_frame, text="", wraplength=300, bg="lightgray", fg="darkblue")
greeting_label.pack(pady=5)

root.mainloop()