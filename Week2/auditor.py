inventory = 0
failedEntry = 0
status = True

while status:
    stock = input("Please enter a stock quantity: ")

    if stock.isdigit():
        stock = int(stock)
        inventory += stock

       
    else:
        failedEntry += 1
        print("Error: Please enter a valid integer.")




    
    

    
