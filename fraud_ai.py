def fraud_score(discount,voids,override):
    return min(100,(discount*2)+(voids*5)+(override*3))