from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import pygame

darkGray = '#232324'
gray = '#303133'

#'1200x800' (lower res)
#'1800x1200'(high res)

def window():
    window = tk.Tk()
    window.title('Game Making Tool for Kids')
    window.geometry('1800x1200')
    window.configure(bg = darkGray)

    nb = ttk.Notebook(window)
    
    page1 = ttk.Frame(nb)
    
    page2 = ttk.Frame(nb)
    text = ScrolledText(page2)
    text.pack(expand=1, fill="both")
    
    codeText = tk.Text(window, width = 75, bg = gray, fg = 'white')
    
    codeText.pack(fill=tk.Y, expand = True)
        
    window.mainloop()

window()
