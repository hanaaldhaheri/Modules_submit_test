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


