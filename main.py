"""
==================================================================
SMART RETAIL STORE MANAGEMENT SYSTEM
==================================================================
Final Project - BS Business Intelligence
Pure Python (no external libraries, no classes/OOP)

This program demonstrates the following mandatory concepts:
- Variables, Data Types, Input/Output, Strings
- Control Flow (if/elif/else, nested if), For Loop, While Loop
- Loop Control (break, continue)
- Functions & Function Arguments
- Lists, Positive/Negative Indexing, List Comprehension
- Built-in List Methods: append(), insert(), extend(), count(),
  index(), copy(), sort(), reverse()

Each concept is marked in comments with the tag [CONCEPT] so it can
be easily located and cited in the project report.
==================================================================
"""

# ------------------------------------------------------------------
# GLOBAL DATA STORAGE (LISTS)
# [CONCEPT] Variables & Lists -> All store data is kept in global
# lists. Because there is no OOP, these lists act as our "database".
# ------------------------------------------------------------------

# ---- Module 2: Product Management lists ----
# Sample data pre-populated so the system is demo-ready.
product_ids       = [101, 102, 103, 104, 105]
product_names     = ["Wireless Mouse", "Mechanical Keyboard", "USB-C Cable", "27-inch Monitor", "Laptop Stand"]
product_categories= ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"]
product_prices    = [1200.0, 4500.0, 350.0, 22000.0, 1800.0]      # [CONCEPT] Data Types -> float
product_quantities= [50, 30, 100, 15, 40]                         # [CONCEPT] Data Types -> int

# ---- Module 3: Customer Management lists ----
customer_names   = ["Ali Khan", "Sara Ahmed", "Bilal Hussain"]
customer_phones  = ["0300-1234567", "0312-7654321", "0333-9988776"]
customer_cities  = ["Lahore", "Karachi", "Islamabad"]

# ---- Module 7: Sales record list (used by Sales & Billing + BI Report) ----
# Each entry stored as a string-formatted record for simplicity (no OOP):
# "CustomerName|ProductName|Quantity|FinalBill"
sales_records = []

# Track login state globally
logged_in = False


# ==================================================================
# MODULE 1: USER LOGIN SYSTEM
# ==================================================================

def login():
    """
    Handles user authentication.
    [CONCEPT] While Loop -> restricts login attempts to a maximum of 3.
    [CONCEPT] If/Else -> validates credentials.
    [CONCEPT] Loop Control (break) -> exits loop immediately on success.
    """
    global logged_in

    correct_username = "admin"
    correct_password = "admin123"

    attempts = 0                     # [CONCEPT] Variable (int)
    max_attempts = 3

    while attempts < max_attempts:   # [CONCEPT] While Loop
        print("\n--- LOGIN ---")
        entered_username = input("Enter Username: ")   # [CONCEPT] Input
        entered_password = input("Enter Password: ")    # [CONCEPT] Input

        # [CONCEPT] If / Else (string comparison)
        if entered_username == correct_username and entered_password == correct_password:
            print("Login Successful! Welcome,", entered_username)
            logged_in = True
            break                      # [CONCEPT] Break -> stop loop, login achieved
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Invalid Username or Password. Attempts remaining: {remaining}")
            else:
                print("Invalid login. Maximum attempts reached. Access denied.")

    return logged_in


# ==================================================================
# MODULE 2: PRODUCT MANAGEMENT SYSTEM
# ==================================================================

def add_product(name, category, price, quantity):
    """
    Adds a new product to the product lists.
    [CONCEPT] Function Arguments -> name, category, price, quantity.
    [CONCEPT] append() -> adds new product ID/name/category/price/qty
    at the end of each respective list.
    """
    # Generate next product ID (simple increment logic using indexing)
    if len(product_ids) == 0:
        new_id = 101
    else:
        new_id = product_ids[-1] + 1     # [CONCEPT] Negative Indexing -> last element

    product_ids.append(new_id)           # [CONCEPT] append()
    product_names.append(name)           # [CONCEPT] append()
    product_categories.append(category)  # [CONCEPT] append()
    product_prices.append(price)         # [CONCEPT] append()
    product_quantities.append(quantity)  # [CONCEPT] append()

    print(f"\nProduct '{name}' added successfully with Product ID: {new_id}")


def insert_priority_product(name, category, price, quantity):
    """
    Inserts a product at the very beginning of the lists (position 0)
    to mark it as a 'priority/featured' product on shelf display.
    [CONCEPT] insert() -> demonstrates insertion at a specific index.
    """
    if len(product_ids) == 0:
        new_id = 101
    else:
        new_id = max(product_ids) + 1

    product_ids.insert(0, new_id)          # [CONCEPT] insert()
    product_names.insert(0, name)          # [CONCEPT] insert()
    product_categories.insert(0, category) # [CONCEPT] insert()
    product_prices.insert(0, price)        # [CONCEPT] insert()
    product_quantities.insert(0, quantity) # [CONCEPT] insert()

    print(f"\nPriority product '{name}' inserted at the top of the list (ID: {new_id}).")


def search_product(search_name):
    """
    Searches a product by name (case-insensitive).
    [CONCEPT] index() -> retrieves position of matching product.
    [CONCEPT] For Loop + Continue -> skips non-matching entries.
    """
    found = False
    for i in range(len(product_names)):       # [CONCEPT] For Loop
        if product_names[i].lower() != search_name.lower():
            continue                          # [CONCEPT] Continue -> skip non-matches
        found = True
        print("\n--- Product Found ---")
        print(f"Product ID   : {product_ids[i]}")
        print(f"Product Name : {product_names[i]}")
        print(f"Category     : {product_categories[i]}")
        print(f"Price        : {product_prices[i]}")
        print(f"Quantity     : {product_quantities[i]}")

    if not found:
        # Demonstrate index()/in usage as an alternative search confirmation
        print(f"\nNo product found with the name '{search_name}'.")


def display_products():
    """
    Displays all products in a formatted table.
    [CONCEPT] List Comprehension -> builds a list of formatted strings.
    [CONCEPT] Positive Indexing -> product_names[i], etc.
    """
    if len(product_ids) == 0:
        print("\nNo products available.")
        return

    print("\n" + "=" * 80)
    print(f"{'ID':<6}{'Name':<22}{'Category':<15}{'Price':<10}{'Qty':<6}")
    print("=" * 80)

    # [CONCEPT] List Comprehension -> create formatted row strings
    rows = [
        f"{product_ids[i]:<6}{product_names[i]:<22}{product_categories[i]:<15}{product_prices[i]:<10}{product_quantities[i]:<6}"
        for i in range(len(product_ids))
    ]

    for row in rows:        # [CONCEPT] For Loop
        print(row)
    print("=" * 80)


def update_product_quantity(product_name, change_amount, operation):
    """
    Updates stock quantity for a product using indexing.
    [CONCEPT] Function Arguments -> product_name, change_amount, operation.
    [CONCEPT] If-Else -> decide whether to add or subtract stock.
    [CONCEPT] List Indexing -> directly modify quantity at found index.
    """
    if product_name not in product_names:
        print(f"\nProduct '{product_name}' not found.")
        return

    idx = product_names.index(product_name)   # [CONCEPT] index()

    if operation == "add":
        product_quantities[idx] = product_quantities[idx] + change_amount
        print(f"\nStock increased. New quantity for '{product_name}': {product_quantities[idx]}")
    elif operation == "subtract":
        # Nested if -> ensure stock never goes negative
        if change_amount > product_quantities[idx]:        # [CONCEPT] Nested If
            print("\nError: Cannot reduce more than available stock.")
        else:
            product_quantities[idx] = product_quantities[idx] - change_amount
            print(f"\nStock reduced. New quantity for '{product_name}': {product_quantities[idx]}")
    else:
        print("\nInvalid operation. Use 'add' or 'subtract'.")


def product_management_menu():
    """Sub-menu for Module 2."""
    while True:                           # [CONCEPT] While Loop
        print("\n----- PRODUCT MANAGEMENT MENU -----")
        print("1. Add Product")
        print("2. Insert Priority Product")
        print("3. Search Product")
        print("4. Display All Products")
        print("5. Update Product Quantity")
        print("6. Back to Main Menu")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter Product Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))
            add_product(name, category, price, quantity)
        elif choice == "2":
            name = input("Enter Product Name: ")
            category = input("Enter Category: ")
            price = float(input("Enter Price: "))
            quantity = int(input("Enter Quantity: "))
            insert_priority_product(name, category, price, quantity)
        elif choice == "3":
            sname = input("Enter Product Name to search: ")
            search_product(sname)
        elif choice == "4":
            display_products()
        elif choice == "5":
            pname = input("Enter Product Name to update: ")
            op = input("Type 'add' or 'subtract': ").lower()
            amt = int(input("Enter quantity amount: "))
            update_product_quantity(pname, amt, op)
        elif choice == "6":
            print("Returning to Main Menu...")
            break                          # [CONCEPT] Break -> exit sub-menu loop
        else:
            print("Invalid choice. Please try again.")


# ==================================================================
# MODULE 3: CUSTOMER MANAGEMENT SYSTEM
# ==================================================================

def add_customer(name, phone, city):
    """
    Adds a new customer.
    [CONCEPT] append() -> adds customer details to respective lists.
    [CONCEPT] String Operations -> .strip(), .title() for clean formatting.
    """
    name = name.strip().title()     # [CONCEPT] Strings -> strip(), title()
    customer_names.append(name)
    customer_phones.append(phone.strip())
    customer_cities.append(city.strip().title())
    print(f"\nCustomer '{name}' added successfully.")


def search_customer(search_name):
    """
    Searches for a customer by name.
    [CONCEPT] For Loop -> iterate through customer list.
    [CONCEPT] String Methods -> .lower() for case-insensitive comparison.
    """
    found = False
    for i in range(len(customer_names)):     # [CONCEPT] For Loop
        if customer_names[i].lower() == search_name.lower():
            found = True
            print("\n--- Customer Found ---")
            print(f"Name  : {customer_names[i]}")
            print(f"Phone : {customer_phones[i]}")
            print(f"City  : {customer_cities[i]}")
            break                              # [CONCEPT] Break -> stop after first match
    if not found:
        print(f"\nNo customer found with the name '{search_name}'.")


def display_customers():
    """
    Displays all customers.
    [CONCEPT] extend() -> demonstrated by merging a temporary list of
    'VIP' tags into a display list (illustrative use of extend()).
    """
    if len(customer_names) == 0:
        print("\nNo customers available.")
        return

    # Demonstration of extend(): build a combined display list
    display_list = []                       # [CONCEPT] empty list creation
    temp_header = ["----- CUSTOMER LIST -----"]
    display_list.extend(temp_header)        # [CONCEPT] extend()

    for line in display_list:
        print(line)

    print(f"{'Name':<20}{'Phone':<18}{'City':<15}")
    print("-" * 53)
    for i in range(len(customer_names)):    # [CONCEPT] For Loop
        print(f"{customer_names[i]:<20}{customer_phones[i]:<18}{customer_cities[i]:<15}")


def customer_management_menu():
    """Sub-menu for Module 3."""
    while True:
        print("\n----- CUSTOMER MANAGEMENT MENU -----")
        print("1. Add Customer")
        print("2. Search Customer")
        print("3. Display All Customers")
        print("4. Back to Main Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter Customer Name: ")
            phone = input("Enter Phone Number: ")
            city = input("Enter City: ")
            add_customer(name, phone, city)
        elif choice == "2":
            sname = input("Enter Customer Name to search: ")
            search_customer(sname)
        elif choice == "3":
            display_customers()
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")


# ==================================================================
# MODULE 4: SALES & BILLING SYSTEM
# ==================================================================

def calculate_discount(bill_amount):
    """
    Calculates discount percentage based on bill amount.
    [CONCEPT] If-elif-else -> tiered discount logic.
    [CONCEPT] Function with single argument and return value.
    """
    if bill_amount >= 50000:
        return 20
    elif bill_amount >= 20000:
        return 10
    else:
        return 0


def process_sale():
    """
    Handles the full sales transaction workflow:
    select product -> enter quantity -> calculate bill -> apply discount
    -> reduce stock -> print receipt -> log sale record.
    [CONCEPT] Nested If -> stock availability check inside discount logic.
    [CONCEPT] List Indexing -> updating product_quantities directly.
    """
    customer_name = input("\nEnter Customer Name: ")
    product_name = input("Enter Product Name to purchase: ")

    if product_name not in product_names:
        print(f"\nProduct '{product_name}' not found in inventory.")
        return

    idx = product_names.index(product_name)   # [CONCEPT] index()

    quantity = int(input(f"Enter quantity (Available stock: {product_quantities[idx]}): "))

    # Nested if: first check product exists logically, then check stock
    if quantity <= 0:
        print("\nInvalid quantity entered.")
        return
    else:
        if quantity > product_quantities[idx]:     # [CONCEPT] Nested If
            print("\nError: Insufficient stock available for this purchase.")
            return
        else:
            unit_price = product_prices[idx]
            total_bill = unit_price * quantity

            discount_percent = calculate_discount(total_bill)
            discount_amount = total_bill * (discount_percent / 100)
            final_bill = total_bill - discount_amount

            # Reduce stock - [CONCEPT] List Indexing update
            product_quantities[idx] = product_quantities[idx] - quantity

            # Log the sale for BI Report (Module 7)
            sale_record = f"{customer_name}|{product_name}|{quantity}|{final_bill:.2f}"
            sales_records.append(sale_record)   # [CONCEPT] append()

            # Print Receipt
            print("\n" + "=" * 50)
            print("              SALES RECEIPT")
            print("=" * 50)
            print(f"Customer Name : {customer_name}")
            print(f"Product Name  : {product_name}")
            print(f"Quantity      : {quantity}")
            print(f"Unit Price    : {unit_price}")
            print(f"Total Bill    : {total_bill:.2f}")
            print(f"Discount      : {discount_percent}% (-{discount_amount:.2f})")
            print(f"Final Bill    : {final_bill:.2f}")
            print("=" * 50)
            print(f"Remaining stock for '{product_name}': {product_quantities[idx]}")


def sales_billing_menu():
    """Sub-menu for Module 4."""
    while True:
        print("\n----- SALES & BILLING MENU -----")
        print("1. New Sale")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            process_sale()
        elif choice == "2":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")


# ==================================================================
# MODULE 5: INVENTORY ANALYSIS SYSTEM
# ==================================================================

def generate_inventory_report():
    """
    Generates a full inventory analysis report.
    [CONCEPT] sort() -> sorts a copy of prices to find rankings.
    [CONCEPT] copy() -> ensures original product_prices list is untouched.
    [CONCEPT] reverse() -> reverses sorted list to show descending order.
    [CONCEPT] Built-in min()/max() used alongside list copy/sort strategy.
    """
    if len(product_ids) == 0:
        print("\nNo products available for analysis.")
        return

    total_products = len(product_ids)

    # Total stock using a simple for loop accumulator
    total_stock = 0
    for qty in product_quantities:       # [CONCEPT] For Loop
        total_stock += qty

    # [CONCEPT] copy() -> create a copy of prices so original list order is preserved
    prices_copy = product_prices.copy()

    # [CONCEPT] sort() -> sort the copied list in ascending order
    prices_copy.sort()

    cheapest_price = prices_copy[0]            # [CONCEPT] Positive Indexing
    most_expensive_price = prices_copy[-1]     # [CONCEPT] Negative Indexing

    # [CONCEPT] reverse() -> reverse the sorted list (descending order) for display
    prices_copy.reverse()

    cheapest_index = product_prices.index(cheapest_price)
    expensive_index = product_prices.index(most_expensive_price)

    print("\n" + "=" * 50)
    print("           INVENTORY ANALYSIS REPORT")
    print("=" * 50)
    print(f"Total Products        : {total_products}")
    print(f"Total Stock Available  : {total_stock}")
    print(f"Most Expensive Product : {product_names[expensive_index]} (Rs. {most_expensive_price})")
    print(f"Cheapest Product       : {product_names[cheapest_index]} (Rs. {cheapest_price})")
    print("=" * 50)
    print("Prices sorted descending (via sort() + reverse()):")
    print(prices_copy)


# ==================================================================
# MODULE 6: STRING ANALYSIS MODULE
# ==================================================================

def string_analysis():
    """
    Performs string analysis on a product name entered by the user.
    [CONCEPT] Strings -> len(), .upper(), .lower(), .count()
    """
    product_name = input("\nEnter a Product Name to analyze: ")

    length = len(product_name)                  # [CONCEPT] String length
    upper_version = product_name.upper()         # [CONCEPT] .upper()
    lower_version = product_name.lower()         # [CONCEPT] .lower()

    char_to_count = input("Enter a character to count in the name: ")
    char_count = product_name.count(char_to_count)   # [CONCEPT] .count()

    print("\n--- STRING ANALYSIS RESULT ---")
    print(f"Original Name      : {product_name}")
    print(f"Total Characters    : {length}")
    print(f"Uppercase Version   : {upper_version}")
    print(f"Lowercase Version   : {lower_version}")
    print(f"Occurrences of '{char_to_count}' : {char_count}")


# ==================================================================
# MODULE 7: BUSINESS INTELLIGENCE REPORT
# ==================================================================

def business_intelligence_report():
    """
    Generates a Business Intelligence summary from sales_records.
    [CONCEPT] List Comprehension -> extracts final bill amounts as floats.
    [CONCEPT] Built-in functions sum(), max(), min() over list comprehension result.
    """
    if len(sales_records) == 0:
        print("\nNo sales have been recorded yet. Please make a sale first.")
        return

    num_customers = len(customer_names)
    num_products = len(product_ids)

    # [CONCEPT] List Comprehension -> parse final bill (4th field) from each record
    sale_amounts = [float(record.split("|")[3]) for record in sales_records]

    total_sales = sum(sale_amounts)
    average_sale = total_sales / len(sale_amounts)
    highest_sale = max(sale_amounts)
    lowest_sale = min(sale_amounts)

    print("\n" + "=" * 50)
    print("        BUSINESS INTELLIGENCE REPORT")
    print("=" * 50)
    print(f"Number of Customers (registered) : {num_customers}")
    print(f"Number of Products (in catalog)   : {num_products}")
    print(f"Total Transactions Recorded       : {len(sales_records)}")
    print(f"Total Sales Revenue                : {total_sales:.2f}")
    print(f"Average Sale per Transaction       : {average_sale:.2f}")
    print(f"Highest Sale                       : {highest_sale:.2f}")
    print(f"Lowest Sale                        : {lowest_sale:.2f}")
    print("=" * 50)


# ==================================================================
# MODULE 8: MENU DRIVEN SYSTEM (MAIN PROGRAM)
# ==================================================================

def main():
    """
    Main driver function for the Smart Retail Store Management System.
    [CONCEPT] While Loop -> keeps menu running until user exits.
    [CONCEPT] If-elif-else -> routes user choice to correct module.
    """
    global logged_in

    print("Welcome to the Smart Retail Store Management System")

    while True:                      # [CONCEPT] While Loop (main menu loop)
        print("\n===== SMART RETAIL STORE MANAGEMENT SYSTEM =====")
        print("1. Login")
        print("2. Product Management")
        print("3. Customer Management")
        print("4. Sales & Billing")
        print("5. Inventory Report")
        print("6. String Analysis")
        print("7. Business Report")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            login()
        elif choice == "2":
            if not logged_in:
                print("\nAccess Denied. Please login first (Option 1).")
            else:
                product_management_menu()
        elif choice == "3":
            if not logged_in:
                print("\nAccess Denied. Please login first (Option 1).")
            else:
                customer_management_menu()
        elif choice == "4":
            if not logged_in:
                print("\nAccess Denied. Please login first (Option 1).")
            else:
                sales_billing_menu()
        elif choice == "5":
            if not logged_in:
                print("\nAccess Denied. Please login first (Option 1).")
            else:
                generate_inventory_report()
        elif choice == "6":
            string_analysis()   # Available without login (standalone utility)
        elif choice == "7":
            if not logged_in:
                print("\nAccess Denied. Please login first (Option 1).")
            else:
                business_intelligence_report()
        elif choice == "8":
            print("\nThank you for using the Smart Retail Store Management System.")
            print("Exiting program... Goodbye!")
            break               # [CONCEPT] Break -> exit main program loop
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")


# ------------------------------------------------------------------
# PROGRAM ENTRY POINT
# ------------------------------------------------------------------
if __name__ == "__main__":
    main()