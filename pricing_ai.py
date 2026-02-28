def dynamic_price(base_price, crowd_level):
    if crowd_level == "LOW":
        return int(base_price * 0.90)
    elif crowd_level == "HIGH":
        return int(base_price * 1.15)
    return base_price
