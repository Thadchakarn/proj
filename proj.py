class Item:  #create item class to add any item in vending machine
    def __init__(self, name, cost, id):
        self.name = name
        self.cost = cost
        self.id = id        #easier to use id for picking any item
    def printItem(self):
        print("id :", str(self.id), str(self.name), "cost", str(self.cost))

class VendingMachine:
    def __init__(self, money):
        self.money = money
        self.item = []      #create item list
        self.item.append(Item("NatWater", 10, 0))
        self.item.append(Item("Cok", 15, 1))
        self.item.append(Item("psi", 15, 2))
        self.item.append(Item("ichita", 20, 3))
        self.item.append(Item("Ley", 20, 4))
        self.item.append(Item("Oishid", 25, 5))
        self.item.append(Item("Pringle", 50, 6))

    def addMoney(self, m):
        #to add amount of money to vending machine
        self.money += int(m)

    def choose(self, id):
        #pick item by using id to point out
        if (self.calculate(self.item[id].cost)):
            print("Have", str(self.money), "change")
            print("Thank you!!\n")
            self.setMoney(0)
            return True
        return False

    def calculate(self, cost):
        #calculate total money that spend and check the amount money in vending machine enough to pay
        if (self.money - cost < 0):
            print("Invalid")
            print("Please top up money first")
            return False
        self.setMoney(self.money - cost)
        print("Your money are charged by", str(cost), "baht")
        return True

    def getMoney(self):
        return self.money

    def setMoney(self, money):
        self.money = money

    def show(self):     # to show how many item you can buy at your money
        print("You can buy")
        for i in self.item:
            if int(i.cost) > self.getMoney():
                break
            i.printItem()
    def showAll(self):
        # show all item in vending machine
        print("We have")
        for i in self.item:
            i.printItem()

def main():
    VM = VendingMachine(0)  # create with 0 baht
    state = 0
    # use state to check the situation 0 is idle, 1 is to choose, 2 is to top up and -1 is the finish situation
    while(True):
        print("Welcome!!")
        VM.showAll()
        money = int(input("Enter your money: ").strip())
        if (money < 0):
            print("Invalid\n")
            continue
        elif (money < 10):
            print("Need to top up money first")
            state = 2
        VM.addMoney(money)
        while(True):
            if (state == -1):
                state = 0
                break
            elif(state == 0):
                state = int(input(("Pick item enter 1, top up money enter 2: ")).strip())
            elif (state == 1):
                if (VM.getMoney() < 10):
                    print("Need to top up money")
                    state = 2
                    continue
                else:
                    VM.show()
                    pick = int(input(("Enter id or top up money enter -1: ")).strip())
                    if (pick == -1):
                        state = 2
                        continue
                    if (VM.choose(pick)):
                        state = -1
            elif(state == 2):
                exit = input("Enter 1 if you want to exit if not enter any: ").strip()
                if (exit == "1"):
                    print("Have", VM.money, "change")
                    print("Thank you!!\n")
                    VM.setMoney(0)
                    break
                amount = int(input("Enter your top up money: ").strip())
                if (amount < 0):
                    print("Invalid\n")
                    print("Have", VM.money, "change")
                    print("Thank you!!\n")
                    VM.setMoney(0)
                    break
                VM.addMoney(amount)
                state = 0

main()

