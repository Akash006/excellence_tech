
def max_score(data: dict) -> dict:
    count = {"-1": "-1"}

    for val in data.keys():
        if count:
            key = list(count.keys())[0]

        if data.get(val) == int(count.get(key)):
            count[val] = data.get(val)
        elif data.get(val) > int(count.get(key)):
            count.clear()
            count[val] = data.get(val)

    return count

if __name__ == '__main__':

    # userid is in str as mention in doc
    uname = {
        "1" : "Akash",
        "2" : "Sagar",
        "3" : "Excellence Technlogies",
        "4" : "Sandeep",
        "5" : "Rahul",
        "6" : "Sidharth"
    }

    exam_score = {
        "1" : 50,
        "2" : 60,
        "3" : 70,
        "4" : 80,
        "5" : 50,
        "6" : 80,
    }
    
    result = max_score(exam_score)

    print(result)