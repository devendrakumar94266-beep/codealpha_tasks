                          ##Stock Portfolio Tracker

prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330, "AMZN": 130}
portfolio = {}

print("Available stocks:", list(prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'stop' to finish): ").upper()
    
    if stock == 'STOP':
        break
        
    if stock in prices:
        qty_input = input("Enter quantity for " + stock + ": ")
        qty = int(qty_input)
        
        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty
    else:
        print("Stock not found in our list.")

print("\n--- Portfolio Summary ---")
total_investment = 0
summary_text = "--- Portfolio Summary ---\n"

for s in portfolio:
    stock_qty = portfolio[s]
    stock_price = prices[s]
    value = stock_qty * stock_price
    total_investment += value
    
    line = s + " : " + str(stock_qty) + " shares. Value = $" + str(value)
    print(line)
    summary_text += line + "\n"

total_line = "\nTotal Investment: $" + str(total_investment)
print(total_line)
summary_text += total_line + "\n"

save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower()

if save_choice == 'yes':
    file = open("portfolio_summary.txt", "w")
    file.write(summary_text)
    file.close()
    print("Summary saved to portfolio_summary.txt successfully.")
