prices = [120, 45, 250, 80, 300, 60, 150]

for i in range(len(prices)):
    if prices[i] > 100:
        old_price = prices[i]
        prices[i] = prices[i] * 0.8
        print("Premium item:", old_price, "->", prices[i])

print("Final prices:", prices)

