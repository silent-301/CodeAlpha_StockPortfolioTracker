STOCK_PRICES = {"APPLE": 180.0, "TESLA": 250.0, "MICROSOFT": 420.0, "GOOGLE": 145.0, "AMAZON": 155.0}

def main():
    
    print("=== Stocks Tracker ===")
    print()
    print("=== Available Stocks ===")
    for s, p in STOCK_PRICES.items():
        print(f"{s}: ${p}")
    
    portfolio = {}

    while True:
        symbol = input("\nEnter stock symbol (or Enter to finish): ").upper().strip()
        if not symbol: break
        
        if symbol in STOCK_PRICES:
            qty = input(f"How many shares of {symbol}?: ")
            if qty.isdigit() and int(qty) > 0:
                portfolio[symbol] = portfolio.get(symbol, 0) + int(qty)
            else:
                print("Invalid quantity.")
        else:
            print("Stock not found. Please choose from the list above.")

    if not portfolio: return print("\nNo stocks added. Exiting.")

    print("\n" + "="*25 + "\nYOUR PORTFOLIO\n" + "="*25)
    total = 0
    csv_data = "Symbol,Quantity,Price,Value\n"
    
    for sym, qty in portfolio.items():
        price = STOCK_PRICES[sym]
        value = qty * price
        total += value
        print(f"{sym:10} | {qty} shares | Total: ${value:.2f}")
        csv_data += f"{sym},{qty},{price},{value:.2f}\n"

    print(f"{'='*25}\nGRAND TOTAL: ${total:.2f}")

    if input("\nSave to portfolio.csv? (y/n): ").lower() == 'y':
        with open("portfolio.csv", "w") as f:
            f.write(csv_data + f"TOTAL,,,${total:.2f}")
        print("File saved successfully.")

if __name__ == "__main__":
    main()