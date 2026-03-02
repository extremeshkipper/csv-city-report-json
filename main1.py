def filter_even(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)

    return result

def find_max(numbers):
        max_numbers = numbers[0]
        for i in numbers[1:]:
            if max_numbers < i:
                max_numbers = i

        return max_numbers

def remove_duplicates(data):
     result = []
     for item in data:
          if item not in result:
               result.append(item)
          
     return result  
          
def sort_by_numbers(data):
     for i in range(len(data)):
          for j in range(len(data)-i-1):
               if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]

     return data

def process_numbers(data):
    result = []
    for i in data:
         if i >= 0:
              result.append(i)
    
    result = filter_even(result)
    result = remove_duplicates(result)
    sort_by_numbers(result)
    
    return result



data = [-3, 2, 2, 5, 8, -1, 4]

print(process_numbers(data))