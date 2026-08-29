users = [
    {"name": " Ahmed ", "age": "25", "score": 85},
    {"name": "Sara", "age": "abc", "score": 72},
    {"name": "  ", "age": "30", "score": 91},
    {"name": "Omar", "age": "17", "score": 60},
    {"name": "Mona", "age": "22", "score": 105},
]


def cleaning(users):
    final_result = []
    for user in users:
        name = user["name"]
        age = user["age"]
        if name.strip() and age.isdigit() and int(age) >= 18 and 0 <= user["score"] <= 100:
            final_result.append({"name":name.strip(), "age":age,"score":user["score"]})
    return final_result
print(cleaning(users))        