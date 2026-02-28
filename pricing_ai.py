def dynamic_price(price,demand):
    if demand>80: return price*1.15
    if demand<30: return price*0.9
    return price