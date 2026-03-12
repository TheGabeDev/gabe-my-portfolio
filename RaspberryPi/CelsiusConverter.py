#Write a GUI program to convert Farheint (F) to Celsius(C). Your program must include
#a label to display the converted result, an EntryBox for farheint (F), a "Convert" button
#and a "Quit" button.
#Farheint value will be entered in the entry box; the user then clicks on the "Convert"
#button to convert F to C.

import tkinter as tk

mainwindow = tk.Tk()

def convert():
    fahrenheit = entry_box.get()
    celsius = 5/9 * (float(fahrenheit)-32)

    label1.config(text=celsius)

def quit():
    mainwindow.destroy()

entry_box = tk.Entry()
convert_button = tk.Button(text='Convert', command= convert)
quit_button = tk.Button(text='Quit', command= quit)
label1 = tk.Label(text='RESULT')

entry_box.pack(padx=5, pady=5)
convert_button.pack(padx=5, pady=5)
quit_button.pack(padx=5, pady=5)
label1.pack(padx=5, pady=5)



mainwindow.mainloop()
