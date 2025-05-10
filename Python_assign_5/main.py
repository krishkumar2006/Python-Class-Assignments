#Automatic teller machine made by krish
class Atm:
    def __init__(self, Balance = 5000 , pin = 1234):
        self.Balance = Balance
        self.pin = pin

#Check pin
    def check_pin(self , Input_pin):
        return Input_pin == self.pin
  #Current Balance  
    def Current_balace(self):
        return self.Balance
# deposit
    def deposit(self , amount):
        self.Balance += amount
        return self.Balance
         
#withdrawal
    def withdraw(self , amount):
         if amount > self.Balance:
             print("insufficient balance")
             exit()
         else:    
             self.Balance -= amount
             return self.Balance   



    

#making instance of Class Atm    
bank = Atm()
user_input = int(input("Enter your pin: "))

# if pin is correct then this will run 
if bank.check_pin(user_input):
    print("Authentication Successful" )
    print(f"your current balance is  {bank.Current_balace()}")

#user selection 
    action = input("what would you like to do(deposit / withdraw)")

# if user select deposit then this will run
    if action == "deposit":
      user_deposit = int(input("Enter your amount: "))    

      bank.deposit(user_deposit)
      print(f"your account is credited by {user_deposit}") 
      print("Current account " ,bank.Current_balace())

# if user select withdrawal then this will run
    elif  action == "withdraw":
      user_withdrawal = int(input("Enter your amount: "))

      bank.withdraw(user_withdrawal)
      print(f"your account is debited by {user_withdrawal}") 
      print("Current balance " , bank.Current_balace())

    else:
        print("invalid selection")

#exit method if pin in is not valid
else:
    print("Invalid pin") 
    exit()



        

    