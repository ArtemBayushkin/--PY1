INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.csv"


def csv_to_list_dict(file_1, file_2, delimiter=",", nl='\n') -> list[dict]:
    with open(file_1) as input_:
        with open(file_2, 'w') as output:
            list_ = []
            headers = input_.readline().rstrip(nl).split(delimiter)
            for line in input_:
                data = line.rstrip(nl).split(delimiter)
                list_.append(dict(zip(headers, data)))
            for line1 in list_:
                    output.write(str(line1)+nl)
    return list_


print(csv_to_list_dict(INPUT_FILE, OUTPUT_FILE))
