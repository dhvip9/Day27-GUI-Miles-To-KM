import tkinter


def mile_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609, 2)
    km_result["text"] = km


frame = tkinter.Tk()
frame.title("MILE to KM Converter")
frame.config(padx=20, pady=20)

# label
is_equal_to_label = tkinter.Label(text="is Equal to", font=("Arial", 18))
is_equal_to_label.grid(column=0, row=3)
is_equal_to_label.config(padx=5)

mile_label = tkinter.Label(text="MILE", font=("Arial", 15))
mile_label.grid(column=2, row=2)
mile_label.config(padx=10, pady=10)

km_label = tkinter.Label(text="KM", font=("Arial", 15))
km_label.grid(column=2, row=3)

km_result = tkinter.Label(text="0", font=("Arial", 24))
km_result.grid(column=1, row=3)


# buttons
button_1 = tkinter.Button(text="Click", command=mile_to_km)
button_1.grid(column=1, row=4)


# Entry
mile_input = tkinter.Entry(width=10)
mile_input.grid(column=1, row=2)


frame.mainloop()
