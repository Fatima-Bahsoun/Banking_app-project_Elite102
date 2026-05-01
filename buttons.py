# UI modul helper
#this is a function to be used in the banking app
import tkinter as tk
from main import create_accout, get_account, deposit, withdraw

def my_buttons(underTheWindow, go_withdraw, go_deposit, go_account, go_balance):
 #adding image to make the buttons look more modern; 
    rounded_img = tk.PhotoImage(file="round_button_image.png")
    underTheWindow.rounded_img = rounded_img
#the buttons are almost all the same; only the names and placements change.
    withdraw_button = tk.Button(underTheWindow, image=rounded_img, text="Withdraw", compound="center", font=("Times New Roman", 18), borderwidth=0, highlightthickness=0, command=go_withdraw)
    withdraw_button.place(x=20, y=90, width=160, height=60)
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    deposite_button = tk.Button(underTheWindow, image=rounded_img, text="Deposit", compound="center", font=("Times New Roman", 18), borderwidth=0, highlightthickness=0, command=go_deposit)
    deposite_button.place(x=200, y=90, width=160, height=60)
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    account_button = tk.Button(underTheWindow, image=rounded_img, text="Account", compound="center", font=("Times New Roman", 18), borderwidth=0, highlightthickness=0, command=go_account)
    account_button.place(x=20, y=170, width=160, height=60)
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    balance_button = tk.Button(underTheWindow, image=rounded_img, text="Balance", compound="center", font=("Times New Roman", 18), borderwidth=0, highlightthickness=0, command=go_balance)
    balance_button.place(x=200, y=170, width=160, height=60)

    return balance_button, account_button, deposite_button, withdraw_button

