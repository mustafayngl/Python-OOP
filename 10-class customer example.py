"""
class customer:
    def __init__(self,name,surname,citizenid,adress):
        self.name = name
        self.surname = surname
        self.citizenid = citizenid
        self.adress = adress
    
    def buy(self,product):
        return f"{self.name} bought {product.amount} {product.itemid}s"

class product:
    def __init__(self,itemid,itemprice,amount):
        self.itemid = itemid
        self.itemprice = itemprice
        self.amount = amount
        

    
john = customer("john","cena",432423,"grovest")
apple = product("apple",3,7)

print(john.buy(apple))
"""
"""
class customer:
    def __init__(self,ID,name,surname,adress):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.adress = adress
        
    def buy(self,quantity,product):
        total = quantity*product.price
        print(f"{self.name} {self.surname} bought {product.name}. Total pay is {total}")

class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

apple = product("Apple",15)
john = customer(1,"John","Cena","LA")
john.buy(5,apple)
"""
class customer:
    def __init__(self,ID,name,surname,adress,credit):
        self.name = name
        self.surname = surname
        self.ID = ID
        self.adress = adress
        self.credit = credit
        
    def buy(self,quantity,product):
        total = quantity*product.price
        if self.credit >= total:
            self.credit = self.credit - total
            print(f"{self.name} {self.surname} bought {product.name}. Total pay is {total}")
        else:
            print(f"{self.name} {self.surname} could not afford {product.name}. Total pay is above credit")
    
    def addcredit(self,amount):
        self.credit = self.credit +amount

class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

apple = product("Apple",15)
john = customer(1,"John","Cena","LA",10)
john.buy(5,apple)
john.addcredit(65)
john.buy(5,apple)

banana = product("Banana",2)
joe = customer(2,"Joe","Star","NYC",30)
joe.buy(7.5,banana)
joe.buy(7.5,banana)
joe.buy(7.5,banana)

