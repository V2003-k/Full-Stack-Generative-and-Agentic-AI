def chai_custormer():
    print("Welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_custormer()
next(stall) # start the generator

stall.send("Masala Chai")
stall.send("Lemon Chai")