

import csv
import os

print("📊 Welcome to Stock Portfolio Tracker!")
print("Track, update, and manage your investments easily.\n")


print("👤 ACCOUNT SETUP")
username = input("Enter your name to create/login: ").strip().capitalize()

# Create personal file names
csv_filename = f"{username}_portfolio.csv"
txt_filename = f"{username}_portfolio.txt"

print(f"\n✅ Welcome, {username}! Your portfolio will be saved as '{csv_filename}' and '{txt_filename}'.\n")


portfolio = {}
total_investment = 0.0

# Create CSV file with header if missing
if not os.path.exists(csv_filename):
    with open(csv_filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Symbol", "Quantity", "Price ($)", "Value ($)"])

# ✅ Step 3: Safely Load Existing Data
if os.path.exists(csv_filename):
    with open(csv_filename, "r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if not row:
                continue
            try:
                symbol = row.get("Stock Symbol", "").strip()
                qty = int(float(row.get("Quantity", 0)))
                price = float(str(row.get("Price ($)", 0)).replace(",", "").strip())
                value = float(str(row.get("Value ($)", 0)).replace(",", "").strip())
                if symbol:
                    portfolio[symbol] = {"price": price, "quantity": qty, "value": value}
                    total_investment += value
            except Exception:
                continue


def save_portfolio():
    """Rewrites the portfolio into CSV and TXT files."""
    global total_investment
    total_investment = sum(info['value'] for info in portfolio.values())

    # Save CSV
    with open(csv_filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock Symbol", "Quantity", "Price ($)", "Value ($)"])
        for symbol, info in portfolio.items():
            writer.writerow([symbol, info["quantity"], f"{info['price']:.2f}", f"{info['value']:.2f}"])

    # Save TXT
    with open(txt_filename, "w") as txt_file:
        txt_file.write(f"Portfolio Owner: {username}\n")
        txt_file.write("Stock Symbol | Quantity | Price ($) | Value ($)\n")
        txt_file.write("-" * 50 + "\n")
        for symbol, info in portfolio.items():
            txt_file.write(f"{symbol:6} | {info['quantity']:8} | ${info['price']:8.2f} | ${info['value']:8.2f}\n")
        txt_file.write("-" * 50 + "\n")
        txt_file.write(f"Total Investment: ${total_investment:.2f}\n")

    print("💾 Portfolio updated and saved!\n")

# ------------------------------
# Step 5: Main Menu Loop
# ------------------------------
while True:
    print(f"\n🔹 OPTIONS for {username}: add / update / delete / show / done")
    action = input("Enter your choice: ").lower().strip()

    if action == "done":
        break

    # ADD NEW STOCK
    elif action == "add":
        stock_symbol = input("Enter stock symbol: ").upper().strip()
        if not stock_symbol:
            print("⚠️ Invalid symbol.")
            continue

        try:
            price = float(input(f"Enter price for {stock_symbol}: $"))
            quantity = int(input(f"Enter quantity of {stock_symbol}: "))
            investment = price * quantity
            confirm = input(f"Save {stock_symbol}? (yes/no): ").lower().strip()
            if confirm == "yes":
                portfolio[stock_symbol] = {"price": price, "quantity": quantity, "value": investment}
                save_portfolio()
                print(f"✅ {stock_symbol} added successfully!")
            else:
                print("❌ Skipped saving this stock.")
        except ValueError:
            print("⚠️ Please enter valid numbers for price and quantity.")

    # UPDATE STOCK
    elif action == "update":
        stock_symbol = input("Enter stock symbol to update: ").upper().strip()
        if stock_symbol not in portfolio:
            print("⚠️ Stock not found.")
            continue
        print(f"Current → Qty: {portfolio[stock_symbol]['quantity']} | Price: ${portfolio[stock_symbol]['price']:.2f}")
        try:
            new_price = float(input("Enter new price: $"))
            new_quantity = int(input("Enter new quantity: "))
            portfolio[stock_symbol] = {
                "price": new_price,
                "quantity": new_quantity,
                "value": new_price * new_quantity
            }
            save_portfolio()
            print(f"✅ {stock_symbol} updated successfully!")
        except ValueError:
            print("⚠️ Invalid input! Update canceled.")

    # DELETE STOCK
    elif action == "delete":
        stock_symbol = input("Enter stock symbol to delete: ").upper().strip()
        if stock_symbol in portfolio:
            confirm = input(f"Are you sure you want to delete {stock_symbol}? (yes/no): ").lower().strip()
            if confirm == "yes":
                del portfolio[stock_symbol]
                save_portfolio()
                print(f"🗑️ {stock_symbol} deleted successfully!")
            else:
                print("❌ Deletion canceled.")
        else:
            print("⚠️ Stock not found in portfolio.")

    # SHOW PORTFOLIO
    elif action == "show":
        print(f"\n💼 {username}'s Portfolio Summary")
        print("-" * 50)
        for symbol, info in portfolio.items():
            print(f"{symbol:6} | Qty: {info['quantity']:3} | Price: ${info['price']:6.2f} | Value: ${info['value']:8.2f}")
        print("-" * 50)
        print(f"Total Investment Value: ${sum(info['value'] for info in portfolio.values()):.2f}")

    else:
        print("⚠️ Invalid option! Please type add / update / delete / show / done.")

# ------------------------------
# Step 6: Final Summary
# ------------------------------
print(f"\n📘 Final Portfolio Summary for {username}")
print("-" * 50)
for symbol, info in portfolio.items():
    print(f"{symbol:6} | Qty: {info['quantity']:3} | Price: ${info['price']:6.2f} | Value: ${info['value']:8.2f}")
print("-" * 50)
print(f"Total Investment Value: ${sum(info['value'] for info in portfolio.values()):.2f}")
print(f"✅ Data saved in '{csv_filename}' and '{txt_filename}'")
print(f"👋 Goodbye, {username}! Your portfolio has been safely stored.")



