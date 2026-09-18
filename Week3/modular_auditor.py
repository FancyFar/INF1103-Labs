total_Price = 0
failed_Entry = 0
deliveries_processed = 0
status = True

def get_valid_input():
    price = input("Please enter a price: ")

    if price == 'quit':
        return 'quit'

    elif price.isdigit():
        return int(price)

    elif price.startswith('-') and price[1:].isdigit():
        print("Business rule: price quantity cannot be negative.")
        return None
    else:
        print("Error: Please enter a valid integer.")
        return None

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total   
   

def calculate_tax(total_price):
    tax = total_price * 0.10
    return int(tax)

def generate_report(total_Price, failed_Entry):
    print("Total Deliveries Processed:", total_Price)
    print("Number of Failed/Rejected Entries:", failed_Entry)



while status:
    valid_input = get_valid_input()

    if valid_input == 'quit':
        generate_report(total_Price, failed_Entry)
        status = False

    elif isinstance(valid_input, int):
        total_Price = process_delivery(total_Price, valid_input)

        if total_Price > 500:
            print("Alert! Total price has exceeded 500 units!") 
            break

        tax = calculate_tax(valid_input)
        print("Tax for this delivery:", tax)

        deliveries_processed += 1

    else:
        failed_Entry += 1
    




     
