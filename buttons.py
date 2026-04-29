#here_it is where I need to 
#|||See this to all
#check all of the possitions 
#, width=259, height=96)#here: try the width to be 194 |||
#this is a function to be used in the banking app
def my_buttons(underTheWindow):
    withdraw_button = tk.Button(underTheWindow, text="Withdraw", font=("Times New Roman", 18))
    #here: button not really correct sieze because its not by pixels
    withdraw_button.place(y=70 x=20)#coordinates place holder
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    deposite_button = tk.Button(underTheWindow, text="Deposite", font=("Times New Roman", 18))
    #here_it fix sieze
    deposite_button.place(y=70, padx=60)#here_it; this is a placehordder; Meaning testing is still needed
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    account_button = tk.Button(underTheWindow, text="Account", font=("Times New Roman", 18))
    account_button.place(y=120, padx=20)#here_it; still needs checking
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    balance_button = tk.Button(underTheWindow, text="Balance", font=("Times New Roman", 18))
    balance_button.place(y=120, padx=60)