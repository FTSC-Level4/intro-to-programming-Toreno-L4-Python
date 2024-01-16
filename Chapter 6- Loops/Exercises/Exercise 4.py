import time

sandwhich_orders = ["Grilled Cheese", "Chicken Sandwhich", "Egg Sandwhich"]
finished_sandwhiches = []
item = 0
listsize = len(sandwhich_orders)

while sandwhich_orders:
    if item != listsize:
        print("I finished making your", sandwhich_orders[item])
        finished_sandwhiches.append(sandwhich_orders[item])
        item = item + 1
        time.sleep(1.5)
    else:
        print(f'These are your finished sandwhiches: {finished_sandwhiches}')
        sandwhich_orders.clear()
        time.sleep(1)
        break
    
