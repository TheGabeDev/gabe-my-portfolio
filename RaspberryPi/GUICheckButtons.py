# Joe’s Automotive performs the following routine maintenance services:
# • Oil change—$35.00
# • Inspection—$50.00
# • Muffler replacement—$100.00
# • Tire rotation—$20.00

#Write a GUI program with check buttons that allow the user to select any or all of these
#services. When the user clicks "Apply Services" button the total charges should be displayed.
#MAKE USE OF GRID GEOMETRY MANAGER TO CONTROL THE LAYOUT OF OUR APPLICATION

import tkinter as tk
import tkinter.messagebox as m

mainwindow = tk.Tk()

def quit1():
    mainwindow.destroy()

def applyServices():
    total = 0
    
    if checkOil.get() != 0:
        total += checkOil.get()

    if checkInspe.get() != 0:
        total += checkInspe.get()

    if checkMuffler.get() != 0:
        total += checkMuffler.get()

    if checkTire.get() != 0:
        total += checkTire.get()

    label.config(text=f'Total cost: ${total:.2f}')

    

checkOil = tk.IntVar()
checkInspe = tk.IntVar()
checkMuffler = tk.IntVar()
checkTire = tk.IntVar()

oil_change = tk.Checkbutton(text='Oil change', onvalue=35, offvalue=0, variable=checkOil)
inspection = tk.Checkbutton(text='Inspection', onvalue=50, offvalue=0, variable=checkInspe)
muffler_replacement = tk.Checkbutton(text='Muffler replacement', onvalue=100, offvalue=0, variable=checkMuffler)
tire_rotation = tk.Checkbutton(text='Tire rotation', onvalue=20, offvalue=0, variable= checkTire)

exit_button = tk.Button(text='Exit', command= quit1)
apply_button = tk.Button(text='Apply Services', command= applyServices)

label = tk.Label(text='Total cost:')

oil_change.grid(row=0, column= 0, padx=5, pady=5)
inspection.grid(row=1, column= 0, padx=5, pady=5)
muffler_replacement.grid(row=2, column=0, padx=5, pady=5)
tire_rotation.grid(row=3, column=0, padx=5, pady=5)
exit_button.grid(row=0, column=1, padx=5, pady=5)
apply_button.grid(row=2, column= 1, padx=5, pady=5)
label.grid(row=4, column=0, padx=5, pady=5, columnspan=2)


