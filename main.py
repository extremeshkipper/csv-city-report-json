def lowercase(text):
    return text.lower()

def remove_extra_space(text):
    result = text.split()
    return " ".join(result)

def count_words(text):
    return len(text.split())

def is_polindrome(text):
    cleaned = text.lower()
    reversed_text = cleaned[::-1]
    return cleaned == reversed_text

def clean_text_list(data):
    result = []
    for item in data:
        item = item.lower()
        if len(item) >= 5:
            result.append(item)

    return result

def normalize_text(text):
    result = []
    text = text.split()
    for item in text:
        item = item.lower()
        for punctuation in '!,.?;"-':
            item = item.replace(punctuation, "")
        result.append(item)
    return " ".join(result)    
        

text = "hello!!!???"

print(normalize_text(text))