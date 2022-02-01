#First Purchased
pStocks = 2000*40.00
print("Bought 2,000 shares for: ", pStocks)
print("Commission to broker: ", pStocks*.03)

#Two weeks later
sStocks = 2000*42.75
print("---------------------------------------------------")
print("Sold 2,000 shares for", sStocks)
print("Commission to broker: ", sStocks*.03)

#Total and profit/no profit
tStocks = sStocks - (pStocks+(pStocks*.03 + sStocks*.03))
print("---------------------------------------------------")
print("Amount after selling and commission: ", tStocks)
#profit check
if tStocks > 0:
    print("You have made a profit.")
else:
    print("You have not made a profit.")