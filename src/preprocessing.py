def normalize_data(data):
    if not data:
        return []
    min_val = min(data)
    max_val = max(data)
    if max_val == min_val:
        return [0] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]