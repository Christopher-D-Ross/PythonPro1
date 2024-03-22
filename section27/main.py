from tkinter import *

window = Tk()
window.title("Process finished with exit code 0")
window.minsize(width=600, height=300)
window.config(padx=100, pady=200)

# Label
# Creating A Label
label = Label(text="XP", font=("Courier", 26, "bold"))
# Using the pack() method to place a component into the screen.
label.config(text="^XP^")
# label.place(x=300, y=280)
label.grid(column=0, row=0)


def button_clicked():
    print("Slash")
    label.config(text="Resurrected")


# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)
# button.pack()
button_two = Button(text="DREAD BUTTON")
button_two.grid(column=3, row=0)

# Entry
# Entry Component - This will create an input box on the screen
insertion = Entry(width=10)
# Adding Placeholder text for the input
insertion.insert(0, "READY")
# The get() method for the Entry class will return the input in a string format.
insertion.get()
insertion.grid(column=4, row=3)


# insertion.pack()


def button_input():
    label.config(text=insertion.get())


button.config(command=button_input)

window.mainloop()
