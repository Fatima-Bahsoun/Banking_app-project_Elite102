#here_it is where I need to 
#|||See this to all
#check all of the possitions 
#, width=259, height=96)#here: try the width to be 194 |||
#this is a function to be used in the banking app
import tkinter as tk
from main import create_accout, get_account, deposit, withdraw
def my_buttons(underTheWindow):
    #adding image to make the buttons look more modern
    rounded_img = tk.PhotoImage(file="round_button_image.png")
    underTheWindow.rounded_img = rounded_img
    
    withdraw_button = tk.Button(underTheWindow, image = rounded_img, text="Withdraw", compound="center", font=("Times New Roman", 18), borderwidth=0, highlightthickness=0)
    withdraw_button.place(x=20, y=70, width=160, height=60)#this size formate works better(it uses pixels)
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    deposite_button = tk.Button(underTheWindow, text="Deposite", font=("Times New Roman", 18))
    deposite_button.place(x=200, y=70, width=160, height=60)
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    account_button = tk.Button(underTheWindow, text="Account", font=("Times New Roman", 18))
    account_button.place(x=20, y=150, width=160, height=60)
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    balance_button = tk.Button(underTheWindow, text="Balance", font=("Times New Roman", 18))
    balance_button.place(x=200, y=150, width=160, height=60)
    return balance_button, account_button, deposite_button, withdraw_button