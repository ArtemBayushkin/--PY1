import json

INPUT_FILE = "input.csv"


def csv_to_list_dict() -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
