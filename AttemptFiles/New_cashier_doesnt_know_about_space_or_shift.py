def get_order(order):
    s = []
    refMenu = ["Burger","Fries","Chicken","Pizza","Sandwich","Onionrings","Milkshake","Coke"]
    for i in refMenu:
        if order.count(i.lower()) > 0:
            for j in range(order.count(i.lower())):
                s.append(i)
    s = " ".join(s)
    return s

#Test:
print(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"))