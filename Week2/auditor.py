inventory = 0
failedEntry = 0
status = True

while status:
    stock = input("Please enter a stock quantity: ")

    if stock.isdigit():
        stock = int(stock)
        inventory += stock

    elif stock.startswith('-') and stock[1:].isdigit():
        failedEntry += 1
        print("Business rule: stock quantity cannot be negative.")

       
    else:
        failedEntry += 1
        print("Error: Please enter a valid integer.")




    
    

    
