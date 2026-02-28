import random

def predict_tomorrow_revenue():
    """
    Simple AI forecast using random growth logic.
    Later real ML model integrate kar sakte hain.
    """
    base = random.randint(25000, 60000)
    growth = random.uniform(1.05, 1.15)
    return int(base * growth)