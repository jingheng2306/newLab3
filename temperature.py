# Lab2.py

def find_min_max(data):
    if not data:
        return None, None
    min_val = min(data)
    max_val = max(data)
    return min_val, max_val

def calc_average(data):
    if not data:
        return None
    return sum(data) / len(data)

def calc_median_temperature(temperatures):
    if not temperatures:
        return None
    sorted_temps = sorted(temperatures)
    n = len(sorted_temps)
    if n % 2 == 0:
        return (sorted_temps[n // 2] + sorted_temps[n // 2 - 1]) / 2
    else:
        return sorted_temps[n // 2]
