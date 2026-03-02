def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        read_content = file.read().splitlines()
        return read_content

def write_file(path, data):
    with open(path, "w", encoding="utf-8") as file:
        for item in data:
            file.write(item + "\n")


def clean_file(input_path, output_path):
    try:
        lines = read_file(input_path)
    except FileNotFoundError:
        print("We can't find your file")
        return 0

    cleaned = []
    for item in lines:
        item = item.strip()
        if item and len(item) >= 4:
            cleaned.append(item.lower())

    cleaned = unique_preserve_order(cleaned)
    cleaned.sort()
    write_file(output_path, cleaned)
    return len(cleaned)

def unique_preserve_order(data):
    result = []
    for item in data:
        if item is not None and item not in result:
            result.append(item)
    
    return result


count_line = 0
input_path = "input.txt"
output_path = "output.txt" 
print(clean_file(input_path, output_path))