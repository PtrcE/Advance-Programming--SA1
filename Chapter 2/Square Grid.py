#Exercise 2B

import tkinter as tk

window = tk.Tk()
window.title("Managing Layout - Square Grid")

left_frame = tk.Frame(window, relief="solid", highlightthickness=0, padx=5, pady=5)
left_frame.pack(side="left", fill="both", expand="TRUE")
right_frame = tk.Frame(window, borderwidth=5, relief="solid", highlightthickness=0, padx=5, pady=5)
right_frame.pack(side="right", fill="both", expand="TRUE")

a_button = tk.Label(left_frame, text="A", bg="#242B40", fg="white", padx=10, pady=10)
a_button.pack(side="top", fill="both", expand="YES")
b_button = tk.Label(left_frame, text="B", bg="white", fg="black", padx=10, pady=10)
b_button.pack(side="bottom", fill="both", expand="YES")
c_button = tk.Label(right_frame, text="C", bg="white",fg="black", padx=10, pady=10)
c_button.pack(side="top", fill="both", expand="YES")
d_button = tk.Label(right_frame, text="D", bg="#242B40", fg="white", padx=10, pady=10)
d_button.pack(side="bottom", fill="both", expand="YES")

window.mainloop()

