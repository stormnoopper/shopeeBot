import pyautogui as pg
import time
from tkinter import *
import tkinter.font as font
import threading

# Run Code using Shift+Enter

# Bot Function
def StartBot():
    # Some of Item have to select product information
    # You can add code like ButButton
    # BuyButton
    pg.click(721, 522, 2)
    time.sleep(0.75)
    # ConfirmCartButton
    pg.click(856, 481, 3)
    time.sleep(0.75)
    # ConfirmPayment
    pg.scroll(-10000)
    time.sleep(0.75)
    pg.click(850, 415, 3)
    # After This have to vertify your payment
    botStatus.config(text="Bot Active Finish", fg="green")

# UI for bot
ui = Tk()
ui.geometry("200x100") # Set window size
ui.resizable(False, False) # Make window can't resize

# Make Window Center
screen_width = ui.winfo_screenwidth()
screen_height = ui.winfo_screenheight()
window_width = 200
window_height = 100
x = screen_width - window_width - 10
y = screen_height - window_height - 40
ui.geometry(f"{window_width}x{window_height}+{x}+{y}")

# App Text
mainTextFont = font.Font(family="Helvetica", size=20, weight="bold")
mainText = Label(ui, text='Shopee Bot', font=mainTextFont)
mainText.pack()

# Version Text
appVersionFont = font.Font(family="Helvetica", size=10, weight="bold")
appVersion = Label(ui, text='V 0.1.2', font=appVersionFont)
appVersion.pack()

# Bot button
startButton = Button(ui, text="Click Me", command=StartBot)
startButton.pack()

# Bot Status
botStatusFont = font.Font(family="Helvetica", size=18, weight="bold")
botStatus = Label(ui, text='Not Active', font=botStatusFont, fg="red")
botStatus.pack()

#Active UI
ui.mainloop()