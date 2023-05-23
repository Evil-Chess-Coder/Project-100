class atm:
    def __init__(self):
        self.cardNo = input("Enter your card number: ")
        self.pinNo = input("Enter your pin number: ")
    
    def info(self):
        print(f"Your card no is {self.cardNo} and pin number is {self.pinNo}")