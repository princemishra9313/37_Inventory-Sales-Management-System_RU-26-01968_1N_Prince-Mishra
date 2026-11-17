
import pandas as pd
import os


# Create CSV files if they do not exist
def create_files():
    if not os.path.exists("inventory.csv"):
        data = pd.DataFrame(columns=["ID", "Name", "Stock", "Price"])
        data.to_csv("inventory.csv", index=False)

    if not os.path.exists("sales.csv"):
        data = pd.DataFrame(columns=["ID", "Quantity", "Amount"])
        data.to_csv("sales.csv", index=False)


# Load data from CSV files
def load_data():
    inventory = pd.read_csv("inventory.csv")
    sales = pd.read_csv("sales.csv")

    return inventory, sales


# Add a new item
def add_item(inventory):
    name = input("Enter item name: ").strip()

    if name == "":
        print("Item name cannot be empty.")
        return inventory

    try:
        stock = int(input("Enter stock: "))
        price = float(input("Enter price: "))

        if stock < 0 or price < 0:
            print("Stock and price cannot be negative.")
            return inventory

    except ValueError:
        print("Please enter valid numbers.")
        return inventory

    # Generate next item ID
    number = 101

    for item_id in inventory["ID"]:
        old_number = int(item_id[1:])

        if old_number >= number:
            number = old_number + 1

    item_id = "I" + str(number)

    new_item = {
        "ID": item_id,
        "Name": name,
        "Stock": stock,
        "Price": price
    }

    inventory.loc[len(inventory)] = new_item
    inventory.to_csv("inventory.csv", index=False)

    print("Item added.")
    print("ID:", item_id, "|", name, "| Stock:", stock, "| Price:", price)

    return inventory


# Sell an item
def sell_item(inventory, sales):
    item_id = input("Enter item ID: ").strip().upper()

    if item_id not in inventory["ID"].values:
        print("Item ID", item_id, "not found.")
        return inventory, sales

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return inventory, sales

    except ValueError:
        print("Please enter a valid quantity.")
        return inventory, sales

    # Find the item
    index = inventory.index[inventory["ID"] == item_id][0]

    available_stock = int(inventory.loc[index, "Stock"])
    price = float(inventory.loc[index, "Price"])
    name = inventory.loc[index, "Name"]

    # Check available stock
    if quantity > available_stock:
        print("Not enough stock. Available:", available_stock)
        return inventory, sales

    amount = quantity * price

    # Reduce stock
    inventory.loc[index, "Stock"] = available_stock - quantity

    # Save sale record
    new_sale = {
        "ID": item_id,
        "Quantity": quantity,
        "Amount": amount
    }

    sales.loc[len(sales)] = new_sale

    inventory.to_csv("inventory.csv", index=False)
    sales.to_csv("sales.csv", index=False)

    print("Sale recorded:", name, "x", quantity, "=", amount)
    print("Stock left:", available_stock - quantity)

    if available_stock - quantity == 0:
        print("Item is now out of stock.")

    return inventory, sales


# Update an item
def update_item(inventory):
    item_id = input("Enter item ID: ").strip().upper()

    if item_id not in inventory["ID"].values:
        print("Item ID", item_id, "not found.")
        return inventory

    index = inventory.index[inventory["ID"] == item_id][0]

    print("Leave a field blank to keep its old value.")

    new_name = input("Enter new name: ").strip()
    new_stock = input("Enter new stock: ").strip()
    new_price = input("Enter new price: ").strip()

    if new_name != "":
        inventory.loc[index, "Name"] = new_name

    try:
        if new_stock != "":
            stock = int(new_stock)

            if stock < 0:
                print("Stock cannot be negative.")
                return inventory

            inventory.loc[index, "Stock"] = stock

        if new_price != "":
            price = float(new_price)

            if price < 0:
                print("Price cannot be negative.")
                return inventory

            inventory.loc[index, "Price"] = price

    except ValueError:
        print("Please enter valid numbers.")
        return inventory

    inventory.to_csv("inventory.csv", index=False)

    print("Item updated.")

    return inventory


# Delete an item
def delete_item(inventory):
    item_id = input("Enter item ID: ").strip().upper()

    if item_id not in inventory["ID"].values:
        print("Item ID", item_id, "not found.")
        return inventory

    inventory = inventory[inventory["ID"] != item_id]

    inventory.to_csv("inventory.csv", index=False)

    print("Item", item_id, "deleted.")

    return inventory


# Display sales report
def sales_report(inventory, sales):
    if sales.empty:
        print("No sales recorded yet.")
        return

    # Group sales by item ID
    report = sales.groupby("ID").agg({
        "Quantity": "sum",
        "Amount": "sum"
    }).reset_index()

    # Add item names to the report
    report = pd.merge(report, inventory[["ID", "Name"]], on="ID", how="left")

    report["Name"] = report["Name"].fillna(report["ID"])

    total_revenue = report["Amount"].sum()

    print("\n----------- SALES REPORT -----------")

    for index, item in report.iterrows():
        print(
            item["Name"], ":",
            int(item["Quantity"]), "units | Revenue:",
            item["Amount"]
        )

    print("------------------------------------")
    print("Total revenue:", total_revenue)

    # Find best-selling item
    best_index = report["Quantity"].idxmax()
    best_item = report.loc[best_index]

    print(
        "Best seller:",
        best_item["Name"],
        "(" + str(int(best_item["Quantity"])) + " units)"
    )


# Main function
def main():
    create_files()

    inventory, sales = load_data()

    while True:
        print("\n===== INVENTORY + SALES MANAGEMENT =====")
        print("1. Add Item")
        print("2. Sell Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Sales Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory = add_item(inventory)

        elif choice == "2":
            inventory, sales = sell_item(inventory, sales)

        elif choice == "3":
            inventory = update_item(inventory)

        elif choice == "4":
            inventory = delete_item(inventory)

        elif choice == "5":
            sales_report(inventory, sales)

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
