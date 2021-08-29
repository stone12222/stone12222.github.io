n=655.665

# wrong
print(round(n,2))
print("%.2f" % n)

# correct
n=655.664
print(n+0.005)
print(int((n+0.005)*100)/100)

nn=-655.665
print(int((nn-0.005)*100)/100)

def r(num,decimalPlace):
    f = 0.5 / (10 ** decimalPlace)
    if num<0:
        num=int((num-f)*(10**decimalPlace))/(10**decimalPlace)
    else:
        num=int((num+f)*(10**decimalPlace))/(10**decimalPlace)
    return num

print(r(n,2))
print(r(-n,2))


