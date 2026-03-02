import csv
import json

def read_csv(path):
    result = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            result.append(row)
    
    return result

def conver_age_to_int(data):
    result = []
    for item in data:
        new_item = item.copy()
        new_item["age"] = int(item["age"])
        result.append(new_item)
        
    return result    

def city_report_from_csv(data):
    result = {}
    for item in data:
        city = item["city"]
        age = item["age"]
        if city not in result:
            result[city] = {"count": 0, "total_age": 0, "avg_age": 0}
        result[city]["count"] += 1

        result[city]["total_age"] += age
    
    for item in result:
        result[item]["avg_age"] = result[item]["total_age"] / result[item]["count"]

    return result

def top_cities_from_csv(report, k):
    items = list(report.items())
    for i in range(len(items)):
        for j in range(len(items)-i-1):
            if items[j][1]["avg_age"] < items[j+1][1]["avg_age"]:
               items[j], items[j+1] = items[j+1], items[j] 
            elif items[j][1]["avg_age"] == items[j+1][1]["avg_age"] and items[j][1]["count"] < items[j+1][1]["count"]:
               items[j], items[j+1] = items[j+1], items[j]
            elif items[j][1]["avg_age"] == items[j+1][1]["avg_age"] and items[j][1]["count"] == items[j+1][1]["count"] and items[j][0] > items[j+1][0]:
               items[j], items[j+1] = items[j+1], items[j] 

    result = []
    for i in items[:k]:
        result.append(i[0])

    return result 

def save_json(new_path, data):
    with open(new_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def generate_full_report(csv_path, output_path, top_k):
    final_data = []
    data = read_csv(csv_path)
    data = conver_age_to_int(data)
    report = city_report_from_csv(data)
    top = top_cities_from_csv(report, top_k) 

    final_data = {
        "city_stats": report,
        "top_cities": top
    }

    save_json(output_path, final_data)





    

generate_full_report("people.csv", "filtered.json", 3)
#print(data)
#print(type(data))
#print(type(data[0]))
