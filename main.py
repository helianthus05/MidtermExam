import sys

file_name = "sales_log.txt"

def print_menu():
    print("========================================")
    print("       SALES RECORD MANAGEMENT SYSTEM   ")
    print("========================================")
    print("1. Add Sale Record")
    print("2. View All Records & Summary Statistics")
    print("3. Clear All Sales Data")
    print("4. Exit System")
    print("========================================")

def add_sale_record():
    print("\n--- ADD SALE RECORD ---")
    item_name = input("Enter Item Name: ").strip()

    while not item_name:
        print("Error: Item name cannot be empty.")
        item_name = input("Enter Item Name: ").strip()

    while True:
        try:
            quantity = int(input("Enter Quantity Sold: "))
            if quantity <= 0:
                print("Error: Quantity must be greater than zero.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer for quantity.")

    while True:
        try:
            price_per_unit = float(input("Enter Price Per Unit: "))
            if price_per_unit <= 0:
                print("Error: Price must be greater than zero.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number for price.")

    total_amount = quantity * price_per_unit

    try:
        with open(file_name, "a") as file:
            record = f"{item_name},{quantity},{price_per_unit:.2f},{total_amount:.2f}\n"
            file.write(record)
        print("Sale record saved successfully.")
    except IOError as e:
        print(f"File Error: Unable to save record. ({e})")

def view_records_and_summary():
    print("\n--- SALES RECORDS & SUMMARY STATISTICS ---")

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No records found.\n")
            return

        total_units_sold = 0
        grand_total_revenue = 0.0

        print(f"{'Item Name'} | {'Quantity'} | {'Unit Price'} | {'Total Amount'}")
        print("-" * 50)

        for line in lines:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",")
            item_name = parts[0]
            quantity = int(parts[1])
            price_per_unit = float(parts[2])
            total_amount = float(parts[3])

            total_units_sold += quantity
            grand_total_revenue += total_amount

            print(f"{item_name} | {quantity} | ${price_per_unit:.2f} | ${total_amount:<.2f}")

        print("-" * 50)
        print(f"Total Units Sold:    {total_units_sold}")
        print(f"Grand Total Revenue: ${grand_total_revenue:.2f}\n")

    except FileNotFoundError:
        print("No records found.")
    except ValueError:
        print("Error: The sales file contains corrupted or improperly formatted data.")
    except IOError as error:
        print(f"File Error: Unable to read file. ({error})")

def clear_all_sales_data():
    print("\n--- CLEAR ALL SALES DATA ---")
    try:
        with open(file_name, "w") as file:
            pass
        print("All records cleared. No records remaining.")
    except IOError as error:
        print(f"File Error: Unable to clear records. ({error})")

def main():
    while True:
        print_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            add_sale_record()
        elif choice == '2':
            view_records_and_summary()
        elif choice == '3':
            clear_all_sales_data()
        elif choice == '4':
            print("Thank you for using the Sales Record Management System! Goodbye!")
            sys.exit(0)
        else:
            print("Invalid selection. Please choose an option from 1 to 4.")


if __name__ == "__main__":
    main()
