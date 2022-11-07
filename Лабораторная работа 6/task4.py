import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as file:
        list_ = []
        headers = file.readline().rstrip().split(",")
        for index, line in enumerate(file):
            data = line.rstrip().split(",")
            list_.append({})
            for i, _ in enumerate(headers):
                list_[-1][headers[i]] = data[i]
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
