import os
import json

#fork z githubu, naklonovat, jít do složky s ukolem, git remote add upstream "url toho forknuteho ukolu", git branch "jmeno"
#git checkout "jmeno vetve"
#zkontrolovat git remote -v

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


def linear_search(seq, num):
    vyskyt = 0
    index = []
    for i, n in enumerate(seq):
        if n == num:
            vyskyt += 1
            index.append(i)
    slovnik = {
        "positions": index,
        "count": vyskyt
    }
    return slovnik



def pattern_search(seq, vzor):      #do sebe vnořené cykly se mezi sebou násobí takže nejhorší scénář O = n*n
    mnozina = set()
    j = 0
    for i in range(0, len(seq)):
        idx = 0
        for letter in seq[i:i + len(vzor)]:
            if letter != vzor[idx]:
                break
            else:
                idx += 1

        if idx == len(vzor):
            mnozina.add(j)
        """
        if seq[i:i + len(vzor)] == vzor:
            mnozina.add(j)
        """
        j += 1
    return mnozina



def binary_search(seq, num):
    """
    while True:
        if seq[int((len(seq) - 1) / 2)] == num:
            return int((len(seq) - 1) / 2)
        elif seq[int((len(seq) - 1) / 2)] > num:
            seq = seq[:int((len(seq) - 1) / 2)]
        elif seq[int((len(seq) - 1) / 2)] < num:
            seq = seq[int((len(seq) - 1) / 2):]
    """
    left = 0
    right = len(seq) - 1
    while left < right:
        middle = (left + right) // 2
        if seq[middle] == num:
            return middle
        elif seq[middle] < num:
            left = middle + 1
        elif seq[middle] > num:
            right = middle - 1
    return None










def main():
    seq_data = read_data("sequential.json", "unordered_numbers")
    print(seq_data)

    dict = linear_search(seq_data, 9)
    print(dict)

    dna = read_data("sequential.json", "dna_sequence")
    print(dna)
    mnozka = pattern_search(dna, "ATA")
    print(mnozka)

    serazene = read_data("sequential.json", "ordered_numbers")
    print(serazene)
    cislo = binary_search(serazene, 8)
    print(cislo)




if __name__ == '__main__':
    main()