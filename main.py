from tkinter import *


# calculates and sets label3's text = answer
def calculate():
    miles = int(user_entry.get())
    km_formatted = "{:.2f}".format(miles * 1.609)

    # formula: kilometers = miles × 1.609344
    label3.config(text=km_formatted)


# window
window = Tk()
window.config(width=500, height=200, padx=20, pady=20)
window.title("Miles to Kilometers Converter App")

# labels
label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text=f"is equal to ")
label2.grid(column=0, row=1)
label3 = Label(text=0)
label3.grid(column=1, row=1)
label4 = Label(text="Km")
label4.grid(column=2, row=1)

# entry
user_entry = Entry()
user_entry.grid(column=1, row=0)

# button
calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)

window.mainloop()