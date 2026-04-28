#here_it is where I need to 
#button to withdraw
def my_buttons(underTheWindow):
    withdraw_button = tk.Button(underTheWindow, text="Withdraw", font=("Times New Roman", 18))#, width=259, height=96)#here: try the width to be 194
    #here: button not really correct sieze because its not by pixels
    withdraw_button.place(y=70 x=20)#coordinates place holder
#★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺★☺#
    deposite_button = tk.Button(underTheWindow, text="Deposite", font=("Times New Roman", 18))#, width=259, height=96)#here: try the width to be 194
    #here_it fix sieze
    deposite_button.place(y=120, padx=60)#here_it; this is a placehordder; Meaning testing is still needed
