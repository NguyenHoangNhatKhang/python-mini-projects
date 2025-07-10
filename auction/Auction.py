Bidders = {}
Minimum_auctional_price = int(input("Enter your price:"))
Bid_winner = False
Bid_price_orginial = int(input("Enter your bid:"))
Bid_customer_name = input("Enter your name")

if Bid_price_orginial > Minimum_auctional_price : 
    Bidders[Bid_customer_name] = Bid_price_orginial
    print("approved_____________________________________")
    print(Bidders)
    
while not Bid_winner :
    Bid_price_next = int(input("Enter your price:"))
    if Bid_price_next > Bid_price_orginial : 
        for counter in range(1,4):
            print(counter) 
            counter+=1
        print("approved")
        Bid_customer_name_next = input("Enter your name:")
        Bidders[Bid_customer_name_next] = Bid_price_next
        break
print(Bidders)