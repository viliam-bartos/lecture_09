import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as jfile:
        data = json.load(jfile)
    if field not in set(data.keys()):
        return None
    return data[field]



def main():
    seq_data = read_data("sequential.json", "unordered_numbers")
    print(seq_data)


if __name__ == '__main__':
    main()