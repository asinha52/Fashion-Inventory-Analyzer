prices = [120, 45, 250, 80, 300, 60, 150]

premium_items = 0
budget_items = 0

for items in prices:
    if items > 100:
     premium_items = premium_items + 1
    else:
     budget_items = budget_items + 1

print("Fashion Inventory Summary:")
print("---------------------------")
print("Premium items:", premium_items)
print("Budget items:", budget_items)
