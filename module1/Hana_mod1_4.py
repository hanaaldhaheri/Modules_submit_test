import datetime
def today_date ():

    return datetime.datetime.now().strftime("%S:%M:%H,%d/%m/%Y")
print(today_date())


def current_min():
    minute=datetime.datetime.now().minute
    n=2*minute
    ####
    a=0
    b=1
    results = []
    for i in range(n):
        results.append(a)
        a,b=b,b+a
        
    return results



print(current_min())


#the function is asked to returned to current's day in the format of (sec/min/hour) as well as (day/month/year)
#the second part is I use current min and multiple it by 2, I used Fibonacci sequence so example current min is 5
# so n=2x5=10 so 10 fibonacci sequence number.
# a=0,b=1. so(0+1=1,1+1=2,1+2=3,2+3=5,3+5=8,5+8=13,8+13=21,13+21=34) 
#display all

