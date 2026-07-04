import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("350x300")
window.resizable(False, False)

tk.Label(window, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(window, text="Weight (kg)").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Height (m)").pack()
height_entry = tk.Entry(window)
height_entry.pack()

tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=15)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack()

window.mainloop()