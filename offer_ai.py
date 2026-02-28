def generate_offer(today_guests):

    if today_guests < 40:
        return "🔥 Flat 20% OFF + Free Dessert"

    elif today_guests < 80:
        return "🍹 Buy 1 Get 1 Mocktail"

    else:
        return "🎉 VIP Combo Offer + Free Drink"
