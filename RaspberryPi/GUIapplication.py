#Write a GUI program with two groups of radio buttons that allow the user to select one
#of three hot beverages (tea, coffee, or chocolate) and one of three pastries (croissant,
#muffin, donut). Use an "Ok" button to display the combo message as a pop-up window.

import tkinter as tk
import tkinter.messagebox

mainwindow = tk.Tk()

def make_order():
    typeBeverage = "None"
    typePastries = "None"

    if beverages.get() == 1:
        typeBeverage = 'tea'
    elif beverages.get() == 2:
        typeBeverage = 'coffee'
    else:
        typeBeverage = 'hot chocolate'

    if pastries.get() == 4:
        typePastries = 'croissant'
    elif pastries.get() == 5:
        typePastries = 'muffin'
    else:
        typePastries = 'donut'
    tkinter.messagebox.showinfo(title='Order Info', message=('You ordered: ' + typeBeverage + ' and ' + typePastries))
    
    

orderButton = tk.Button(text='order', command=make_order)

beverages = tk.IntVar(value=1)
pastries = tk.IntVar(value=4)

teaButton = tk.Radiobutton(text='tea', variable=beverages, value=1)
coffeeButton = tk.Radiobutton(text='coffee', variable=beverages, value=2)
hotChocolateButton = tk.Radiobutton(text='hot chocolate', variable=beverages, value=3)

croissantButton = tk.Radiobutton(text='croissant', variable=pastries, value=4)
muffinButton = tk.Radiobutton(text='muffin', variable=pastries, value=5)
donutButton = tk.Radiobutton(text='donut', variable=pastries, value=6)

teaButton.pack()
coffeeButton.pack()
hotChocolateButton.pack()
croissantButton.pack()
muffinButton.pack()
donutButton.pack()
orderButton.pack()

mainwindow.mainloop()
