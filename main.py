from tkinter import *

# Create GUI window
window = Tk()
window.title("Miles to Kilometer")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)

# Static labels
miles_label = Label(text="Miles", font=("Arial", 20), width=8)
miles_label.grid(row=1, column=3)
km_label = Label(text="Km", font=("Arial", 20), width=8)
km_label.grid(row=2, column=3)
equals_label = Label(text="is equal to", font=("Arial", 20), width=10)
equals_label.grid(row=2, column=1)

# Dynamic labels
km_number_label = Label(text="0", font=("Arial", 20), width=10)
km_number_label.grid(row=2, column=2)
km_number_label.config(pady=20)

# User input: enter miles
userinput_miles = Entry(font=("Arial", 20), width=10)
userinput_miles.focus()
userinput_miles.grid(row=1, column=2)


# User input: calculate result
def calculate_button_click():
    miles = userinput_miles.get()
    # Change background to red if userinput is invalid
    if not miles.isnumeric():
        userinput_miles.config(bg="red")
    # Otherwise, restore background and calculate result
    else:
        userinput_miles.config(bg="white")


calculate_button = Button(font=("Arial", 20), text="Calculate", command=calculate_button_click)
calculate_button.grid(row=3, column=2)

# Keep GUI window open until program ends
window.mainloop()
