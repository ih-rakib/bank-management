"""
Manages bank account

"""

from multiprocessing.dummy import active_children


class Account : 
    accID = 1
    def __init__(self, name, age, nid_num, balance) -> None:
        self.name = name
        self.age = age
        self.nid_num = nid_num
        self.balance = balance

        # update account id
        self.account_id = Account.accID 
        Account.accID += 1

    def deposit(self, amount) :
        self.balance += amount 
    
    def withdraw(self, amount) : 
        self.balance -= amount

acc1 = Account('Rakib', 17, 1237, 500)
acc2 = Account('Akib', 24, 2345, 1000)

acc1.deposit(3000)
print(acc1.balance)
acc1.withdraw(700)
print(acc1.balance)
# print(acc1.account_id)
# print(acc2.account_id)