import tkinter as tk

window = tk.Tk()
window.title('Math')
window.minsize(width=400, height=400)

def math():
    import Calculator

def game():
    import Games

title_label = tk.Label(window, text='Math')
title_label.pack()

Buttom_input = tk.Button(window, text='Click', command=math)
Buttom_input.pack()

title_label2 = tk.Label(window, text='Game')
title_label2.pack()


Buttom2_input = tk.Button(window, text='Hi', command=game)
Buttom2_input.pack()

output_label = tk.Label(window)
output_label.pack()

window.mainloop()