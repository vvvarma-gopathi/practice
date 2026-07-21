""" parking prices 
    1st 2hours=100 fixed
    next 3 hours=400
    next 7 hours=300
    hours above 12 and with in 24 =500 fixed   """
def parking_price(hours):
    price=0
    if 12<hours<=24: #hours between 12 and 24 500 fixed
        price=500
    elif hours>=2:
        price=100 #2 hours fixed 100
        hours-=2
        if 0<hours:
            if hours>=3: 
                price+=40*3 #for next 3 hours after 2 hours
                hours-=3
                if hours>0:
                    if hours<=7: #for next 7 hours after 2+3 hours
                        temp=hours
                        for i in range(temp):
                            price+=30
                            hours-=1
            elif hours<3:  #within next 3 hours after 2 hours doesnt exceed 3 hours
                temp=hours
                for i in range(temp):
                    price+=40
                    hours-=1
    return price
hours=int(input("Enter parking hours:"))
if 0>=hours or hours>24:
    print("Invalid parking hours")
else:
    print("Price of parking is:",parking_price(hours))