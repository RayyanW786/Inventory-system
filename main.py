from utils import InventoryItem
from typing import Optional, Union
from operator import itemgetter


class MainProgram(object):
    def __init__(self):
        self.data = [["swords"], ["shields"], ["potions"]]
        self.menu()
        
    
    def menu(self):
        while True:
            try:
                user_input = input("\n____________________\n1. View Inventory\n2. View Category\n3. Add Category\n4. Add Item\n___________________\nEnter your choice 1-4: ")
                user_input = int(user_input)
                if user_input in [1, 2, 3, 4]:
                    self.main(user_input)
                else:
                    print("Please enter a valid option\nTo quit type quit, exit or stop!")
            except ValueError:
                if user_input.lower() in ["quit", "exit", "stop"]:
                    exit()
    
    def sorter(self, *, name: Optional[str] = None, attrname: Optional[str] = None) -> Union[bool, list]:
        if name != None:
            unsorted_lst = None
            for i in self.data:
                if i[0] == name:
                    unsorted_lst = i
                    break
            if unsorted_lst == None:
                return False
            
            unsorted_lst.remove(name)
            if unsorted_lst == []: return [name]

            if attrname == None:
                sorted_lst = sorted(unsorted_lst, key=lambda x: x.name)
                sorted_lst.insert(0, name)
            else:
                try:
                    sorted_lst = sorted(unsorted_lst, key=lambda x: getattr(x, attrname), reverse=True)
                except AttributeError:
                    return False
                sorted_lst.insert(0, name)
    
        else:
            sorted_lst = []
            for sub in self.data:
                name = sub[0]
                sub = sub[1:]
                if attrname == None:
                    inner = sorted(sub, key=lambda x: x.name)
                else:
                    try:
                        inner = sorted(sub, key=lambda x: getattr(x, attrname), reverse=True)
                    except AttributeError:
                        return False
                inner.insert(0, name)
                sorted_lst.append(inner)
            
        return sorted_lst
    
    def displayer(self, *, name: Optional[str] = None, attrname: Union[int, str] = None) -> None:
        data = self.sorter(name=name, attrname=attrname)
        if attrname == None:
            attrname = "name"
        if data == False:
            print(f"A error occurred, Please make sure all of your inputs are valid!")
            self.menu()
        else:
            if name != None:
                cat = data[0]
                print(f"Category: {cat}\nsorted by: {attrname}\n")
                data = data[1:]
                if data == []: print("No items in category\n\n")
                else:
                    for i in data:
                        print(f"Item Name: {i.name}\nQuantity Owned: {i.quantity}\nStats:\nAttack: {i.attack}\nDefence: {i.defence}\n\n")
            else:
                print(f"Full Inventory\nsorted by: {attrname}")
                for sub in data:
                    cat = sub[0]
                    print(f"Category: {cat}\n")
                    sub = sub[1:]
                    if sub == []: print("No items in Category\n\n")
                    else:    
                        for i in sub:
                           print(f"Item Name: {i.name}\nQuantity Owned: {i.quantity}\nStats:\nAttack: {i.attack}\nDefence: {i.defence}\n\n")
        self.menu()
    
    def add_category(self, category: str) -> None:
        if category in [item for sublist in sorted(self.data, key = itemgetter(0)) for item in sublist]:
            print("category already exists!")
        else:    
            self.data.append([category])
            print(f"Added Category: {category}")

    def add_item(self, category: str, item: InventoryItem) -> None:
        if category not in [item for sublist in sorted(self.data, key = itemgetter(0)) for item in sublist]:
            print("category does not exists!")
        else:
            index = None
            for sub in range(len(self.data)):
                if self.data[sub][0] == category:
                    index = sub

            if item.name in sorted(self.data[index][1:], key = lambda x: x.name):
                print(f"The item \"{item.name}\" already exists in this category")
            self.data[index].append(item)
            print(f"Added Item: {item.name}")

    def main(self, option):
        if option == 1:
            maybe_attr = input("Would you like to sort by a item attribute?\nType n if not, valid options are: attack, defence and quantity: ")
            valid_inputs = ["attack", "defence", "quantity"]
            if maybe_attr.lower() in valid_inputs:
                self.displayer(attrname = maybe_attr)
            self.displayer()
        elif option == 2:
            name = input("Enter the name of the Category: ")
            maybe_attr = input("Would you like to sort by a item attribute?\nType n if not, valid options are: attack, defence and quantity: ")
            valid_inputs = ["attack", "defence", "quantity"]
            if maybe_attr.lower() in valid_inputs:
                self.displayer(name = name, attrname = maybe_attr)
            else:
                self.displayer(name = name)
        elif option == 3:
            name = input("Enter the name of the Category: ")
            self.add_category(name)
        elif option == 4:
            category = input("Enter the name of the Category you wish to add said item into: ")
            name = input("Enter the name of the Item: ")
            attack = int(input("Enter the attack stats for said item: "))
            defence = int(input("Enter the defence stats for said item: "))
            quantity = int(input("Enter the quantity of the said item that you own: "))
            self.add_item(category, InventoryItem(name = name, attack = attack, defence = defence, quantity = quantity))
        self.menu()

if __name__ == "__main__":
    MainProgram()

        







        
