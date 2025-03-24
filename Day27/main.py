import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

input1 = tkinter.Entry(width=10)
input1.grid(column=3, row=2)

window.mainloop()
