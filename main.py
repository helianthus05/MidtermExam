filename = "sales_log.txt"

while True:
    print("========================================")
    print("     SALES RECORD MANAGEMENT SYSTEM     ")
    print("========================================")
    print("1. Add Sale Record")
    print("2. View All Records & Summary Statistics")
    print("3. Clear All Sales Data")
    print("4. Exit System")
    print("========================================")

    option = 0

    try:
        option = input("Select an option (1-4): ")
        option = int(option)
        if 5 > option > 0:
            break
        else:
            continue
    except ValueError:
        print(f'\n"{option}" is not a value option. Please try again.\n')
        continue

total_amount = 0
quantity_sold = 0
price_per_unit = 0

if option == 1:
    while True:
        print("\n1. Add Sale Record")
        item_name = input("Enter name: ")
        quantity_sold = input("Enter quantity sold (integer): ")
        price_per_unit = input("Enter Price Per Unit (float): ")
        try:
            quantity_sold = int(quantity_sold)
            price_per_unit = float(price_per_unit)
            break
        except ValueError:
            print("\nInvalid input. Please try again.\n")
            continue

    total_amount = quantity_sold * price_per_unit

    quantity_sold = str(quantity_sold)
    price_per_unit = str(price_per_unit)
    total_amount = str(total_amount)

    new_record = f"{item_name}, {quantity_sold}, {price_per_unit}, {total_amount}"

    try:
        with open(filename, "a") as f:
            f.write("\n")
            f.write(new_record)
            print("Sale record saved successfully.")
    except FileNotFoundError:
        print("Error: File does not exist.")

if option == 2:
    print("\n2. View All Records & Summary Statistics")
    try:
        with open(filename, "r") as f:
            for line in f:
                records = line.split(",")
                print(f"Item Name: {records[0]} ")

    except FileNotFoundError:
        print("Sale record saved successfully")