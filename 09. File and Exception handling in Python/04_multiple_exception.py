def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        if type(quantity) != 'int':
            raise TypeError("Quantity must be in number")
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError as te:
        print(te)

process_order("ginger", 2)
process_order("masala", "two")