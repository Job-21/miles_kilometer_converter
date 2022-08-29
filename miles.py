import tkinter

window = tkinter.Tk()
window.title("CONVERT MILES TO KILOMETER")
window.iconbitmap("icons8_calculator.ico")
window.geometry("600x200")
window.config(bg="#123456")


def converter():
    if entry_field.get() == "" or entry_field.get() == " ":
        pass
    else:
        if " " in entry_field.get():
            label_info.grid(column=0, row=3)
        else:
            miles = float(entry_field.get())
            km = miles * 1.609
            km_label1.config(text=f"{km} km")


miles_label = tkinter.Label(text="Enter Miles ", bg="black", fg="white", font=("Arial", 16, "bold"))
miles_label.grid(column=0, row=0, pady=10, padx=50)

entry_field = tkinter.Entry(width=30, border=2, font=("Arial", 13, "bold"))
entry_field.grid(column=1, row=0, padx=10, pady=10)

km_label = tkinter.Label(text="Kilometer results : ", bg="black", fg="white", font=("Arial", 16, "bold"))
km_label.grid(column=0, row=1, pady=10, padx=50)

km_label1 = tkinter.Label(text="0", bg="black", fg="white", font=("Arial", 16, "bold"), width=10)
km_label1.grid(column=1, row=1, pady=10, padx=50)

calculate_button = tkinter.Button(text="CALCULATE", font=("Arial", 15, "bold"), command=converter)
calculate_button.grid(column=0, row=2, padx=40, pady=10)

label_info = tkinter.Label(text="No spaces allowed in numbers.", font=("Arial", 12, "bold"))



window.mainloop()