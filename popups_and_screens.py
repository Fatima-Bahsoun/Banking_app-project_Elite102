#functions for the pop-up windows (withdraw, balance, and deposit)import tkinter as tk
import tkinter as tk
from tkinter import messagebox
from main import create_accout, get_account, deposit, withdraw

def withdraw_popup(root):
    popup = tk.Toplevel(root)
    popup.title("Withdraw")
    popup.geometry("400x300")
    popup.resizable(False, False)

    tk.Label(popup, text="Withdraw Money", font=("Times New Roman", 20)).pack(pady=10)

    tk.Label(popup, text="Account ID:").pack()
    id_entry = tk.Entry(popup)
    id_entry.pack(pady=5)

    tk.Label(popup, text="Amount:").pack()
    amount_entry = tk.Entry(popup)
    amount_entry.pack(pady=5)

    def confirm_withdraw():
        try:
            withdraw(id_entry.get(), float(amount_entry.get()))
            messagebox.showinfo("Success", "Withdrawal completed.")
            popup.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(popup, text="Confirm", command=confirm_withdraw).pack(pady=15)


def deposit_popup(root):
    popup = tk.Toplevel(root)
    popup.title("Deposit")
    popup.geometry("400x300")
    popup.resizable(False, False)

    tk.Label(popup, text="Deposit Money", font=("Times New Roman", 20)).pack(pady=10)

    tk.Label(popup, text="Account ID:").pack()
    id_entry = tk.Entry(popup)
    id_entry.pack(pady=5)

    tk.Label(popup, text="Amount:").pack()
    amount_entry = tk.Entry(popup)
    amount_entry.pack(pady=5)

    def confirm_deposit():
        try:
            deposit(id_entry.get(), float(amount_entry.get()))
            messagebox.showinfo("Success", "Deposit completed.")
            popup.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(popup, text="Confirm", command=confirm_deposit).pack(pady=15)


def balance_popup(root):
    popup = tk.Toplevel(root)
    popup.title("Balance")
    popup.geometry("400x250")
    popup.resizable(False, False)

    tk.Label(popup, text="Check Balance", font=("Times New Roman", 20)).pack(pady=10)

    tk.Label(popup, text="Account ID:").pack()
    id_entry = tk.Entry(popup)
    id_entry.pack(pady=5)

    def show_balance():
        try:
            acc = get_account(id_entry.get())
            messagebox.showinfo("Balance", f"Balance: ${acc[2]}")
            popup.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(popup, text="Check", command=show_balance).pack(pady=15)


def account_screen(root, main_menu):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Create Account", font=("Times New Roman", 26)).pack(pady=20)

    tk.Label(root, text="Name:").pack()
    name_entry = tk.Entry(root, font=("Times New Roman", 16))
    name_entry.pack(pady=5)

    tk.Label(root, text="Initial Deposit:").pack()
    deposit_entry = tk.Entry(root, font=("Times New Roman", 16))
    deposit_entry.pack(pady=5)

    def create_account_action():
        try:
            create_accout(name_entry.get(), float(deposit_entry.get()))
            messagebox.showinfo("Success", "Account created.")
            main_menu()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(root, text="Create", font=("Times New Roman", 18), command=create_account_action).pack(pady=20)
    tk.Button(root, text="Back", font=("Times New Roman", 16), command=main_menu).pack(pady=10)
