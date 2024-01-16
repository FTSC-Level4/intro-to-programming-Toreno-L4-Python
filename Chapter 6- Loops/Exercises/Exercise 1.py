toppings_list = []
loop = "true"

while loop == "true":

    toppings = input('Please enter a topping for your pizza or type "quit" to stop: ')
    if toppings == "quit" or toppings == "Quit" or toppings == "QUIT":
        print(f'These are your chosen and final toppings: {toppings_list}')
        loop == "false"
    else:
        toppings_list.append(toppings)
        print("I will add",toppings,"to your pizza.")
        print(f'These are your current toppings:{toppings_list}\n')
        
    
   
            
            

  

    
    

    
        
    