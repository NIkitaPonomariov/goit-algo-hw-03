from datetime import datetime
import random

#перевірочка функція

def test(x,y:int):
 print("pass") if(x==y) else print("fail")

#1
def get_days_from_today(date):
    try:
        g_date = datetime.strptime(date, '%Y-%m-%d').date()
        t_date = datetime.today().date()
        res = t_date -g_date
        return res.days
    except ValueError:
        return "please try with correct values"

#first homework test!
test(get_days_from_today('2024-04-16'),1)



#2

def get_numbers_ticket(min, max, quantity):
    x=[]
    try:
        if min >=1 and max <= 1000 and min < quantity < max and min<max:
            for i in range(quantity):
                x.append(random.sample(range(min, max+1), quantity))
            x.sort()
            return x
        else:
            return "u have wrong values for this function"
    except ValueError:
        return "please enter correct values"
    

# перевірка другого завдання

test(get_numbers_ticket(10,3,5),"u have wrong values for this function")
test(get_numbers_ticket(-2,1001,5),"u have wrong values for this function")
test(get_numbers_ticket(5,10,43),"u have wrong values for this function")