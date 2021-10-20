import hashlib
from hashlib import sha256
import csv


def hash_password_hack(input_file_name, output_file_name):
    f = open(input_file_name)
    lines = csv.reader(f)
    hashdict = {}
    names_password = {}

    for i in range(1000, 10000):
        new_hash = sha256(str(i).encode()).hexdigest()
        hashdict[new_hash] = i
    for line in lines:
        name = line[0]
        hash_input = line[1]
        for hash_in_hashdict in hashdict.keys():
            if hash_input == hash_in_hashdict:
                names_password[name] = hashdict.get(hash_in_hashdict)

    output = open(output_file_name, 'w')
    count = 0
    for names in names_password:
        count += 1
        if count == 1:
            output.write(names + ',' + str(names_password.get(names)))
        else:
            output.write('\n' + names + ',' + str(names_password.get(names)))
    output.close()


hash_password_hack("Python Projects/input.txt", "Python Projects/output.txt")
