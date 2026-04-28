#here is where work in to be continued
import tkinter as tk
from tkinter import messagebox
from main import create_accout, get_account, deposit, withdraw
#this is the main window
root = tk.Tk()
root.title("That's My Money")
root.geometry("714x942")
#items inside the main window
def main_menu():
    #clear window; used in order to be able to switch screen.
    for widget in root.winfo_children():
        widget.destroy()
    #display text on the main screen
    text_display = tk.Label(root, text="Welcome. This is YOUR money.", font=("Times New Roman", 22))# here: find a way to display at the bottom
    text_display.pack()
#declearing & calling the buttons from the 



    
#calling the main menu
main_menu()
#this is what runs the main window
root.mainloop()#this is what starts the window