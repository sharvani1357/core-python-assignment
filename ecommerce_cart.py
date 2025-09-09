def ecommerce(n):
    total_price=sum(n.values())
    if len(n)>5:
        total_price-=total_price*10/100
        print("Total price:",total_price)
    else:
        print("Total price:",total_price)
k=list(map(str,input().split()))
v=list(map(int,input().split()))
n=dict(zip(k,v))
print("cart items=",n)
ecommerce(n)