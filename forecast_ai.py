import random

def predict_tomorrow_revenue(today_revenue):
    growth = random.uniform(1.08, 1.18)
    return int(today_revenue * growth)
