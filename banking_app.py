#UI; front end
import tkinter as tk
from buttons import my_buttons as mb
from tkinter import messagebox
from main import create_accout, get_account, deposit, withdraw
from popups_and_screens import withdraw_popup, deposit_popup, balance_popup, account_screen
#this is the main window
root = tk.Tk()
root.title("That's My Money")
root.geometry("394x700")#16:9 ration
#items inside the main window
def main_menu():
    #clear window; used in order to be able to switch screen.
    for widget in root.winfo_children():
        widget.destroy()
    bg_img = tk.PhotoImage(file="bg.png")
    root.bg_img = bg_img 
    bg_label = tk.Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #display text on the main screen--Title
    text_display = tk.Label(root, text="Welcome.\nThis is your safe money place.", font=("Times New Roman", 22), fg= "white", bg="#cfb5cb")
    text_display.pack(pady=20)
    #declearing & calling the buttons from the buttons file
    mb( root, go_withdraw=lambda: withdraw_popup(root), go_deposit=lambda: deposit_popup(root), go_account=lambda: account_screen(root, main_menu), go_balance=lambda: balance_popup(root)
    )
#calling the main menu
main_menu()
#this is what runs the main window
root.mainloop()#this is what starts the window