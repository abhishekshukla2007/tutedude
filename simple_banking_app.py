# Welcome to simple banking application app

# start of functions to execute Show balance/ withdrawl/ deposit amount
balance = 0.0
def show_bal():
    print(f"Showing balance {balance}")
    
def withdrawl(amt):
    global balance
    
    if amt <= 0:
         print("Not sufficient balance to withdraw")
    elif amt > balance:
        print("Insufficient balance")
    else:
        balance -= amt

def deposit_amt(amt):
    global balance
    if amt > 0:
         balance += amt
    else:
         print("Invlid amount to deposit")
    
              
    
if __name__ == "__main__":
        
        while True:
                    print("-----------Welcome to ABC bank-----------")
                    print("=====================")
                    print("1. Show Balance")
                    print("=====================")
                    print("2. Amount Withdrawl")
                    print("=====================")
                    print("3. Deposit Amount")
                    print("=====================")
                    print("4. Quit")
                    choice = int(input("Hello Banking User. Please enter your choice ! (1-4)"))
                    
                    if choice == 1:
                        show_bal()
                    elif choice == 2:
                        amt = float(input("Enter the Amount to withdraw: "))
                        withdrawl(amt)
                    elif choice == 3:
                        amt = float(input("Enter the Amount to deposit: "))
                        deposit_amt(amt)
                    elif choice == 4:
                        break
                    else:
                        print("Invalid choice, try again !! ")

print("Thank you for banking with us")