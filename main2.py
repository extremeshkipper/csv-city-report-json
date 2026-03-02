def safe_to_int(value):
    if isinstance(value, int):
        return value

    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def filter_positive(data):
    result = []
    for i in data:
        if i is not None and i >= 0:
            result.append(i)

    return result

def filter_even(data):
    result = []
    for i in data:
        if isinstance(i, int) and i % 2 == 0:
            result.append(i)

    return result

def unique_preserve_order(data):
    result = []
    for item in data:
        if item is not None and item not in result:
            result.append(item)
    
    return result

def sort_numbers(data):
    result = data.copy()
    for i in range(len(result)):
        for j in range(len(result)-i-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    
    return result

def process_numbers_v2(data):
    result = []
    for value in data:
        new_value = safe_to_int(value)
        if new_value is not None:
            result.append(new_value)
    
    
    result = filter_positive(result)
    result = filter_even(result)
    result = unique_preserve_order(result)
    result = sort_numbers(result)
    return result
    


data = ["2", 2, "abc", -4, "10", None, 3, "7", 8]

print(process_numbers_v2(data))