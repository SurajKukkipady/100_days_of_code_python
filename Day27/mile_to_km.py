import tkinter

window = tkinter.Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

label = tkinter.Label(text="is equal to")
label.grid(column=0, row=1)

label2 = tkinter.Label(text="Miles")
label2.grid(column=2, row=0)

label3 = tkinter.Label(text="Km")
label3.grid(column=2, row=1)


def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.60934)
    label4.config(text=km)


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

label4 = tkinter.Label(text="0")
label4.grid(column=1, row=1)

window.mainloop()
