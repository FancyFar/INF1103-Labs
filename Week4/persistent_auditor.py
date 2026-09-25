total_Price = 0
failed_Entry = 0
deliveries_processed = 0
status = True

def get_valid_input():
    user_product = input('\n'+ "Enter Product Name: ")

    if user_product.lower() == 'quit':
        return ['quit']
    else:
        user_quantity = input("Enter Quantity: ")

        if user_quantity.isdigit():
            return([user_product, user_quantity])

        elif user_quantity.startswith('-') and user_quantity[1:].isdigit():
            print("Business rule: price quantity cannot be negative.")
            return None
        else:
            print("Error: Please enter a valid integer.")
        return None

# def process_delivery(current_total, new_value):
#     new_total = current_total + new_value
#     return new_total   
   

# def calculate_tax(total_price):
#     tax = total_price * 0.10
#     return int(tax)

def load_inventory():
    try:
        print("Current Orders:" + '\n')
        with open("orders.txt", "r") as file:
            data = file.readlines()

            for item in data:
                print(item.strip())

    except FileNotFoundError:
        print("File not found")



def save_inventory(product_name, product_quantity):
    try: 
        with open("orders.txt", "r") as file:
            lines = file.readlines()
            if len(lines) > 0:
                last_line = lines[-1].strip()
                product_code = int(last_line.split(",")[0]) + 1

            else:
                product_code = 1001

    except FileNotFoundError:
        product_code = 1001

    try:
        with open("orders.txt", "a") as file:
            entry = f'{product_code}, {product_name}, {product_quantity}' + '\n'
            file.write(entry)

            print('\n' + "New Order Added:")
            print(entry)
            print("Order successfully saved to orders.txt")
    except:
        print("Order failed to save to order.txt")



def generate_report(total_Price, failed_Entry):
    print("Total Deliveries Processed:", total_Price)
    print("Number of Failed/Rejected Entries:", failed_Entry)


load_inventory()
while status:

    valid_input = get_valid_input() #get product name and quantity


    if valid_input[0] == 'quit':
        # generate_report(total_Price, failed_Entry)
        status = False

    # elif isinstance(user_input[1], int):
    #     total_Price = process_delivery(total_Price, user_input[1])

    #     if total_Price > 500:
    #         print("Alert! Total price has exceeded 500 !") 
    #         break

    #     tax = calculate_tax(user_input[1])
    #     print("Tax for this delivery:", tax)

    elif valid_input[1]:
        save_inventory(valid_input[0], valid_input[1])

        deliveries_processed += 1

    else:
        failed_Entry += 1
        




     
