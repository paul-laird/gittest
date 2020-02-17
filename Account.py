
# coding: utf-8

# In[2]:

#Create a Bank Account class

#define functions deposit, withdraw, transfer, checkBalance

#Create some bank accounts and test your methods

#Try to prevent illegal actions on the accounts

#github.com/sadfjkhsdafk/sadkygsfdak
print("Real version")


# In[3]:

#Update: The below is unfinished, and ignore pin-related stuff

#Also: Modify this to create a Wallet class 
#which can handle multiple simultaneous balances
#in different currencies or securities


# In[4]:

import random
import hashlib
class BankAccount:
    Accounts={}
    def __init__ (self, name,pin):
        self.__name=name
        self.__balance=0
        m = hashlib.sha256()
        m.update(pin.encode())
        self.__pin=m.digest()
        self.__accNo=random.randint(10000000,99999999)
        while self.__accNo in BankAccount.Accounts:
            self.__accNo=random.randint(10000000,99999999)
        BankAccount.Accounts[self.__accNo]=self
    def getDetails(self):
        return {'name':self.__name}
    def transfer(self,amt,dest):
        if self.withdraw(amt):
            dest.deposit(amt)
            return True
        else:
            return False
    def withdraw(self,amt,pin):
        m = hashlib.sha256()
        m.update(pin.encode())
        if m.digest()!=self.__pin:
            raise ValueError('Wrong PIN')
        if amt>self.__balance:
            return False
        else:
            self.__balance-=amt
            return True
    def deposit(self,amt):
        self.__balance+=amt


# In[5]:

a=BankAccount('Paul','1sdfhnjdgj,ketdyshjsrfx234')
a.deposit(100)
try:
    a.withdraw(50,'1233')
except ValueError as v:
    print (v)
    print (a._BankAccount__pin)


# In[6]:

BankAccount.Accounts.keys()
for k,v in BankAccount.Accounts.items():
    print(' %i: %s : %i'%(k,v.getDetails(), v._BankAccount__balance))


# In[7]:

BankAccount.Accounts[11566923].transfer(-1000,BankAccount.Accounts[47553964])


# In[ ]:




# In[8]:

menu=input('''What operation would you like to perform:
Deposit, Withdraw, Transfer, Check Balance''')
if menu=='Transfer':
    src=int(input('Enter your account number: '))
    dst=int(input('Enter the recipient\'s account number: '))
    amt=int(input('Enter the amount: '))
    if src in BankAccount.Accounts and dst in BankAccount.Accounts:
        BankAccount.Accounts[src].transfer(amt,BankAccount.Accounts[dst])
    else:
        print('Error!')


# In[ ]:




# In[9]:

flag=True
while flag:
    flag=False
    name=input('Whose account shall we create? ')
    try:
        BankAccount(name)
    except ValueError:
        print ('Name Taken, please try again!')
        flag=True
    


# In[10]:

BankAccount.Accounts.keys()


# In[12]:

BankAccount.Accounts[82846061].getDetails()


# In[ ]:



