r = lambda a:a + 15

print(r(12))

r = lambda a,b: a * b

print(r(2,12))


def commupte_mul(n):
    return lambda x: x*n

result = commupte_mul(4) 
print(result(3))

result = commupte_mul(3)
print(result(3))


def discount_strategy(discount_type):
    if discount_type == "flat_10":
        return lambda price: price - 10
    elif discount_type == "percent_20":
        return lambda price: price * 0.8
    elif discount_type == "none":
        return lambda price: price
    else:
        raise ValueError("Invalid discount type")


apply_discount = discount_strategy("percent_20")
final_price = apply_discount(100)
print(final_price)
   