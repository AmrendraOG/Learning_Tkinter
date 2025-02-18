# This is a very basic implementation of a Temperature Converter
# Making this to learn GUI development using Python

import tkinter as tk

root = tk.Tk()

root.title("Celsius to Fahrenheit")
root.geometry("400x400")
root.configure(bg="black")

def convert_temp():
	temp = cel.get()
	fah = (float(temp) * 9/5) + 32
	result.config(text=f"{fah}F")

title = tk.Label(root, text="Temperature Converter", font=("Arial", 24), fg="white", bg="black")
title.pack(pady=10)
cel_title = tk.Label(root, text="Celsius:", font=("Arial", 16), fg="white", bg="black")
cel_title.pack(pady=20)
cel = tk.Entry(root)
cel.insert(0, "0.0")
cel.pack(pady=10)
convert = tk.Button(root, text="Convert", command=convert_temp)
convert.pack(pady=10)
result = tk.Label(root, text="Temperature in Fahrenheit", font=("Arial", 16), fg="white", bg="black")
result.pack(pady=10)
exit = tk.Button(root, text="Exit", command=lambda: root.destroy())
exit.pack(pady=10)

root.mainloop()
