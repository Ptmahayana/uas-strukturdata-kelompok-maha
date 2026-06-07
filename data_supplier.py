suppliers = {
    "Supplier A": {"price": 85, "distance": 10, "quality": 90, "delivery_time": 3},
    "Supplier B": {"price": 70, "distance": 25, "quality": 75, "delivery_time": 5},
    "Supplier C": {"price": 90, "distance": 15, "quality": 95, "delivery_time": 2},
    "Supplier D": {"price": 60, "distance": 40, "quality": 65, "delivery_time": 7},
    "Supplier E": {"price": 80, "distance": 20, "quality": 85, "delivery_time": 4}
}

# Bobot kriteria (bisa diatur user)
weights = {
    "price": 0.4,
    "distance": 0.2,
    "quality": 0.3,
    "delivery_time": 0.1
}

def normalize(value, min_val, max_val, is_cost=True):
    if is_cost:
        return (max_val - value) / (max_val - min_val)  # semakin kecil semakin baik
    else:
        return (value - min_val) / (max_val - min_val)  # semakin besar semakin baik