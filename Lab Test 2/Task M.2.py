def cart_total(cart):
    total = 0
    for item, (price, qty) in cart.items():
        total += price * qty
    return total

cart = {
    "apple": (3, 2),
    "banana": (5, 1)
}

print(cart_total(cart))

