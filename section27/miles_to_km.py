from tkinter import *

window = Tk()
window.wm_minsize(300, 150)
window.title("Miles To Kilometers Converter")
window.config(padx=50, pady=50)

miles = Entry(width=10)
miles.grid(row=1, column=2)


def convert_miles_to_km():
    output_label.config(text=str(round(int(miles.get()) * 1.60934, 2)))


calc_button = Button(text="Calculate", command=convert_miles_to_km)
calc_button.grid(row=3, column=2)

miles_label = Label(text="Miles")
miles_label.grid(row=1, column=3)

equal_label = Label(text="Is Equal To")
equal_label.grid(row=2, column=1)

output_label = Label(text="0")
output_label.grid(row=2, column=2)

km_label = Label(text="Km")
km_label.grid(row=2, column=3)

window.mainloop()
