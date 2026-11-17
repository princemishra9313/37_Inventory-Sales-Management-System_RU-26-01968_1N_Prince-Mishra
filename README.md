# Inventory + Sales Management System

A simple Python-based Inventory and Sales Management System that helps manage product stock, record sales, update item details, and generate sales reports.

This project uses **Python, Pandas, and CSV files** to store and manage inventory and sales data.

## Features

- **Add Item:** Add new items with a unique ID, name, stock quantity, and price.
- **Sell Item:** Sell items and automatically update available stock.
- **Update Item:** Modify item name, stock, and price.
- **Delete Item:** Remove items from the inventory.
- **Sales Report:** Generate a report showing total quantity sold and revenue for each item.
- **Best-Selling Item:** Identify the item with the highest sales quantity.
- **Total Revenue:** Calculate total revenue from recorded sales.
- **Data Storage:** Automatically save inventory and sales records in CSV files.

## Technologies Used

- Python
- Pandas
- CSV (Comma-Separated Values)
- OS Module

## Project Structure

```text
Inventory_Sales_Management/
│
├── main.py
├── inventory.csv
├── sales.csv
└── README.md
```

### File Description

- `main.py` – Contains the main program and all functions.
- `inventory.csv` – Stores item details and available stock.
- `sales.csv` – Stores sales transactions.
- `README.md` – Project documentation.

**Note:** The CSV files are automatically created when the program runs for the first time.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-link>
```

### 2. Open the Project Folder

```bash
cd Inventory_Sales_Management
```

### 3. Install Required Library

```bash
pip install pandas
```

### 4. Run the Program

```bash
python main.py
```

## Main Menu

When you run the program, the following menu appears:

```text
===== INVENTORY + SALES MANAGEMENT =====

1. Add Item
2. Sell Item
3. Update Item
4. Delete Item
5. Sales Report
6. Exit

Enter your choice:
```

## How It Works

1. Select an operation from the main menu.
2. Add products with their stock and price.
3. Sell products using their unique item IDs.
4. The system checks stock availability before completing a sale.
5. Available stock is automatically reduced after a successful sale.
6. View the sales report to check revenue and best-selling products.
7. All records are saved in CSV files.

## Important Concepts Used

| Concept | Purpose |
|---|---|
| Functions | Organize program operations |
| Dictionaries | Store item and sales records |
| Pandas DataFrame | Manage inventory and sales data |
| CSV Handling | Store data permanently |
| `groupby()` | Calculate item-wise sales |
| `merge()` | Combine sales data with item names |
| Loops and Conditions | Handle menu operations |
| Exception Handling | Handle invalid inputs |

## Future Improvements

- Add a graphical user interface (GUI).
- Add product search functionality.
- Generate graphical sales reports.
- Add date-wise sales tracking.
- Export sales reports to Excel.

## Author

**Prince Mishra**

## License

This project is created for educational purposes.
