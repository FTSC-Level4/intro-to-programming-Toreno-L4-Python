import time

sandwhich_orders = ["Grilled Cheese", "Pastrami Sandwhich", "Chicken Sandwhich", "Pastrami Sandwhich", "Egg Sandwhich", "Pastrami Sandwhich"]
finished_sandwhiches = []
Pastrami_supply = 0 #No more Pastrami :(
check_pastrami = 0 #value used to check for pastrami
item = 0 #value used to check and move up the listing in order
loop = "true"
listsize = len(sandwhich_orders)

print("Apologies dear customers but we have run out of Pastrami and will therefore cancel and refund all your Pastrami orders.\n")
time.sleep(1)

while loop == "true":

    if "Pastrami Sandwhich" in sandwhich_orders: #Detects if the list still has an idex with "Pastrami Sandwhich"

        if sandwhich_orders[check_pastrami] == "Pastrami Sandwhich":
            
            sandwhich_orders.pop(check_pastrami)
            check_pastrami = check_pastrami + 1

        else:

            check_pastrami = check_pastrami + 1

    else:

        if item != listsize:

            print("I finished making your", sandwhich_orders[item])
            finished_sandwhiches.append(sandwhich_orders[item])
            item = item + 1
            listsize = listsize - 1
            time.sleep(2)

        else:

            print(f'These are your finished sandwhiches: {finished_sandwhiches}')
            sandwhich_orders.clear()
            time.sleep(1)
            break
    