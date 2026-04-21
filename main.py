#here is where work in to be continued
import mysql.connector


db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="ALGAWTHadrekna@1",
    database="testdb")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    balance DOUBLE
)
""")
db.commit()
#%s is a placeholder, from the parameters; 
#replacing %s with {id_} (for example) there are higher risks; 
#someone could view other's info using certain commands like 
# 1 or 1=1 making all the querys would show;
def create_accout(name, inti_depo):
    cursor = db.cursor()
    #adds a new row with name and starting balance
    sql = "INSERT INTO accounts (name, balance) VALUES (%s,%s)" 
    values = (name, inti_depo)
    cursor.execute(sql, values)
    #above is the same as: 
    #cursor.execute("INSERT INTO accounts (name, balance) VALUES (%s,%s)",(name, inti_depo))
    db.commit()
    print("Account created.\nSUCCEEDED")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def get_account(id_):
    cursor = db.cursor()
    sql = "SELECT id, name, balance FROM accounts WHERE id = %s"
    values = (id_,)
    cursor.execute(sql, values)
    #above is the same as: 
    #cursor.execute("SELECT id, name, balance FROM accounts WHERE id = %s",(id_,))
    return cursor.fetchone()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def deposit(id_, amount):
    cursor = db.cursor()
    sql = "UPDATE accounts SET balance = balance + %s WHERE id = %s"
    values= (amount, id_)
    cursor.execute(sql,values)
    #above is the same as: 
    #cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s",(amount, id_))
    db.commit()
    print("Deposit completed.\nSUCCEEDED")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def withdraw(id_, amount):
    cursor = db.cursor()
    sql = "UPDATE accounts SET balance = balance - %s WHERE id = %s"
    values= (amount, id_)
    cursor.execute(sql,values)
    #above is the same as: 
    #cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s",(amount, id_))
    db.commit()
    print("Withdrew your money...\nHave some fun, you deserve it!")

#db.close()
create_accout("Jacob", 100)
print(get_account(1))
deposit(1, 50)
print(get_account(1))
withdraw(1, 20)
print(get_account(1))
