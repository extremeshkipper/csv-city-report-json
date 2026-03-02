import json

def read_json(path):
    with open(path, "r") as file:
        data = json.load(file)

    return data

def filter_by_city(data, city):
    new_dict = []
    for item in data:
        if item["city"] == city:
            new_dict.append(item)
    return new_dict

def filter_by_age(data, age):
    new_dict = []
    for item in data:
        if item["age"] >= age:
            new_dict.append(item)
    return new_dict

def save_json(new_path, data):
    with open(new_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def group_by_city(data):
    result = {}
    for item in data:
        city = item["city"]
        if city in result:
            result[city] += 1
        else:   
            result[city] = 1

    return result
        
def city_report(data):
    result = {}
    for item in data:
        city = item["city"]
        age = item["age"]
        if city not in result:
            result[city] = {"count": 0, "avg_age": 0, "min_age": age, "max_age": age}
        result[city]["count"] += 1
        
        if result[city]["min_age"] > age:
            result[city]["min_age"] = age

        if result[city]["max_age"] < age:
            result[city]["max_age"] = age
        
        result[city]["avg_age"] += age

    for item in result:
        result[item]["avg_age"] /= result[item]["count"]

    return result 



path = "data.json"
new_path = "filtered.json"
#city = "Lviv"
#age = 25
#data = read_json(path)
#print(filter_by_city(data, city))
#print(filter_by_age(data, age))
#data = filter_by_age(data, age)
#data = group_by_city(data)
#save_json(new_path, data)
#data = city_report(data)
#save_json(new_path, data)

