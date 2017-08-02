import pytz
import datetime

class Account(object):
    """ Simple Account Class with Balance """

    #Declare below statement a staticmethod
    @staticmethod
    def _currentTime():
        utcTime = datetime.datetime.utcnow()
        return pytz.utc.localize(utcTime)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transActionList = [(Account._currentTime(), self.balance)]
        print("Account created for {}".format(self.name))


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.showBalance()
            self.transActionList.append((Account._currentTime(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.showBalance()
            self.transActionList.append((Account._currentTime(), amount*-1))

    def showBalance(self):
        print("Balance is {}".format(self.balance))

    def showTransactions(self):
        initialBalance = True
        for date, amount in self.transActionList: #Python unpacks the tuple allowing you to assign variables to each value
            if initialBalance:
                print("{:6} Opened Balance was opened on {} (local time was {})".format(amount, date, date.astimezone()))
                initialBalance = False
            else: 
                if amount > 0:
                    transType = "Deposited"
                else:
                    transType = "Withdrawn"
                    amount *= -1
                print("{:6} {} on {} (local time was {})".format(amount, transType, date, date.astimezone()))
    
if __name__ == '__main__': #Check if current is main if so run code below
    ron = Account("Ron", 2000)
    ron.showBalance()
    ron.deposit(1000)
    ron.withdraw(500)
    ron.showTransactions()


