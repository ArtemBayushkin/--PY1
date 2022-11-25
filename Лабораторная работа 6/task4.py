INPUT_FILE = "input.csv"
OUTPUT_FILE = "output.json"


def csv_to_list_dict(file_1, file_2, delimiter=",", nl='\n', indent=4*" ", sk=2) -> list[dict]:
    with open(file_1) as input_:
        with open(file_2, 'w') as output:
            list_ = []
            headers = input_.readline().rstrip(nl).split(delimiter)
            for line in input_:
                data = line.rstrip(nl).split(delimiter)
                list_.append(dict(zip(headers, data)))
            output.write("[")
            for line1 in list_:
                output.write(indent*sk +
                             str(line1).replace(delimiter, delimiter + nl + indent * sk).replace("}", nl + 
                             indent + "},").replace("{'", nl + indent + "{" + nl + indent * sk + " '"))
            output.write(nl+"]")
    return list_


csv_to_list_dict(INPUT_FILE, OUTPUT_FILE)

with open(OUTPUT_FILE) as f:
    for line in f:
        print(line)
