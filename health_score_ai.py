def health_score(sales,growth,fraud):
    return max(0,min(100,(sales+growth)-(fraud)))