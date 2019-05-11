class Account():
    msge = 'Welcome To Axis Bank'
    def __init__(self):
        print("Bank Accout details")
        
    def bal_dep(self,name,bal_cr,city):
        self.name = name
        self.name = bal_cr
        self.name = city
        #print("Here is the account information with deposit amount")
        print("Holder name is:",name)
        print("City:",city)
        print(bal_cr,"Amount will be deposited in your account.")
        
    def bal_wd(self,name,bal_db=4000):
        self.name = bal_db
        self.name = name
        #print("Here is the account information with debited amount")
        print("Holder name is",name)
        print("Debited amount of",name,"is",bal_db)

    def ava_bal(self,av_bl):
        self.name = av_bl
    

if __name__ == '__main__':
    obj = Account()
    print(obj.msge)
    obj.bal_dep("Aakash",4000,'Pune')
    obj.bal_dep("Parag", 3000,'Pune')
    obj.bal_dep("Chetan",2500,'Mumbai')
    obj.bal_dep("Sujit",2000,'Banglore')
    obj.bal_wd("Aakash",2000)
    obj.bal_wd("Parag",2000)
    obj.bal_wd("Chetan",1000)
    obj.bal_wd("Sujit",1000)

