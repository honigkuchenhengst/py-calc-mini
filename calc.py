import tkinter as tk
FONT_SIZE1 = 28
FONT = ('Arial', FONT_SIZE1)

window = tk.Tk()
window.title("Mini Calculator")
window.geometry("500x600")

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)  # Lösche den aktuellen Text im Entry
    entry.insert(tk.END, current_text + str(value))  # Füge den neuen Text hinzu

def do_math():
    current_text = entry.get()
    result= eval(current_text)
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

entry = tk.Entry(font = FONT)
entry.grid(row=0, column=0, columnspan= 4, sticky="nsew")

button1 = tk.Button(text="1", font=FONT, command=lambda: button_click(1))
button1.grid(row=3, column= 0, sticky="nsew")
button2 = tk.Button(text="2", font=FONT, command=lambda: button_click(2))
button2.grid(row=3, column= 1, sticky="nsew")
button3 = tk.Button(text="3", font=FONT, command=lambda: button_click(3))
button3.grid(row=3, column= 2, sticky="nsew")
button4 = tk.Button(text="4", font=FONT, command=lambda: button_click(4))
button4.grid(row=2, column= 0, sticky="nsew")
button5 = tk.Button(text="5", font=FONT, command=lambda: button_click(5))
button5.grid(row=2, column= 1, sticky="nsew")
button6 = tk.Button(text="6", font=FONT, command=lambda: button_click(6))
button6.grid(row=2, column= 2, sticky="nsew")
button7 = tk.Button(text="7", font=FONT, command=lambda: button_click(7))
button7.grid(row=1, column= 0, sticky="nsew")
button8 = tk.Button(text="8", font=FONT, command=lambda: button_click(8))
button8.grid(row=1, column= 1, sticky="nsew")
button9 = tk.Button(text="9", font=FONT, command=lambda: button_click(9))
button9.grid(row=1, column= 2, sticky="nsew")
button0 = tk.Button(text="0", font=FONT, command=lambda : button_click(0))
button0.grid(row=4, column= 0, sticky="nsew")

buttonPlus = tk.Button(text="+", font=FONT, command=lambda: button_click("+"))
buttonPlus.grid(row=4, column= 2, sticky="nsew")
buttonMinus = tk.Button(text="-", font=FONT, command=lambda: button_click("-"))
buttonMinus.grid(row=3, column= 3, sticky="nsew")
buttonMal = tk.Button(text="*", font=FONT, command=lambda: button_click("*"))
buttonMal.grid(row=2, column= 3, sticky="nsew")
buttonDurch = tk.Button(text="/", font=FONT, command=lambda: button_click("/"))
buttonDurch.grid(row=1, column= 3, sticky="nsew")
buttonGleich = tk.Button(text="=", font=FONT, command=lambda: do_math())
buttonGleich.grid(row=4, column= 3, sticky="nsew")
buttonKomma = tk.Button(text=".", font=FONT, command=lambda value="." : button_click(value))
buttonKomma.grid(row=4, column= 1, sticky="nsew")

buttonClear = tk.Button(text="C L E A R", font=('Arial', 18), command=lambda: entry.delete(0, tk.END))
buttonClear.grid(row=5, column= 0, columnspan=4, sticky="nsew")

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

window.mainloop()